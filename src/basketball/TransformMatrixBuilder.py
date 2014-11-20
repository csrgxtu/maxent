#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 20/Nov/2014
# File: TransformMatrixBuilder.py
# Desc: build transform matrix from dates
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile
from os import listdir

dates = loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/dates.csv')[0]
dirs = listdir('/home/archer/Documents/maxent/data/basketball/leaguerank/')
sortedFiles = []
for f in dirs:
  if f.endswith('.csv.sorted'):
    sortedFiles.append(f)

for d in dates:
  print 'INFO: build matrix for ' + d
  for f in sortedFiles:
    print '   INFO: load matrix from ' + f
    tmpMatrix = loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/' + f)
    tmpMatrixa = []
    for row in tmpMatrix:
      if row[1] == d:
        tmpMatrixa.append(row)
        break
      else:
        tmpMatrixa.append(row)

# generateRow
# generate a row from matrix for transform matrix
#
# @param matrix
# @return list
def generateRow(matrix):
  pass