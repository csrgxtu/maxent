#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 16/Oct/2014
# File: StatsView.py
# Desc: class for stats view
#
# Produced By CSRGXTU
from Download import Download
from json import loads

class StatsView(object):
  DateFrom = ""
  DateTo = ""
  GameScope = ""
  GameSegment = ""
  LastNGames = "0"
  # must
  LeagueId = "00"
  Location = ""
  MeasureType = "Base"
  Month = "0"
  # must
  OpponentTeamId = ""
  Outcome = ""
  PaceAdjust = "N"
  PerMode = "PerGame"
  Period = "0"
  PlusMinus = "N"
  Rank = "N"
  # must
  Season = None
  SeasonSegment = ""
  # must
  SeasonType = "Regular Season"
  # must
  TeamId = None
  VsConference = ""
  VsDivision = ""
  
  Url = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?"
  
  recs = None
  
  def __init__(self, leagueId, opponentTeamId, season, seasonType, teamId):
    self.LeagueId = leagueId
    self.OpponentTeamId = opponentTeamId
    self.Season = season
    self.SeasonType = seasonType.replace(" ", "+")
    self.TeamId = teamId
    
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
    self.Url += "&GameScope=" + self.GameScope
    
  def doRequest(self):
    d = Download(self.Url)
    if d.doRequest():
      return 1
    self.recs = d.getSOURCE()
    return 0
  
  # return [['home', 1], ['road', 0]]
  def getLabelVsLocation(self):
    j = loads(self.recs)
    recs = []
    for item in j["resultSets"][1]["rowSet"]:
      recs.append([str(item[1]), item[4]])
    return recs
    return j["resultSets"][1]["rowSet"]
