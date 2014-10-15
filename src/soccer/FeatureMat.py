#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 25/Jun/2014
# File: FeatureMat.py
# Des: build the numeric matrice of the feature and the label
# i.e. f1, f2, f3 ... fn, label
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
      FH.write("%d " % item)
    
    FH.write("\n")

# main
# main method glue everything up
#
def main():
  if len(sys.argv) != 4:
    print "Usage: python FeatureMat.py spamwordsfile wordsSrcDir FeatureMatrice"
    sys.exit(1)
  
  features =  readWordLst(sys.argv[1])
  
  files = getFileLst(sys.argv[2])
  for item in files:
    # email words
    words = readWordLst(item)
    featureVector = []
    
    for feature in features:
      if feature in words:
        featureVector.append(1)
      else:
        featureVector.append(0)
    
    appendVector2File(sys.argv[3], featureVector)

if __name__ == "__main__":
  main()
