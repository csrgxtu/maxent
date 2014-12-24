#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 24/DEC/2014
# File: GenerateDataForKNN.py
# Desc: generating input data for KNN classifier, since
#   different classifier use different kinds of input
#   data, so this one only guratte works for KNN
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile, saveMatrixToFile, readmatricefromfile
from Utility import loadSeasons, loadTeamIds

# generateTrainDataBySeason
# generate train data by season
#
# @param season
# @return res list(list)
def generateTrainDataBySeason(season):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [row[1] for row in loadMatrixFromFile(DIR + 'teamidshortname.csv')]
  leagueranks = loadMatrixFromFile(DIR + season + '.l')[0]
  res = []

  for team in teamIds:
    mat = loadMatrixFromFile(DIR + team + '.csv.sorted')
    for row in mat:
      if row[2] != season:
        continue

      if row[0] == 'W':
        WIN = 1
      else:
        WIN = 0
     
      if 'vs.' in row[5]:
        HOME = 1
      else:
        HOME = 0

      #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + team + '.' + season + '.player.csv.processed.total')[0]
      #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + team + '.' + season + '.player.csv.processed.avg')[0]
      heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + team + '.' + season + '.player.csv.processed.norm')[0]

      leaguerank = leagueranks[teamNames.index(row[5][0:3])]

      vsTeamId = teamIds[teamNames.index(row[5][-3:])]
      #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.total')[0]
      #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.avg')[0]
      vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.norm')[0]
      vsLeaguerank = leagueranks[teamIds.index(vsTeamId)]

      tmp = []
      tmp.append(HOME)
      tmp.append(heightTotal)
      tmp.append(weightTotal)
      tmp.append(ageTotal)
      tmp.append(expTotal)
      tmp.append(leaguerank)

      tmp.append(vsHeightTotal)
      tmp.append(vsWeightTotal)
      tmp.append(vsAgeTotal)
      tmp.append(vsExpTotal)
      tmp.append(vsLeaguerank)

      tmp.append(WIN)

      res.append(tmp)
  return res

# generateTestDataBySeason
# generate test data by season
#
# @param season
# @return res list(list)
def generateTestDataBySeason(season):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [row[1] for row in loadMatrixFromFile(DIR + 'teamidshortname.csv')]
  leagueranks = loadMatrixFromFile(DIR + season + '.l')[0]
  res = []

  mat = loadMatrixFromFile(DIR + season + '.playoff.csv')
  for row in mat:
    if row[0] == 'W':
      WIN = 1
    else:
      WIN = 0
   
    if 'vs.' in row[6]:
      HOME = 1
    else:
      HOME = 0

    teamId = teamIds[teamNames.index(row[6][0:3])]
    #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.total')[0]
    #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.avg')[0]
    heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.norm')[0]

    leaguerank = leagueranks[teamNames.index(row[6][0:3])]

    vsTeamId = teamIds[teamNames.index(row[6][-3:])]
    #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.total')[0]
    #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.avg')[0]
    vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.norm')[0]
    vsLeaguerank = leagueranks[teamIds.index(vsTeamId)]

    tmp = []
    tmp.append(HOME)
    tmp.append(heightTotal)
    tmp.append(weightTotal)
    tmp.append(ageTotal)
    tmp.append(expTotal)
    tmp.append(leaguerank)

    tmp.append(vsHeightTotal)
    tmp.append(vsWeightTotal)
    tmp.append(vsAgeTotal)
    tmp.append(vsExpTotal)
    tmp.append(vsLeaguerank)

    tmp.append(WIN)

    res.append(tmp)
  return res

# generateTrainDataBySeasons
# generate train data by seasons
#
# @return none
def generateTrainDataBySeasons():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')

  for season in seasons:
    res = generateTrainDataBySeason(season)
    outputFile = DIR + season + '-train.csv.knn'
    print 'INFO: ', outputFile
    saveMatrixToFile(outputFile, res)

# generateTestDataBySeasons
# generate test data by seasons
#
# @return none
def generateTestDataBySeasons():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')

  for season in seasons:
    res = generateTestDataBySeason(season)
    outputFile = DIR + season + '-test.csv.knn'
    print 'INFO: ', outputFile
    saveMatrixToFile(outputFile, res)

# generateTrainDataByTeam
# generate Train data by team
#
# @param teamId
# @return res list(list)
def generateTrainDataByTeam(teamId):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [row[1] for row in loadMatrixFromFile(DIR + 'teamidshortname.csv')]
  mat = loadMatrixFromFile(DIR + teamId + '.csv.sorted')
  res = []

  for row in mat:
    if row[0] == 'W':
      WIN = 1
    else:
      WIN = 0
   
    if 'vs.' in row[5]:
      HOME = 1
    else:
      HOME = 0

    season = row[2]
    #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.total')[0]
    #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.avg')[0]
    heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.norm')[0]
    
    leagueranks = loadMatrixFromFile(DIR + season + '.l')[0]
    leaguerank = leagueranks[teamNames.index(row[5][0:3])]

    vsTeamId = teamIds[teamNames.index(row[5][-3:])]
    #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.total')[0]
    #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.avg')[0]
    vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.norm')[0]
    vsLeaguerank = leagueranks[teamIds.index(vsTeamId)]

    tmp = []
    tmp.append(HOME)
    tmp.append(heightTotal)
    tmp.append(weightTotal)
    tmp.append(ageTotal)
    tmp.append(expTotal)
    tmp.append(leaguerank)

    tmp.append(vsHeightTotal)
    tmp.append(vsWeightTotal)
    tmp.append(vsAgeTotal)
    tmp.append(vsExpTotal)
    tmp.append(vsLeaguerank)

    tmp.append(WIN)
    res.append(tmp)
  return res

# generateTestDataByTeam
# generate Test data by team
#
# @param teamId
# @return res list(list)
def generateTestDataByTeam(teamId):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [row[1] for row in loadMatrixFromFile(DIR + 'teamidshortname.csv')]
  seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')
  res = []
  
  for season in seasons:
    mat = loadMatrixFromFile(DIR + season + '.playoff.csv')
    for row in mat:
      if teamNames[teamIds.index(teamId)] not in row[6]:
        continue

      if row[0] == 'W':
        WIN = 1
      else:
        WIN = 0
     
      if 'vs.' in row[6]:
        HOME = 1
      else:
        HOME = 0

      season = row[3]
      #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.total')[0]
      #heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.avg')[0]
      heightTotal, weightTotal, ageTotal, expTotal = loadMatrixFromFile(DIR + teamId + '.' + season + '.player.csv.processed.norm')[0]

      leagueranks = loadMatrixFromFile(DIR + season + '.l')[0]
      leaguerank = leagueranks[teamNames.index(row[6][0:3])]

      vsTeamId = teamIds[teamNames.index(row[6][-3:])]
      #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.total')[0]
      #vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.avg')[0]
      vsHeightTotal, vsWeightTotal, vsAgeTotal, vsExpTotal = loadMatrixFromFile(DIR + vsTeamId + '.' + season + '.player.csv.processed.norm')[0]
      vsLeaguerank = leagueranks[teamIds.index(vsTeamId)]

      tmp = []
      tmp.append(HOME)
      tmp.append(heightTotal)
      tmp.append(weightTotal)
      tmp.append(ageTotal)
      tmp.append(expTotal)
      tmp.append(leaguerank)

      tmp.append(vsHeightTotal)
      tmp.append(vsWeightTotal)
      tmp.append(vsAgeTotal)
      tmp.append(vsExpTotal)
      tmp.append(vsLeaguerank)

      tmp.append(WIN)
      
      res.append(tmp)
  return res

# generateTrainDataByTeams
# generate train data by teams
#
# @return none
def generateTrainDataByTeams():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [row[1] for row in loadMatrixFromFile(DIR + 'teamidshortname.csv')]

  for teamId in teamIds:
    res = generateTrainDataByTeam(teamId)
    outputFile = DIR + teamId + '-train.csv.knn'
    print 'INFO: ', outputFile
    saveMatrixToFile(outputFile, res)

# generateTestDataByTeams
# generate test data by teams
#
# @return none
def generateTestDataByTeams():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  teamNames = [row[1] for row in loadMatrixFromFile(DIR + 'teamidshortname.csv')]

  for teamId in teamIds:
    res = generateTestDataByTeam(teamId)
    outputFile = DIR + teamId + '-test.csv.knn'
    print 'INFO: ', outputFile
    saveMatrixToFile(outputFile, res)

# main
# glue function
def main():
  generateTrainDataBySeasons()
  generateTestDataBySeasons()
  generateTrainDataByTeams()
  generateTestDataByTeams()

if __name__ == '__main__':
  main()
