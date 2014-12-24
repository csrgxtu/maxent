#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 24/DEC/2014
# File: NBAStatsTeamPlayerDataProcessor.py
# Desc: the data downloaded from net isnt good, so need this
#   file process it before used in models
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile, saveMatrixToFile, readmatricefromfile, loadSeasons, loadTeamIds, saveLstToFile

DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')
teamIds = loadTeamIds(DIR + 'teamidshortname.csv')

# noneWithAVG
# replace None with average value
#
# @param teamId
# @param season
# @return res list(list)
def noneWithAVG(teamId, season):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  mat = loadMatrixFromFile(DIR + teamId + "." + season + ".player.csv")
  if len(mat) == 0:
    return [[]]

  heights = []
  weights = []
  ages = []
  exps = []

  for row in mat:
    heights.append(row[2])
    weights.append(row[3])
    ages.append(row[4])
    exps.append(row[5])

  # for heights
  # change height from inch to inchs
  for i in range(len(heights)):
    if heights[i] == 'None':
      continue
    else:
      heights[i] = int(heights[i].split('-')[0]) * 12 + int(heights[i].split('-')[1])

  # get avgHeight
  tmpSum = 0
  heightCount = 0
  for i in range(len(heights)):
    if heights[i] == 'None':
      tmpSum = tmpSum + 0
    else:
      heightCount = heightCount + 1
      tmpSum = tmpSum + float(heights[i])
  
  avgHeight = tmpSum / float(heightCount)

  # replace None with avgHeight
  for i in range(len(heights)):
    if heights[i] == 'None':
      heights[i] = avgHeight

  # for weights
  tmpSum = 0
  weightCount = 0
  for i in range(len(weights)):
    if weights[i] == 'None':
      tmpSum = tmpSum + 0
    else:
      weightCount = weightCount + 1
      tmpSum =  tmpSum + float(weights[i])
  
  avgWeight = tmpSum / float(weightCount)

  for i in range(len(weights)):
    if weights[i] == 'None':
      weights[i] = avgWeight

  # for ages
  tmpSum = 0
  ageCount = 0
  for i in range(len(ages)):
    if ages[i] == 'None':
      tmpSum = tmpSum + 0
    else:
      ageCount = ageCount + 1
      tmpSum = tmpSum + float(ages[i])

  avgAge = tmpSum / float(ageCount)

  for i in range(len(ages)):
    if ages[i] == 'None':
      ages[i] = avgAge

  # make a mat
  res = []
  for i in range(len(ages)):
    tmp = []
    tmp.append(heights[i])
    tmp.append(weights[i])
    tmp.append(ages[i])
    tmp.append(exps[i])
    res.append(tmp)

  return res

# avg
# get avg of a mat in clumns
#
# @param teamId
# @param season
# @return res list
def avg(teamId, season):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  #mat = loadMatrixFromFile(DIR + teamId + "." + season + ".player.csv.processed")
  mat = readmatricefromfile(DIR + teamId + "." + season + ".player.csv.processed")
  if len(mat) == 0:
    return []

  heights = [row[0] for row in mat]
  weights = [row[1] for row in mat]
  ages = [row[2] for row in mat]
  exps = [row[3] for row in mat]

  res = []
  res.append(sum(heights)/float(len(heights)))
  res.append(sum(weights)/float(len(weights)))
  res.append(sum(ages)/float(len(ages)))
  res.append(sum(exps)/float(len(exps)))

  return res

# total
# get total of a mat in clumns
#
# @param teamId
# @param season
# @return res list
def total(teamId, season):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  #mat = loadMatrixFromFile(DIR + teamId + "." + season + ".player.csv.processed")
  mat = readmatricefromfile(DIR + teamId + "." + season + ".player.csv.processed")
  if len(mat) == 0:
    return []

  heights = [row[0] for row in mat]
  weights = [row[1] for row in mat]
  ages = [row[2] for row in mat]
  exps = [row[3] for row in mat]

  res = []
  res.append(sum(heights))
  res.append(sum(weights))
  res.append(sum(ages))
  res.append(sum(exps))
  return res

# normalize
# get normalize of a mat in clumns
#
# @param teamId
# @param season
# @return res list
def normalize(teamId, season):
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  #mat = loadMatrixFromFile(DIR + teamId + "." + season + ".player.csv.processed")
  mat = readmatricefromfile(DIR + teamId + "." + season + ".player.csv.processed")
  if len(mat) == 0:
    return []

  heights = [row[0] for row in mat]
  weights = [row[1] for row in mat]
  ages = [row[2] for row in mat]
  exps = [row[3] for row in mat]
  
  heightMax = max(heights)
  heightMin = min(heights)
  weightMax = max(weights)
  weightMin = min(weights)
  ageMax = max(ages)
  ageMin = min(ages)
  expMax = max(exps)
  expMin = min(exps)
  avgHeight = sum(heights) / float(len(heights))
  avgWeight = sum(weights) / float(len(weights))
  avgAge = sum(ages) / float(len(ages))
  avgExp = sum(exps) / float(len(exps))

  nHeight = (avgHeight - heightMin) / (heightMax - heightMin)
  nWeight = (avgWeight - weightMin) / (weightMax - weightMin)
  nAge = (avgAge - ageMin) / (ageMax - ageMin)
  nExp = (avgExp - expMin) / (expMax - expMin)

  res = []
  res.append(nHeight)
  res.append(nWeight)
  res.append(nAge)
  res.append(nExp)
  return res

def main():
  """
  for team in teamIds:
    for season in seasons:
      outputFile = DIR + team + "." + season + ".player.csv.processed"
      res = noneWithAVG(team, season)
      if len(res) == 0:
        continue
      print "INFO: ", outputFile
      saveMatrixToFile(outputFile, res)

  for team in teamIds:
    for season in seasons:
      outputFile = DIR + team + "." + season + ".player.csv.processed.avg"
      res = avg(team, season)
      if len(res) == 0:
        continue
      print "INFO: ", outputFile
      saveLstToFile(outputFile, res)

  for team in teamIds:
    for season in seasons:
      outputFile = DIR + team + "." + season + ".player.csv.processed.total"
      res = total(team, season)
      if len(res) == 0:
        continue
      print "INFO: ", outputFile
      saveLstToFile(outputFile, res)
  """

  for team in teamIds:
    for season in seasons:
      outputFile = DIR + team + "." + season + ".player.csv.processed.norm"
      res = normalize(team, season)
      if len(res) == 0:
        continue
      print 'INFO: ', outputFile
      saveLstToFile(outputFile, res)
if __name__ == '__main__':
  main()
