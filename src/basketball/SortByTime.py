#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 19/Nov/2014
# File: SortByTime.py
# Desc: sort the content in original data file by time
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile, saveMatrixToFile
from os import listdir
from datetime import datetime

"""
matrix = loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/1610612766.csv')
print matrix
"""

dirs = listdir('/home/archer/Documents/Python/maxent/data/basketball/')
for f in dirs:
  if f.startswith('161'):
    print 'Process file: ' + f
    matrix = loadMatrixFromFile('/home/archer/Documents/Python/maxent/data/basketball/' + f)
    matrixa = sorted(matrix, key=lambda x: datetime.strptime(x[1], '%b %d:%Y'))
    saveMatrixToFile('/home/archer/Documents/Python/maxent/data/basketball/' + f + '.sorted', matrixa)
