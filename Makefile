MAKE = make
DOCDIR = docs
BUILDDIR = blog/html

html:
	cd $(DOCDIR) && tinker --build

install:
	pip install -r requirements.txt

build:
	curl -X POST http://readthedocs.org/build/zhengkun

run:
	cd $(DOCDIR)/$(BUILDDIR) && python -m SimpleHTTPServer $(port)
