#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 15/Oct/2014
# File: PlayerHelper.py
# Desc: helper class for players.py
#
# Produced By CSRGXTU
from Players import Players
from PlayerInfo import PlayerInfo
from numpy import sum

class PlayerHelper(object):
  TeamId = None
  Season = None
  SeasonType = None
  LeagueId = None
  PlayerIds = []
  CurrentSeasonStats = []
  
  # season 2013-14 seasonType Regular Season
  def __init__(self, teamId, season, seasonType, leagueId):
    self.TeamId = teamId
    self.Season = season
    self.SeasonType = seasonType.replace(" ", "+")
    self.LeagueId = leagueId
    
    p = Players(self.Season, self.SeasonType, self.TeamId, self.LeagueId)
    if p.doRequest():
      pass
    else:
      self.PlayerIds = p.getPlayerIds()
  
  def fillCurrentSeasonStats(self):
    for playerId in self.PlayerIds:
      p = PlayerInfo(playerId, self.SeasonType, self.LeagueId)
      if p.doRequest():
        pass
      else:
        self.CurrentSeasonStats.append(p.getCurrentSeasonStats())
    
    return self.CurrentSeasonStats
  
  def getCurrentSeasonStatsInTotals(self):
    return list(sum(self.CurrentSeasonStats, axis=0))
    
