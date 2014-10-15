#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 26/Jun/2014
# File: DataMat.py
# Des: build the input matrice of the feature and the label
# i.e. label f1 f2 f3 ...
#
# Produced By CSRGXTU
import sys
import glob

# readWordLst
# read word list from file
#
# @param absPath path to the file to be read
# @return words list
def readWordLst(absPath):
  # check out the parameter
  
  words = []
  with open(absPath, "r") as FH:
    for line in FH:
      words.append(line.rstrip("\n"))
  
  return words

# getFileLst
# get file list from the directory you give
#
# @param dir directory you specify
# @return list of files
def getFileLst(directory):
  # check out the parameter
  
  directory = directory.rstrip('/')
  
  files = glob.glob(directory + "/*.words")
  files.sort()
  
  return files

# appendVector2File
# append the feature vector into a file
#
# @param absPath
# @param vector list
def appendVector2File(absPath, vector):
  # check the parameter
  
  with open(absPath, "a") as FH:
    for item in vector:
      FH.write("%s " % item)
    
    FH.write("\n")

# MatTest
# prepare Test data
#
def MatTest():
  if len(sys.argv) != 5:
    print "Usage: DataMat.py spamwordsfile wordsSrcDir FeatureMatrice Labels"
    sys.exit(1)
  
  features =  readWordLst(sys.argv[1])
  files = getFileLst(sys.argv[2])

# main
# main method glue everything up
#
def main():
  if len(sys.argv) != 5:
    print "Usage: DataMat.py spamwordsfile wordsSrcDir FeatureMatrice Labels"
    sys.exit(1)
  
  features =  readWordLst(sys.argv[1])
  labels = readWordLst(sys.argv[4])
  
  files = getFileLst(sys.argv[2])
  # process each words file
  for i in range(len(files)):
    featureVector = []
    featureVector.append(labels[i])
    
    words = readWordLst(files[i])
    for i in range(len(features)):
      if features[i] in words:
        featureVector.append(features[i])
    appendVector2File(sys.argv[3], featureVector)
  

if __name__ == "__main__":
  main()
