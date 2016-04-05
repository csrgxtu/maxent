#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 17/DEC/2014
# File: NLTKNaiveBayes.py
# Desc: use naive bayes classify
#
# Produced By CSRGXTU
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
  DIR = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [x[1] for x in loadMatrixFromFile(DIR + 'teamidshortname.csv')]
  countTotal = 0
  total = 0

  for team in teamIds:
    train = buildTrainingSets(DIR + team + '-train.csv')
    test = buildTestingSets(DIR + team + '-test.csv')
    labels = buildTestingLabels(DIR + team + '-test.csv')
    total = total + len(labels)
    
    classifier = NaiveBayesClassifier.train(train)
    res = classifier.batch_classify(test)

    # accuracy
    count = 0
    for i in range(len(res)):
      if labels[i] == res[i]:
        count = count + 1

    countTotal = countTotal + count
    print 'INFO: Accuracy(', teamNames[teamIds.index(team)], ')', count/float(len(res))
  print 'INFO: Total Accuracy: ', countTotal/float(total)

# train and test by season
def main():
  DIR = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'
  seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')
  countTotal = 0
  total = 0

  for season in seasons:
    train = buildTrainingSets(DIR + season + '-train.csv')
    test = buildTestingSets(DIR + season + '-test.csv')
    labels = buildTestingLabels(DIR + season + '-test.csv')
    total = total + len(labels)

    classifier = NaiveBayesClassifier.train(train)
    res = classifier.batch_classify(test)

    # accuracy
    count = 0
    for i in range(len(res)):
      if labels[i] == res[i]:
        count = count + 1

    countTotal = countTotal + count
    print 'INFO: Accuracy(', season, ')', count/float(len(res))
  print 'INFO: Total Accuracy: ', countTotal/float(total)

if __name__ == '__main__':
  teamMain()
  print "DEBUG: ;f;dsjf"
  main()
