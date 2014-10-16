#!/usr/local/env python
# coding = utf8
# Author: Archer Reilly
# Date: 15/Oct/2014
# File: Players.py
# Desc: initially, i use this script get the user id, thus can be
# used by PlayerInfo.py
#
# Produced By CSRGXTU
from Download import Download
from json import loads, dump

class Players(object):
  Season = None
  SeasonType = "Regular Season"
  LeagueId = "00"
  TeamId = None
  MeasureType = "Base"
  PerMode = "PerGame"
  PlusMinus = "N"
  PaceAdjust = "N"
  Rank = "N"
  Outcome = ""
  Location = ""
  Month = "0"
  SeasonSegment = ""
  DateFrom = ""
  DateTo = ""
  OpponentTeamId = "0"
  VsConference = ""
  VsDivision = ""
  GameSegment = ""
  Period = "0"
  LastNGames = "0"
  
  
  Url = "http://stats.nba.com/stats/teamplayerdashboard?"
  
  recs = None
  
  # season 2013-14
  def __init__(self, season, seasonType, teamId, leagueId):
    self.Season = season
    self.SeasonType = seasonType
    self.TeamId = teamId
    self.LeagueId = leagueId
    
    self.Url += "Season=" + self.Season + "&SeasonType="
    self.Url += self.SeasonType + "&LeagueId=" + self.LeagueId
    self.Url += "&TeamId=" + self.TeamId + "&MeasureType="
    self.Url += self.MeasureType + "&PerMode=" + self.PerMode
    self.Url += "&PlusMinus=" + self.PlusMinus + "&PaceAdjust="
    self.Url += self.PaceAdjust + "&Rank=" + self.Rank
    self.Url += "&Outcome=" + self.Outcome + "&Location="
    self.Url += self.Location + "&Month=" + self.Month
    self.Url += "&SeasonSegment=" + self.SeasonSegment + "&DateFrom="
    self.Url += self.DateFrom + "&DateTo=" + self.DateTo
    self.Url += "&OpponentTeamId=" + self.OpponentTeamId + "&VsConference="
    self.Url += self.VsConference + "&VsDivision=" + self.VsDivision
    self.Url += "&GameSegment=" + self.GameSegment + "&Period="
    self.Url += self.Period + "&LastNGames=" + self.LastNGames
  
  def doRequest(self):
    d = Download(self.Url)
    if d.doRequest():
      return 1
    
    self.recs = d.getSOURCE()
    return 0
  
  def getPlayerIds(self):
    j = loads(self.recs)
    
    recs = []
    for item in j["resultSets"][1]["rowSet"]:
      recs.append(item[1])
    
    return recs
