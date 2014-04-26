Django 大文件下载问题处理
=========================

问题出现
--------

你的Web应用可能会提供下载文件的功能。下载个几百KB乃至几个MB的文件直接用open读取文件返回response就可以了。内存它也不在乎你占用它那么点空间。但是，如果下载个几百M乃至几个G的文件直接用open读取文件返回response那就悲剧了，内存可不乐意一下子被你占用这么多空间。

问题解决
--------

解决方法网上相关文章很多，比如：http://djangosnippets.org/snippets/365/

简单说就是用FileWrapper类来迭代器化一下文件对象，实例化出一个经过更适合大文件下载场景的文件对象，具体实现可以看源代码：django/core/servers/basehttp.py中的FileWrapper类的实现。

实现原理相当与把内容一点点从文件中读取，放到内存，下载下来，直到完成整个下载过程。这样内存就不会担心你一下子占用它那么多空间了。

新的问题
--------

也许你有又会碰到一个新的问题，下载下来的文件竟然是个空文件。

如果你单步跟踪调试会发现文件内容返回的response在通过各个中间件过程中会被提前使用，最后发现是gzip这个中间件的一段代码对response取了下len，导致提前使用了这个迭代器化的文件对象，从而response返回内容没有了，表现为下载了一个空文件。

继续处理
--------

这个时候你有很多选择：

* 继续用FileWrapper，不用gzip中间件
* 继续用gzip中间件，直接重写FileWrapper
* 重写gzip中间件，继续用FileWrapper

看了下Django源码，会发现重写gzip中间件会比较靠谱，只要简单修改一段代码逻辑即可。

但要有效，必须在下载的views代码的response返回值中设置个header。

遗留问题
--------

其实更治本的办法应该是重写FileWapper，因为保证不了其它中间件或其它组建进行了类似gzip中间件的处理。

Django官网也有相关讨论，里面还有各种思路：https://code.djangoproject.com/ticket/2131

问题发现和处理使用的Django版本是1.3.0，也许未来Django应该会提供更好的官方解决方案吧。

代码片段
--------

下载的views代码片段如下：

::

   def tarball(request, release):

       file_name = 'dj-download-%s.tar.gz' % release
       file_path = os.path.join(FILE_FOLDER, file_name)
       try:
           tarball_file = open(file_path)
       except IOError:
           raise Http404
       wrapper = FileWrapper(tarball_file)
       response = HttpResponse(wrapper, content_type='application/zip')
       response['Content-Encoding'] = 'utf-8'  # 设置该值gzip中间件就会直接返回而不进行后续操作
       response['Content-Disposition'] = 'attachment; filename=%s' % file_name
       return response

修改Django的gzip中间件代码片段如下：

::

   def process_response(self, request, response):
       # Avoid gzipping if we've already got a content-encoding.
       if response.has_header('Content-Encoding'):
           return response

       # It's not worth compressing non-OK or really short responses.
       if response.status_code != 200:
           return response
       if len(response.content) < 200:
           return response

       patch_vary_headers(response, ('Accept-Encoding',))
       # ... 省略的代码


相应对比Django的gzip中间件代码片段如下：

::

   def process_response(self, request, response):
       # It's not worth compressing non-OK or really short responses.
       if response.status_code != 200 or len(response.content) < 200:
           return response

       patch_vary_headers(response, ('Accept-Encoding',))

       # Avoid gzipping if we've already got a content-encoding.
       if response.has_header('Content-Encoding'):
           return response
       # ... 省略的代码

代码实例下载：

https://github.com/akun/dj-download/archives/master

.. author:: default
.. categories:: Django Django
.. tags:: Django, gzip, middleware, 中间件, 大文件下载
.. comments::
