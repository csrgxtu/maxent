#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 15/Oct/2014
# File: Main.py
# Desc: main script that prepare the data
#
# Produced By CSRGXTU
from StatsView import StatsView
from TeamProfile import TeamProfile
from CurrentLeagueRanking import CurrentLeagueRanking
from PlayerHelper import PlayerHelper
from Utility import appendlst2file

"""
season = "2013-14"
seasonType = "Regular Season"
"""
leagueId = "00"
teamId = "1610612752"
opponentTeamId = "1610612747"

def run(season, seasonType, dataFile):
  # list that contains the original data
  #raw = []
  
  # get label and home/road
  s = StatsView(leagueId, opponentTeamId, season, seasonType, teamId)
  if s.doRequest():
    print "Cant get label and home/road"
  else:
    #print s.getLabelVsLocation()
    pass
  
  # get current league ranking
  c = CurrentLeagueRanking(season, seasonType, leagueId, teamId)
  if c.doRequest():
    print "Cant get current league ranking"
  else:
    #print c.getCurrentLeagueRanking()
    pass
  
  # get average age height weight
  t = TeamProfile(season, leagueId, teamId)
  if t.doRequest():
    print "Cant get AVGS of age height weight"
  else:
    #print t.getAVGs()
    pass
  
  # get player stats in total
  p = PlayerHelper(teamId, season, seasonType, leagueId)
  p.fillCurrentSeasonStats()
  #print p.getCurrentSeasonStatsInTotals()
  
  # fill the raw
  for item in s.getLabelVsLocation():
    raw = []
    raw.append(season)
    raw.append(item[1])
    raw.append("null")
    raw.append(c.getCurrentLeagueRanking()[0])
    raw.append(c.getCurrentLeagueRanking()[1])
    raw.append(c.getCurrentLeagueRanking()[2])
    raw.append(c.getCurrentLeagueRanking()[3])
    raw.append("null")
    raw.append(item[0])
    raw.append(t.getAVGs()[0])
    raw.append(t.getAVGs()[1])
    raw.append(t.getAVGs()[2])
    raw.append(p.getCurrentSeasonStatsInTotals()[0])
    raw.append(p.getCurrentSeasonStatsInTotals()[1])
    raw.append(p.getCurrentSeasonStatsInTotals()[2])
    raw.append(p.getCurrentSeasonStatsInTotals()[3])
    raw.append("null")
    raw.append("null")
    raw.append("null")
    appendlst2file(raw, dataFile)

def main():
  dataFile = "../../data/basketball/Knicks-Lakers-data.csv"
  
  seasons = ['1996-97', '1997-98', '1998-99', '1999-00',
    '2000-01', '2001-02', '2002-03', '2003-04', '2004-05',
    '2005-06', '2006-07', '2007-08', '2008-09', '2009-10',
    '2010-11', '2011-12', '2012-13', '2013-14']
  
  seasonTypes = ['Regular Season', 'Playoffs']
  
  for t in seasonTypes:
    for s in seasons:
      print "Processing " + s + " " + t,
      run(s, t, dataFile)
      print "  Done"

if __name__ == "__main__":
  main()
