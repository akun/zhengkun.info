MAKE = make
DOCDIR = docs
BUILDDIR = blog/html
TARFILE = html.tar.bz2
HOST = user@host  # eg: jack@192.168.1.1
STATIC = /www/blog  # blog root folder

html:
	cd $(DOCDIR) && tinker --build

install:
	pip install -r requirements.txt

build:
	curl -X POST http://readthedocs.org/build/zhengkun

run:
	cd $(DOCDIR) && python -m SimpleHTTPServer $(port)

upload:
	cd $(DOCDIR)/$(BUILDDIR) && \
	tar jcvf $(TARFILE) * && \
	ssh $(HOST) "if [ -d $(STATIC) ]; then echo 'exists' ;else mkdir $(STATIC); fi" && \
	scp $(TARFILE) $(HOST):$(STATIC) && \
	ssh $(HOST) "tar jxvf $(STATIC)/$(TARFILE) -C $(STATIC); rm $(STATIC)/$(TARFILE)" && \
	rm $(TARFILE)
