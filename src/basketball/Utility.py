#!/usr/bin/env python
# coding = utf8
# 
# Author: Archer Reilly
# File: Utility.py
# Date: 15/Oct/2014
# Desc: some useful utilities
#
# Produced By CSRGXTU

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
