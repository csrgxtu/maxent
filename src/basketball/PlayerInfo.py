#!/usr/bin/env python
# coding = utf8
#
# Author: Archer Reilly
# Date: 15/Oct/2014
# File: PlayerInfo.py
# Desc: use the json web api in the stats.nba.com get the player info
#
# Produced By CSRGXTU
from Download import Download
from json import loads, dumps

"""
url = "http://stats.nba.com/stats/commonplayerinfo/\
?PlayerID=2405&SeasonType=Regular+Season&LeagueID=00"

d = Download(url)
d.doRequest()
print d.getSOURCE()
"""

class PlayerInfo(object):
  PlayerId = None
  SeasonType = None
  LeagueId = 0
  Url = "http://stats.nba.com/stats/commonplayerinfo/?"
  recs = None
  
  def __init__(self, playerId, seasonType, leagueId):
    self.PlayerId = playerId
    self.SeasonType = seasonType
    self.LeagueId = leagueId
    
  def doRequest(self):
    playerId = str(self.PlayerId)
    seasonType = self.SeasonType.replace(" ", "+")
    url = self.Url + "PlayerId=" + playerId + "&SeasonType=" + seasonType + "&League=" + self.LeagueId
    d = Download(url)
    
    if d.doRequest() == 1:
      return 1
    
    self.recs = dumps(loads(d.getSOURCE()))
    return 0
  
  def getCurrentSeasonStats(self):
    j = loads(self.recs)
    return j["resultSets"][1]["rowSet"][0][3:]
