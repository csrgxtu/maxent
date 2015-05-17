#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 17/May/2015
# File: MainProcessRawData.py
# Desc: process the raw file and get the html snippet from it,
# and save the snippet into the file.
#
# Produced By CSRGXTU
from ProcessRawData import ProcessRawData
from Utility import readfromfile, utfstr2file
import glob

for f in glob.glob('./data/*.raw'):
  print 'INFO: Processing ', f
  raw = readfromfile(f)
  p = ProcessRawData(raw)
  utfstr2file(p.toJson(), f + '.html')

