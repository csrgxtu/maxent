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
