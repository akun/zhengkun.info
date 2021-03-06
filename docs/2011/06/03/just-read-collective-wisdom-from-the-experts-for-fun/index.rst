书摘：《程序员应该知道的97件事》
================================

读书的乐趣之一在于，作者的文字能表达出你想要说的。表达能力差就这点不好，只能在自己的世界徘徊，所以没事瞎读书，给人喷的时候，就各种引用了。

下面只是简单书摘，寻找有共鸣文字，加入下自己感言，纯粹好玩。

**P2**

**《谨慎行动》**

避免技术债务！

*kun的感言：这可是高利贷啊，没事别瞎玩！*

**P6**

**《试问自己“用户会怎么做”（你不能算是用户）》**

要想知道用户的想法，最好的办法是观察一个用户，要求用户使用功能类似的小软件完成一项任务，并确保任务是一项真实的业务。

*kun的感言：真正用你产品的人，你都应该感谢他，真的！*

**P16**

**《童子军规则》**

“要让离开时的营地比进入时更加干净”“让模块签入（check in）的时候比签出（check out）的时候更整洁”

*kun的感言：做人也是，你离开世界的时候能让世界变得更美好，哪怕一点也行！*

**P22**

**《领域语言里的代码》**

几个月后，前来接受代码的程序员将会感谢你。那个程序员很可能就是你自己。

*kun的感言：因为总有一种惶恐，担心接受你代码的程序员是个疯子。*

**P28**

**《代码审查》**

另外，在代码审查会议上，对代码格式应该不作评论。促使审核成功的最大因素可能是让这一过程充满乐趣，审查是由人来做的，如果审查会议室痛苦的或无趣的，那就难以激发人们的积极性。那不如发起一次不太正式的代码审查，主要着眼于在团队成员之间分享知识，抛开讽刺性的评语，带着蛋糕或自带午餐做到一起。

*kun的感言：让人愉悦，才能让人接受。*

**P36**

**《不断学习》**

你需要不断学习，才能保持自己“市场号召力”。否则，你就会变成恐龙，在同一个职位上日复一日，直到有一天，你不再被需要，或者你的工作被外包给了某个更便宜的机构。

*kun的感言：If You Can’t Be Replaced, You Can’t Be Promoted.*

**P42**

**《区分业务异常和技术异常》**

区分这些情况会使应用框架结构更清晰，能更有效地处理技术异常，而业务领域异常则由客户端代码来妥善处理。

*kun的感言：技术异常，网络超时，数组越界（前提是还没意识到需要业务层面处理时候）；业务异常，Web开发中常见的表单验证出错。*

**P53**

**《不要忽略那个错误》**

不要掩盖它们，也不要假装你的服务总是能运转的。

*kun的感言：程序不会说谎！*

**P58**

**《不要指望“魔法会在此发生”》**

你不必去理解所有让你项目运转的魔法，但是，你去理解其中的一些也不会对你有什么损害——或者，还要感谢一下那些你所不知的人。最重要的是，要确保魔法停止的时候，它还能够再次显现。

*kun的感言：可能团队中的某个人，某个流程有你所想不到的用处，如果去掉，可能魔法就会发生了。*

**P74**

**《加班加点，事倍功半》**

但是，真实情况是少做一些，可能会出更多成绩——有时时多得多。你应该考虑一下消减你的工作量，提升效率，从而完成更多任务。为了避免无效工作，你必须有时间去观察你手头上工作的影响，思考你所看到的情况，并随之调整你的行为。作为一个专业程序员，你必须让你的专业领域知识保持最新。因此，你不能把你的晚上、周末和假期都用在项目加班上。工作准备和接受教育才是他们（类似程序员这种技术工种的脑外科医生和飞行员）职业的核心部分。作为一名专业程序员，你应该知道努力达成每周60小时的专注和“产出”不是一件明智的事情。要像一个专业人员一样：充分准备、付诸实施、观察、反省和改变。

*kun的感言：的确，不解释。*

**P76**

**《如何使用bug跟踪器》**

一份好的bug报告需要具备三样东西：• 如何重现该bug，尽可能准确的描述，间隔多久后bug会再出现一次。• 本应该发生什么，至少按你自己的见解来说。• 实际上发生了什么，或者至少是你记录到的尽可能多的信息。

*kun的感言：让人心悦诚服的接受你提交的bug。*

**P78**

**《代码的去芜存菁》**

YAGNI原则（即You Aren’t Gonna Need It）

*kun的话：该删代码时候要毫不留情，特别是你用了版本控制工具了。*

**P95**

**《知道你下次提交的内容》**

如果你无法完成，就丢弃掉更改，然后按照你已有的理解，定义出一项你确信能能完成的新任务。

*kun的话：这很重要，要先动起来，别被一座山压的死死的。*

**P110**

**《使接口易用正确使用，难于错误使用》**

总之，要记住接口的存在是为了方便使用者，而不是实现者。

*kun的话：API程序员接口（程序）之于应用程序员，应用程序员接口（界面）之于用户。*

**P114**

**《在并行系统中使用消息传递可获得更好的伸缩性》**

问题的答案也很明显：要么放弃并发，要么避免共享内存。我们可以在编程模型中使用进程和消息传递，来替换原先使用的线程和共享内存。总之，要想充分驾驭计算机硬件内建的并行能力，使用消息传递是一条比共享内存编程更为成功的路径。

*kun的话：个人智商有限，一切能简单处理就简单处理，用有限的智商享受无限的乐趣。*

**P139**

**《放下鼠标，原理键盘》**

有时，为了解决一个问题，你能采用的最好办法就是放下鼠标，远离键盘。

*kun的话：让你的潜意识帮助你思考！*

**P144**

**《经常重新发明轮子》**

重新发明轮子不只是在某个位置上重新拼凑代码，而是一个如何从众多已存在的组件中领会其内部工作方式的过程。

*kun的话：作者之意应该是让你更深入的理解原理吧，从而更好的使用轮子，即使你不想发明轮子的时候。*

**P152**

**《单一职责原则》**

优秀设计的最根本原则之一是：把所有会为同一个原因而更改的东西汇集在一起，把所有会为不同理由而更改的东西独立开来。

*kun的话：也就是传说中的，各回各家，各找各妈！*

**P164**

**《在睡觉的时候（或度周末的时候）进行测试》**

多数时候，这台测试服务器是整晚、整个周末都空闲着。你可以用它来做你的事情。• 你有没有过这样的罪恶感：没有运行完所有测试就提交了更改？• 你是否有足够多的机会测试产品的稳定性？• 你有没有在你的性能测试环境里得到过黄金时间？• 是否有太多的配置组合需要手工测试？

*kun的话：这是很现实的目标，而非共产主义，努力实践中！*

**P168**

**《关于状态的思想》**

…把咖啡因转化为代码的日子…

*kun的话：纯粹对这句话很有感觉而记录，无它*

**P180**

**《冗长的日志会让你睡不安枕》**

太多的日志等于没有日志。一份混乱的日志只表明一件事，那就是一旦系统在产品环境里运行，就将难以控制。如果你不希望所有东西都出现在错误日志里，那就更容易知道当有些东西出现时，接下来你要做的是什么。

*kun的话：在这个信息爆炸的时代，你还好意思再让日志哪怕再多一个字节吗？！*

**P188**

**《使用实例编写小函数》**

测试无法证明软件里没有bug。尽管测试能够证明现有的功能，但是，我们仍然有着大小的问题。

*kun的话：测试的目的是啥？反正不是为了发现bug而测试，引用我觉得合理的话：“简言之，测试的目的应该是验证需求，bug（预期结果与实际结果之间的差别）是这个过程中的产品而非目标。测试人员应该象工兵一样，在大部队（客户）预期前进的方向上探雷、扫雷（bug），而不需要去关心那些根本没有人会去碰的地雷。”*

.. author:: default
.. categories:: 随便摘录
.. tags:: 程序员
.. comments::
