#!/bin/bash

# When writing documentation, you may need a quick feedback loop to
# live check your changes. This script (based on Browsersync [1]) watches
# the html changes in your _build/html/ directory
# The dev worklflow is (with sublime text):
#      1- update you .rst files
#      2- ctrl+b to build html with sphinxdoc builder [2]
#      3- the browser is automatically reloaded
#      4- goto 1 ;)
# /!\ You may need to tune the reload-delay option
# [1] (http://www.browsersync.io/)
# [2] sublimeText shortcut (see sublime-text project file)

browser-sync start --server "docs/_build/html/" --files "docs/_build/html/*.*" --reload-delay 1000

