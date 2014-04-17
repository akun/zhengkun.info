MAKE = make
DOCDIR = docs
BUILDDIR = blog/html

install:
	pip install -r requirements.txt

build:
	curl -X POST http://readthedocs.org/build/zhengkun

html:
	cd $(DOCDIR) && tinker --build

run:
	cd $(DOCDIR)/$(BUILDDIR) && python -m SimpleHTTPServer $(port)
