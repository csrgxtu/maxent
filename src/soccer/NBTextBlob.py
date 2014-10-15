#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 28/Jun/2014
# File: NBTextBlob.py
# Des: use TextBlob naive bayes tookit train and test model
#
# Produced By CSRGXTU
import nltk
import sys
import numpy as np
import scipy
from datetime import datetime
from text.classifiers import NaiveBayesClassifier


# loadTxt2Lst
# load the text in file -- one word perline into a list
#
# @param absPath
# @return words list
def loadTxt2Lst(absPath):
  # check out the param
  
  words = []
  with open(absPath, 'r') as FH:
    for line in FH:
      words.append(line.rstrip("\n"))
  
  return words

# loadFeatureMat
# load the feature matrice from file into a array list
#
# @param absPath
# @return mat list(2d)
def loadFeatureMat(absPath):
  # check out the param
  
  return np.loadtxt(absPath, delimiter=',').tolist()

# prepareData
# prepare the data format that can be used by nltk maxent
#
# @param spamwords list
# @param labels list
# @param features list(2d)
# @return list(tupple(dict(f), label))
def prepareData(spamwords, labels, features):
  # check out the params
  
  if len(labels) != len(features):
    print "Fatal Error: labels and features should have same length"
    sys.exit(1)
  
  results = []
  for i in range(len(labels)):
    # build the dic for each feature
    if len(spamwords) != len(features[i]):
      print "Fatal Error: spamwords should be same length with each feature"
      sys.exit(1)
    
    featureDic = {}
    for j in range(len(spamwords)):
      featureDic[spamwords[j]] = int(features[i][j])
    
    # append to results
    results.append((featureDic, int(labels[i])))
  
  return results

# nb
# train and test method of naive bayes
#
# @param algorithm iterator algorithms
# @param data
# @return accuracy
def nb(data):
  # check out params
  
  # divide data into 4 = 3 + 1, 3 for train, 1 for test
  train = data[0: (len(data) / 4) * 3]
  test = data[(len(data) / 4) * 3:]
  
  print "Training ..."
  classifier = NaiveBayesClassifier(train)
  print "Testing ..."
  print "Accuracy: ", classifier.accuracy(test)
  
  """
  try:
    print "Training ..."
    spamClassifier = nltk.MaxentClassifier.train(train, algorithm, trace=0, max_iter=1000)
  except Exception, e:
    spamClassifier = e
    print "Fatal Error: Exceptions: ", e
    sys.exit(1)
  
  print "Testing ..."
  # build new test data, removeing the label
  test_new = []
  for item in test:
    test_new.append(item[0])
  
  # calculate accuracy
  counter = 0
  for k in range(len(test_new)):
    pdist = spamClassifier.prob_classify(test_new[k])
    if pdist.prob('0') >= pdist.prob('1'):
      label = 0
    else:
      label = 1
    
    if label == test[k][1]:
      counter = counter + 1
    
  print "Accuracy: ", float(counter)/len(test), " (", counter, "/", len(test), ")"
  """

# main
# gloue method
def main():
  if len(sys.argv) != 4:
    print "Usage: NBNLTK.py spamwords labels featuresmat"
    sys.exit(1)
  
  spamwords = loadTxt2Lst(sys.argv[1])
  porterStemmer = nltk.PorterStemmer()
  spamwords_new = [porterStemmer.stem(t).lower() for t in spamwords]
  labels = loadTxt2Lst(sys.argv[2])
  features = loadFeatureMat(sys.argv[3])
  data = prepareData(spamwords_new, labels, features)
  nb(data)


if __name__ == "__main__":
  main()
