#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 17/DEC/2014
# File: NLTKNaiveBayes.py
# Desc: use naive bayes classify
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile
from nltk.classify import NaiveBayesClassifier

# buildTrainingSets
# build training sets from raw data file
#
# @param inputFile
# @return res list(tuple)
def buildTrainingSets(inputFile):
  res = []
  mat = loadMatrixFromFile(inputFile)
  for row in mat:
    if (float(row[1]) - float(row[2])) < 0:
      leaguerank = 0
    else:
      leaguerank = 1

    res.append((dict(HOME = row[0], LeagueRank = leaguerank), row[3]))

  return res

# buildTestingSets
# build testing sets from raw data file without labels
#
# @param inputFile
# @return res list(tuple)
def buildTestingSets(inputFile):
  res = []
  mat = loadMatrixFromFile(inputFile)
  for row in mat:
    if (float(row[1]) - float(row[2])) < 0:
      leaguerank = 0
    else:
      leaguerank = 1

    res.append((dict(HOME = row[0], LeagueRank = leaguerank)))

  return res

# buildTestingLabels
# build testing labels from raw data file
#
# @param inputFile
# @return res list
def buildTestingLabels(inputFile):
  res = []
  mat = loadMatrixFromFile(inputFile)
  for row in mat:
    res.append(row[3])

  return res

def main():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  train = buildTrainingSets(DIR + '2013-14-train.csv')
  test = buildTestingSets(DIR + '2013-14-test.csv')
  labels = buildTestingLabels(DIR + '2013-14-test.csv')

  classifier = NaiveBayesClassifier.train(train)
  res = classifier.batch_classify(test)

  # accuracy
  count = 0
  for i in range(len(res)):
    if labels[i] == res[i]:
      count = count + 1
  print 'INFO: Accuracy -- ', count/float(len(res))

if __name__ == '__main__':
  main()
