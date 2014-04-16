MAKE = make
DOCDIR = docs

install:
	pip install -r requirements.txt

build:
	curl -X POST http://readthedocs.org/build/zhengkun

html:
	cd $(DOCDIR) && $(MAKE) clean && $(MAKE) html

run:
	cd $(DOCDIR) && $(MAKE) run PORT=$(PORT)
