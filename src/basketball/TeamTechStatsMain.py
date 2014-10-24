#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 24/Oct/2014
# File: TeamTechStatsMain.py
# Desc: main file that use TeamTechStatsExtractor
#
# Produced By CSRGXTU
from TeamTechStatsExtractor import TeamTechStatsExtractor
from Utility import appendlst2file

leagueId = "00"
teamId = "1610612752" # Knicks
opponentTeamId = "1610612747" # Lackers

dataFile = "../../data/basketball/Knicks-Lakers-data-24-Oct-2014.csv"

seasons = ['1996-97', '1997-98', '1999-00',
  '2000-01', '2001-02', '2002-03', '2003-04', '2004-05',
  '2005-06', '2006-07', '2007-08', '2008-09', '2009-10',
  '2010-11', '2011-12', '2012-13', '2013-14']

seasonTypes = ['Regular Season', 'Playoffs']

def run(season, seasonType, dataFile):
  t = TeamTechStatsExtractor(teamId, opponentTeamId, season, seasonType, leagueId)
  vst = TeamTechStatsExtractor(opponentTeamId, teamId, season, seasonType, leagueId)
  tRank = t.getCurrentLeagueRankingInfo()
  tTech = t.getTechStatsInfo()
  tProfile = t.getTeamProfileInfo()
  vstRank = vst.getCurrentLeagueRankingInfo()
  vstTech = vst.getTechStatsInfo()
  vstProfile = vst.getTeamProfileInfo()

  raw = []
  # label
  raw.append(tTech['Home']['Win'])

  raw.append(tRank['PPG'])
  raw.append(tRank['RPG'])
  raw.append(tRank['APG'])
  raw.append(tRank['OPPG'])

  raw.append(vstRank['PPG'])
  raw.append(vstRank['RPG'])
  raw.append(vstRank['APG'])
  raw.append(vstRank['OPPG'])

  raw.append(tProfile['Height'])
  raw.append(tProfile['Weight'])
  raw.append(tProfile['Age'])

  raw.append(vstProfile['Height'])
  raw.append(vstProfile['Weight'])
  raw.append(vstProfile['Age'])

  #raw.append(tTech['Home']['Location'])
  if tTech['Home']['Location'] == 'Home':
    raw.append(1)
  else:
    raw.append(0)

  raw.append(tTech['Home']['FGM'])
  raw.append(tTech['Home']['FGA'])
  raw.append(tTech['Home']['FG3M'])
  raw.append(tTech['Home']['FG3A'])
  raw.append(tTech['Home']['FTM'])
  raw.append(tTech['Home']['FTA'])
  raw.append(tTech['Home']['OREB'])
  raw.append(tTech['Home']['DREB'])
  raw.append(tTech['Home']['AST'])
  raw.append(tTech['Home']['TOV'])
  raw.append(tTech['Home']['STL'])
  raw.append(tTech['Home']['BLK'])
  raw.append(tTech['Home']['BLKA'])
  raw.append(tTech['Home']['PF'])
  raw.append(tTech['Home']['PTS'])
  raw.append(tTech['Home']['PLUS-MINUS'])

  #raw.append(vstTech['Road']['Location'])
  if vstTech['Road']['Location'] == 'Home':
    raw.append(1)
  else:
    raw.append(0)

  raw.append(vstTech['Road']['FGM'])
  raw.append(vstTech['Road']['FGA'])
  raw.append(vstTech['Road']['FG3M'])
  raw.append(vstTech['Road']['FG3A'])
  raw.append(vstTech['Road']['FTM'])
  raw.append(vstTech['Road']['FTA'])
  raw.append(vstTech['Road']['OREB'])
  raw.append(vstTech['Road']['DREB'])
  raw.append(vstTech['Road']['AST'])
  raw.append(vstTech['Road']['TOV'])
  raw.append(vstTech['Road']['STL'])
  raw.append(vstTech['Road']['BLK'])
  raw.append(vstTech['Road']['BLKA'])
  raw.append(vstTech['Road']['PF'])
  raw.append(vstTech['Road']['PTS'])
  raw.append(vstTech['Road']['PLUS-MINUS'])

  appendlst2file(raw, dataFile)

  raw = []
  # label
  raw.append(tTech['Road']['Win'])

  raw.append(tRank['PPG'])
  raw.append(tRank['RPG'])
  raw.append(tRank['APG'])
  raw.append(tRank['OPPG'])

  raw.append(vstRank['PPG'])
  raw.append(vstRank['RPG'])
  raw.append(vstRank['APG'])
  raw.append(vstRank['OPPG'])

  raw.append(tProfile['Height'])
  raw.append(tProfile['Weight'])
  raw.append(tProfile['Age'])

  raw.append(vstProfile['Height'])
  raw.append(vstProfile['Weight'])
  raw.append(vstProfile['Age'])

  #raw.append(tTech['Road']['Location'])
  if tTech['Road']['Location'] == 'Home':
    raw.append(1)
  else:
    raw.append(0)

  raw.append(tTech['Road']['FGM'])
  raw.append(tTech['Road']['FGA'])
  raw.append(tTech['Road']['FG3M'])
  raw.append(tTech['Road']['FG3A'])
  raw.append(tTech['Road']['FTM'])
  raw.append(tTech['Road']['FTA'])
  raw.append(tTech['Road']['OREB'])
  raw.append(tTech['Road']['DREB'])
  raw.append(tTech['Road']['AST'])
  raw.append(tTech['Road']['TOV'])
  raw.append(tTech['Road']['STL'])
  raw.append(tTech['Road']['BLK'])
  raw.append(tTech['Road']['BLKA'])
  raw.append(tTech['Road']['PF'])
  raw.append(tTech['Road']['PTS'])
  raw.append(tTech['Road']['PLUS-MINUS'])

  #raw.append(vstTech['Home']['Location'])
  if vstTech['Home']['Location'] == 'Home':
    raw.append(1)
  else:
    raw.append(0)

  raw.append(vstTech['Home']['FGM'])
  raw.append(vstTech['Home']['FGA'])
  raw.append(vstTech['Home']['FG3M'])
  raw.append(vstTech['Home']['FG3A'])
  raw.append(vstTech['Home']['FTM'])
  raw.append(vstTech['Home']['FTA'])
  raw.append(vstTech['Home']['OREB'])
  raw.append(vstTech['Home']['DREB'])
  raw.append(vstTech['Home']['AST'])
  raw.append(vstTech['Home']['TOV'])
  raw.append(vstTech['Home']['STL'])
  raw.append(vstTech['Home']['BLK'])
  raw.append(vstTech['Home']['BLKA'])
  raw.append(vstTech['Home']['PF'])
  raw.append(vstTech['Home']['PTS'])
  raw.append(vstTech['Home']['PLUS-MINUS'])

  appendlst2file(raw, dataFile)

if __name__ == '__main__':
  for t in seasonTypes:
    for s in seasons:
      print "Processing " + s + " " + t,
      run(s, t, dataFile)
      print "  Done"

  #run('2013-14', 'Regular Season', dataFile)