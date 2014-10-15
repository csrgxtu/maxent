#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 22/Jun/2014
# File: SubCont.py
# Des: this file is used to preprocessing the dataset --
# CSDMC2010 SPAM corpus, i.e. extract the subject and main
# content from the original email file. for an original
# email file like TRAIN_00000.eml, will extract its contents
# as plain text and save it to TRAIN_00000.sc, the postfix
# sc stands for subject and content.
#
# Produced By CSRGXTU
from __future__ import division
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import nltk, re, pprint
import glob

# file2Str
# read a text file into string with \n replaced by whitespace
#
# @param absPath abosolutely path to file
# @return fileStr string
def file2Str(absPath):
  # check the parameter here
  
  fh = open(absPath, 'r')
  fileStr = fh.read().replace('\n', ' ')
  fh.close()
  

  return fileStr

# file2lst
# read a text file into a list
#
# @param absPath abosolutely path to file
# @return lines
def file2lst(absPath):
  # check the parameter here
  
  lines = []
  with open(absPath, 'r') as f:
    for line in f:
      lines.append(line)
  
  return lines


# getSub
# get subject of the email from a list that store the email
#
# @param lines the lines store the email
# @return subject string or empty string
def getSub(lines):
  # check the parameter here
  
  for line in lines:
    matchObj = re.match(r'Subject: (.*)', line, re.M|re.I)
    if matchObj:
      subject = matchObj.group(1)
      return subject
  
  return ''

# getContent
# get the email content from a list that store the email
#
# @param lines the lines store the email
# @return content list or empty string
def getContent(lines):
  # check the parameter here
  
  content = []
  flag = False
  for line in lines:
    matchObj = re.match(r'------000000000000000000000', line, re.M|re.I)
    if matchObj:
      flag = True
      continue
    if flag:
      content.append(line)

  return ''.join(content)

# savelst2file
# save a list of words to a file
#
# @param list of words
# @param absPath path of the target file
def savelst2file(words, absPath):
  # check for the parameters
  
  with open(absPath, "w") as FH:
    for word in set(words):
      FH.write(word + "\n")

# getFileLst
# get file list from the directory you give
#
# @param dir directory you specify
# @return list of files
def getFileLst(directory):
  # check out the parameter
  
  directory = directory.rstrip('/')
  
  files = glob.glob(directory + "/*")
  files.sort()
  """
  for item in files:
    print item
  """
  
  return files

# main
# the main method glue everything up
#
def main():
  if len(sys.argv) != 2:
    print "Usage: python SubCont.py srcDir"
    sys.exit(1)
  
  fileLsts = getFileLst(sys.argv[1])
  print "Processing"
  for item in fileLsts:
    print ".",
    """
    lines = file2lst(item)
    subject = getSub(lines)
    content = getContent(lines)
    subCont = subject + content
    """
    subCont = file2Str(item)
    subCont = nltk.clean_html(subCont)
    subCont = re.sub(r'[^A-Za-z0-9]+', ' ', subCont)
    tokens = nltk.word_tokenize(subCont)
    porterStemmer = nltk.PorterStemmer()
    words = [porterStemmer.stem(t).lower() for t in tokens]
    wordsFile = item + ".words"
    savelst2file(words, wordsFile)

  print "Done"


"""      
absPath = "/home/archer/Desktop/thesis/data/CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TRAIN_00000.eml"
lines = file2lst(absPath)
subject = getSub(lines)
content = getContent(lines)
subCont = subject + content
subCont = nltk.clean_html(subCont)
tokens = nltk.word_tokenize(subCont)
porterStemmer = nltk.PorterStemmer()
words = [porterStemmer.stem(t) for t in tokens]
absPath = "/home/archer/Desktop/thesis/data/CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TRAIN_00000.eml.words"
savelst2file(words, absPath)
print words
"""
#getFileLst("/home/archer/Desktop/thesis/data/CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING")
if __name__ == "__main__":
  main()

#print "Subject: ", getSub(lines)
#print "Content: ", getContent(lines)
#print "Content: ", ''.join(BeautifulSoup(getContent(lines)).findAll(text=True))
