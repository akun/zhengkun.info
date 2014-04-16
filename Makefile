MAKE = make
DOCDIR = docs

install:
	pip install -r requirements.txt

html:
	cd $(DOCDIR) && $(MAKE) clean && $(MAKE) html

run:
	cd $(DOCDIR) && $(MAKE) run PORT=$(PORT)
