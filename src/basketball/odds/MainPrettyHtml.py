#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 17/May/2015
# File: MainPrettyHtml.py
# Desc: prettify the html in the data into a formated version
#
# Produced By CSRGXTU
from PrettyHtml import PrettyHtml
from Utility import str2file, readfromfile
import glob

for f in glob.glob('./data/*.html'):
  print 'INFO: Processing ', f
  html = readfromfile(f)
  p = PrettyHtml(html)
  pretty = p.pretty()
  str2file(pretty, f + '.pretty')
