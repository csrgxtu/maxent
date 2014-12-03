#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 24/Oct/2014
# File: NBAStatsMain.py
# Desc: main file that use NBAStatsExtractor
#
# Produced By CSRGXTU
from NBAStatsExtractor import NBAStatsExtractor
from Utility import appendlst2file, loadTeamIds, loadSeasons


def run(teamId, season, seasonType, leagueId, dataFile):
  t = NBAStatsExtractor(teamId, season, seasonType, leagueId)

  ranking = t.getCurrentLeagueRankingInfo()
  profile = t.getTeamProfileInfo()
  for item in t.getTechStatsInfo()['stats']:
    tmpLst = []
    tmpLst.append(item['WIN'])
    tmpLst.append(item['DATE'])

    tmpLst.append(season)
    tmpLst.append(seasonType)
    tmpLst.append(leagueId)

    tmpLst.append(item['MATCHUP'])
    tmpLst.append(item['FGM'])
    tmpLst.append(item['FGA'])
    tmpLst.append(item['FG3M'])
    tmpLst.append(item['FG3A'])
    tmpLst.append(item['FTM'])
    tmpLst.append(item['FTA'])
    tmpLst.append(item['OREB'])
    tmpLst.append(item['DREB'])
    tmpLst.append(item['AST'])
    tmpLst.append(item['STL'])
    tmpLst.append(item['BLK'])
    tmpLst.append(item['TOV'])
    tmpLst.append(item['PF'])
    tmpLst.append(item['PTS'])

    tmpLst.append(ranking['PPG'])
    tmpLst.append(ranking['RPG'])
    tmpLst.append(ranking['APG'])
    tmpLst.append(ranking['OPPG'])

    tmpLst.append(profile['Height'])
    tmpLst.append(profile['Weight'])
    tmpLst.append(profile['Age'])

    appendlst2file(tmpLst, dataFile)

if __name__ == '__main__':
  # first, load team id
  teamIds = loadTeamIds('../../data/basketball/leaguerank/teamidname-18-Nov-2014.csv')

  # second, load seasons
  seasons = loadSeasons('../../data/basketball/leaguerank/seasons-18-Nov-2014.txt')

  # seasonTypes
  seasonTypes = ['Playoffs']

  # leagueId
  leagueId = "00"

  """
  for teamId in teamIds:
    dataFile = '../../data/basketball/leaguerank/' + teamId + '.playoff.csv'
    for t in seasonTypes:
      for s in seasons:
        print "Processing " + teamId + " " + s + " " + t,
        run(teamId, s, t, leagueId, dataFile)
        print "  Done"
  """

  # download playoff logs for each season
  for s in seasons:
    dataFile = '../../data/basketball/leaguerank/' + s + '.playoff.csv'
    for t in seasonTypes:
      for teamId in teamIds:
        print 'INFO: Processing ' + s + ' ' + t + ' ' + teamId
        run(teamId, s, t, leagueId, dataFile)
        print 'INFO: Done'

