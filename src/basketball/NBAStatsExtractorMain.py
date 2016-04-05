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

# leagueId = "00"
# teamId = "1610612752" # Knicks
# teamId = "1610612747" # Lackers
# opponentTeamId = "1610612747" # Lackers

# dataFile = "../../data/basketball/Lackersdata-29-Oct-2014-v1.0.csv"

# seasonspre = ['1990-91', '1991-92', '1992-93', '1993-94',
#   '1994-95', '1995-96']
# seasons = ['1996-97', '1997-98', '1998-99', '1999-00',
#   '2000-01', '2001-02', '2002-03', '2003-04', '2004-05',
#   '2005-06', '2006-07', '2007-08', '2008-09', '2009-10',
#   '2010-11', '2011-12', '2012-13', '2013-14']

# seasonTypes = ['Regular Season']

def run(teamId, season, seasonType, leagueId, dataFile):
  t = NBAStatsExtractor(teamId, season, seasonType, leagueId)
  # print t.getCurrentLeagueRankingInfo()
  # print t.getTeamProfileInfo()
  # print t.getTechStatsInfo()

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
  teamIds = loadTeamIds('../../data/basketball/teamidname-18-Nov-2014.csv')

  # second, load seasons
  seasons = loadSeasons('../../data/basketball/seasons.txt')

  # seasonTypes
  seasonTypes = ['Regular Season']

  # leagueId
  leagueId = "00"

  # for teamId in teamIds:
  #   dataFile = '../../data/basketball/' + teamId + '.csv'
  #   for t in seasonTypes:
  #     for s in seasons:
  #       print "Processing " + teamId + " " + s + " " + t,
  #       run(teamId, s, t, leagueId, dataFile)
  #       print "  Done"

  for teamId in ['1610612754']:
    dataFile = '../../data/basketball/' + teamId + '.csv'
    for t in seasonTypes:
      for s in ['2014-15']:
        print "Processing " + teamId + " " + s + " " + t,
        run(teamId, s, t, leagueId, dataFile)
        print " Done"

  """
  for t in seasonTypes:
    for s in (seasonspre + seasons):
      print "Processing " + s + " " + t,
      run(s, t, dataFile)
      print "  Done"
  """
  #run('2013-14', 'Regular Season', dataFile)
