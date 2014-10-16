#!/usr/bin/evn python
# coding = utf8
# Author: Archer Reilly
# Date: 16/Oct/2014
# File: TeamProfile.py
# Desc: class for Team Profile.
#
# Produced By CSRGXTU
from Download import Download
from json import loads
from numpy import sum

class TeamProfile(object):
  Season = None
  LeagueId = None
  TeamId = None
  
  Url = "http://stats.nba.com/stats/commonteamroster/?"
  
  recs = None
  
  # season 2013-14
  def __init__(self, season, leagueId, teamId):
    self.Season = season
    self.LeagueId = leagueId
    self.TeamId = teamId
    
    self.Url += "Season=" + self.Season + "&LeagueId="
    self.Url += self.LeagueId + "&TeamId=" + self.TeamId
    
  def doRequest(self):
    d = Download(self.Url)
    if d.doRequest():
      return 1
    self.recs = d.getSOURCE()
    return 0
  
  def getPlayerInfo(self):
    j = loads(self.recs)
    recs = []
    for item in j["resultSets"][0]["rowSet"]:
      height = int(item[6][0]) * 12
      height += height + int(item[6][2])
      weight = int(item[7])
      recs.append([height, weight, item[9]])
    return recs
  
  def getAVGs(self):
    return list(sum(self.getPlayerInfo(), axis=0))
