#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 25/DEC/2014
# File: NLTKMaxent.py
# Des: use nltk tookit train and test model
#
# Produced By CSRGXTU
import nltk
import sys
import numpy as np
import scipy
from datetime import datetime

from Utility import loadMatrixFromFile, loadSeasons, loadTeamIds
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

# train and test by team
def teamMain():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [x[1] for x in loadMatrixFromFile(DIR + 'teamidshortname.csv')]
  countTotal = 0
  total = 0

  for team in teamIds:
    train = buildTrainingSets(DIR + team + '-train.csv')
    test = buildTestingSets(DIR + team + '-test.csv')
    labels = buildTestingLabels(DIR + team + '-test.csv')
    total = total + len(labels)
    
    # train
    classifier = nltk.MaxentClassifier.train(train, 'IIS', trace=0, max_iter=1000)
    
    # test
    count = 0
    for i in range(len(labels)):
      pdist = classifier.prob_classify(test[i])
      if pdist.prob('L') >= pdist.prob('W'):
        flag = 'L'
      else:
        flag = 'W'
      
      #print 'DEBUG: ', flag, labels[i]
      if flag == labels[i]:
        count = count + 1
        
    print 'INFO: accuracy ', team, " ", float(count)/len(labels)

# train and test by season
def seasonMain():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')
  countTotal = 0
  total = 0

  for season in seasons:
    train = buildTrainingSets(DIR + season + '-train.csv')
    test = buildTestingSets(DIR + season + '-test.csv')
    labels = buildTestingLabels(DIR + season + '-test.csv')
    total = total + len(labels)

    # train
    classifier = nltk.MaxentClassifier.train(train, 'IIS', trace=0, max_iter=1000)
    
    # test
    count = 0
    for i in range(len(labels)):
      pdist = classifier.prob_classify(test[i])
      if pdist.prob('L') >= pdist.prob('W'):
        flag = 'L'
      else:
        flag = 'W'
      
      if flag == labels[i]:
        count = count + 1
        
    print 'INFO: accuracy ', season, " ", float(count)/len(labels)
    
if __name__ == "__main__":
  print "--------------teamMain----------------"
  teamMain()
  print "--------------seasonMain---------------"
  seasonMain()
