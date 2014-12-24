#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 11/DEC/2014
# File: NBAStatsTeamPlayerExtractorMain.py
# Desc: main, extract the team's player tech stats for each season
#
# Produced By CSRGXTU
from NBAStatsTeamPlayerExtractorV1 import NBAStatsTeamPlayerExtractor
from Utility import loadSeasons, loadTeamIds, saveMatrixToFile

def main():
  DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  seasons = loadSeasons(DIR + 'seasons-18-Nov-2014.txt')
  teamIds = loadTeamIds(DIR + 'teamidshortname.csv')
  seasonTypes = ['Regular Season', 'Playoffs']
  # print seasons
  # return
  for team in teamIds:
    for season in seasons:
      #for seasonType in seasonTypes:
      seasonType = 'Regular Season'
      n = NBAStatsTeamPlayerExtractor(team, season, seasonType)
      outputFile = DIR + team + '.' + season + '.player.csv'
      print 'INFO: Processing ', outputFile
      mat = n.getStats()
      if mat == False:
        saveMatrixToFile(outputFile, [])
      else:
        saveMatrixToFile(outputFile, mat)


if __name__ == '__main__':
  main()
