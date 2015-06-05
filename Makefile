# Copyright (C) 2015 Legrand France
# All rights reserved

# Simple makefile for pyzigbee development

test:
	@echo "Running tests..."
	PYTHONPATH=. nosetests -v

doc:
	@echo "Building documentation..."
	@cd docs && PYTHONPATH=.. make html && cd ..
	@echo "Open docs/_build/html/index.html with your favourite browser"docs/_build/html/index.html
	@echo
	@echo "sensible-browser docs/_build/html/index.html &"
	@echo

egg:
	@echo "Building egg..."
	PYTHONPATH=. python setup.py bdist_egg

clean: clean-bytecode clean-doc clean-egg clean-build

clean-bytecode:
	@echo "Cleaning byte code..."
	@find -name \*.py[co] -exec rm {} \;

clean-doc:
	@echo "Cleaning doc..."
	@make -C docs clean

clean-egg:
	@echo "Cleaning egg..."
	@rm -rf *.egg-info

clean-build:
	@echo "Cleaning build..."
	@ rm -rf build
	@ rm -rf dist
