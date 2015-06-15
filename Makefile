# Copyright (C) 2015 Legrand France
# All rights reserved

# Simple makefile for pyzigbee development

TEST_ARGS = -v
ifeq ($(WITH_COVERAGE), yes)
	TEST_ARGS += --with-coverage --cover-package=pyzigbee --cover-erase
endif


test:
	@echo "Running tests..."
	PYTHONPATH=. nosetests $(TEST_ARGS)
	@echo "Done."

doc:
	@echo "Building documentation..."
	@cd docs && PYTHONPATH=.. make SPHINXOPTS=-j4 html && cd ..
	@echo "Done."
	@echo "Open docs/_build/html/index.html with your favourite browser"docs/_build/html/index.html
	@echo
	@echo "sensible-browser docs/_build/html/index.html &"
	@echo

egg:
	@echo "Building egg..."
	PYTHONPATH=. python setup.py bdist_egg
	@echo "Done."

pep8:
	@echo "Cheking PEP8 coding style..."
	@pep8 . --exclude="docs,test*" --max-line-length=90 --ignore=E127,E265
	@echo "Done."

check-shell:
	@echo "Checking shell (check imports)..."
	@PYTHONPATH=. python pyzigbee/shell/pyzigbeesh.py --check
	@echo "Done."

check: test doc pep8 check-shell

python: test pep8

clean: clean-bytecode clean-doc clean-egg clean-build

clean-bytecode:
	@echo "Cleaning byte code..."
	@find -name \*.py[co] -exec rm {} \;
	@echo "Done."

clean-doc:
	@echo "Cleaning doc..."
	@make -C docs clean
	@echo "Done."

clean-egg:
	@echo "Cleaning egg..."
	@rm -rf *.egg-info
	@echo "Done."

clean-build:
	@echo "Cleaning build..."
	@ rm -rf build
	@ rm -rf dist
	@echo "Done."
