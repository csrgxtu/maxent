#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# File: CurrentLeagueRanking.py
# Date: 16/Oct/2014
# Desc: class for current league ranking
#
# Produced By CSRGXTU
from Download import Download
from json import loads

class CurrentLeagueRanking(object):
  Season = None
  SeasonType = None
  LeagueId = None
  TeamId = None
  
  Url = "http://stats.nba.com/stats/teaminfocommon?"
  
  recs = None
  
  def __init__(self, season, seasonType, leagueId, teamId):
    self.Season = season
    self.SeasonType = seasonType.replace(" ", "+")
    self.LeagueId = leagueId
    self.TeamId = teamId
    
    self.Url += "Season=" + self.Season + "&SeasonType="
    self.Url += self.SeasonType + "&LeagueId=" + self.LeagueId
    self.Url += "&TeamId=" + self.TeamId
    
  def doRequest(self):
    d = Download(self.Url)
    if d.doRequest():
      return 1
    self.recs = d.getSOURCE()
    return 0
  
  def getCurrentLeagueRanking(self):
    j = loads(self.recs)
    recs = []
    for item in j["resultSets"][1]["rowSet"]:
      recs.append(item[3])
      recs.append(item[5])
      recs.append(item[7])
      recs.append(item[9])
    
    return recs
