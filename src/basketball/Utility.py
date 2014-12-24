#!/usr/bin/env python
# coding = utf8
# 
# Author: Archer Reilly
# File: Utility.py
# Date: 15/Oct/2014
# Desc: some useful utilities
#
# Produced By CSRGXTU
from numpy import loadtxt

# str2file
# save string to file
#
# @param string
# @param outFile
# @return nothing
def str2file(string, outFile):
  with open(outFile, "w") as myFile:
    myFile.write(string)

# appendstr2file
# append string to file
#
# @param string
# @param outFile
# @return nothing
def appendstr2file(string, outFile):
  with open(outFile, "a") as myFile:
    myFile.write(string + "\n")

# appendlst2file
# append a [] list to file
#
# @param lst
# @param outFile
# @return nothing
def appendlst2file(lst, outFile):
  with open(outFile, "a") as myFile:
    myFile.write(",".join(map(lambda x: str(x), lst)) + "\n")
    myFile.close()

# readmatricefromfile
# read matrice from file, i.e. 2 dim list
#
# @param inputFile
# @return lst 2 dim
def readmatricefromfile(inputFile):
	# res = []
	return loadtxt(open(inputFile, 'r'), delimiter=",").tolist()
	# with open(inputFile, "r") as myFile:
	# 	pass

# loadMatrixFromFile
# load string matrix from file
#
# @param inputFile
# @return lst 2 dim
def loadMatrixFromFile(inputFile):
  res = []
  with open(inputFile, 'r') as myFile:
    for line in myFile:
      res.append(line.rstrip().split(','))
  return res

# saveMatrixToFile
# save an string matrix to file
#
# @param outputFile
# @param matrix
# @return noe
def saveMatrixToFile(outputFile, matrix):
  with open(outputFile, 'w') as myFile:
    for row in matrix:
      myFile.write(','.join([str(x) for x in row]) + '\n')
    myFile.close()

# saveLstToFile
# save an list to file
#
# @param outputFile
# @param list
# @return noe
def saveLstToFile(outputFile, lst):
  with open(outputFile, 'w') as myFile:
    myFile.write(','.join([str(x) for x in lst]) + '\n')
  myFile.close()

# loadTeamIds
# load team ids from file
#
# @param inputFile
# @return teamIds in list
def loadTeamIds(inputFile):
  teamIds = []
  with open(inputFile, "r") as myFile:
    for line in myFile:
      teamIds.append(line.split(',')[0])

  return teamIds

# loadSeasons
# load seasons from file
#
# @param inputFile
# @return seasons in list
def loadSeasons(inputFile):
  seasons = []
  with open(inputFile, 'r') as myFile:
    for line in myFile:
      seasons.append(line.rstrip())

  return seasons

# generateRow
# generate a row from matrix for transform matrix
#
# @param matrix
# @param rowName
# @param sortedNames team names
# @return list
def generateRow(matrix, rowName, sortedNames):
  res = []
  loseNum = 0
  tmpWinMatrix = []
  for row in matrix:
    if row[0] == 'L':
      loseNum = loseNum + 1
      tmpWinMatrix.append(row)

  # get lose matrix
  tmpLoseMatrix = []
  for row in matrix:
    if row[0] == 'L':
      tmpLoseMatrix.append(row)

  if loseNum == 0:
    for team in sortedNames:
      res.append(0.0)
    return res

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

  return res
