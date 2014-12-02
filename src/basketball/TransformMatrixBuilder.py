#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 20/Nov/2014
# File: TransformMatrixBuilder.py
# Desc: build transform matrix from dates
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile, appendlst2file, saveMatrixToFile
from os import listdir


dates = loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/dates.csv')[0]
"""
dirs = listdir('/home/archer/Documents/maxent/data/basketball/leaguerank/')
sortedFiles = []
for f in dirs:
  if f.endswith('.csv.sorted'):
    sortedFiles.append(f)
"""
teamidabbrs = loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/teamidshortname.csv')
sortedFiles = []
sortedNames = []
for row in teamidabbrs:
  sortedFiles.append(row[0] + '.csv.sorted')
  sortedNames.append(row[1])

# generateRow
# generate a row from matrix for transform matrix
#
# @param matrix
# @param rowName
# @return list
def generateRow(matrix, rowName):
  res = []
  #winsNum = 0
  loseNum = 0
  tmpWinMatrix = []
  for row in matrix:
    if row[0] == 'L':
      #winsNum = winsNum + 1
      loseNum = loseNum + 1
      tmpWinMatrix.append(row)
  # print '   DEBUG:' + str(winsNum)

  # get lose matrix
  tmpLoseMatrix = []
  for row in matrix:
    if row[0] == 'L':
      tmpLoseMatrix.append(row)

  if loseNum == 0:
    for team in sortedNames:
      res.append(0.0)
    return res

  # print '   DEBUG sortedNames: ' + str(len(sortedNames))
  for team in sortedNames:
    counter = 0
    if team == rowName:
      res.append(0.0)
      continue
    else:
      for row in tmpLoseMatrix:
        if row[5].endswith(team):
          counter = counter + 1
      res.append(counter/float(loseNum))

  # print '     INFO: ',
  # print res
  return res

# tmpMatrixa = []
for d in dates[3633:]:
  print 'INFO: build matrix for ' + d
  tmpMatrixb = []
  for i in range(len(sortedFiles)):
    print '   INFO: load martix from ' + sortedFiles[i]
    tmpMatrix = loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/' + sortedFiles[i])
    tmpMatrixa = []
    """
    for row in tmpMatrix:
      if row[1] == d:
        tmpMatrixa.append(row)
        break
      else:
        tmpMatrixa.append(row)
    """
    for row in tmpMatrix:
      if row[1] == d:
        # print '   DEBUG: ',
        # print row
        appendlst2file(row, '/home/archer/Documents/maxent/data/basketball/leaguerank/' + sortedFiles[i] + '.swp')

    # print '   DEBUG generateRow:',
    tmpMatrixb.append(generateRow(loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/' + sortedFiles[i] + '.swp'), sortedNames[i]))
    # appendlst2file(tmpMatrixa, '/home/archer/Documents/maxent/data/basketball/leaguerank/' + sortedFiles[i] + '.swp')
    # tmpMatrixb.append(generateRow(loadMatrixFromFile('/home/archer/Documents/maxent/data/basketball/leaguerank/' + sortedFiles[i] + '.swp'), sortedNames[i]))
    # break
  # print 'INFO: matrix for ' + d + ':'
  # print tmpMatrixb
  # print 'INFO: save ' + d + '.m  Done'
  # print '\033[1;31mINFO: save %s.m  Done\t\t\033[1;m' % d
  print '\033[1;32mINFO: save %s.m  Done\t\tON\033[1;m' % d
  saveMatrixToFile('/home/archer/Documents/maxent/data/basketball/leaguerank/' + d + '.m', tmpMatrixb)
  # break


"""
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
"""


