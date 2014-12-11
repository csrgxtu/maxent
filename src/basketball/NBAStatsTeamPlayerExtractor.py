#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 11/DEC/2014
# File: NBAStatsTeamPlayerExtractor.py
# Desc: extract the team's player tech stats for each season
#
# Produced By CSRGXTU
from Download import Download
from json import loads

class NBAStatsTeamPlayerExtractor(object):
  teamId = False
  season = False
  seasonType = False

  API = 'http://stats.nba.com/stats/teamplayerdashboard?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&SeasonSegment=&VsConference=&VsDivision='

  # initialization the api url
  #
  # @param teamId int
  # @param season int (2013-14)
  # @param seasonType string (Regular Season, Playoffs)
  def __init__(self, teamId, season,seasonType):
    self.teamId = teamId
    self.season = season
    self.seasonType = seasonType.replace(" ", "+")

    self.API = self.API + '&TeamID=' + teamId
    self.API = self.API + '&Season=' + season
    self.API = self.API + '&SeasonType=' + self.seasonType
    #pass

  # getStats
  # get the tech stats for players
  #
  # @return res list(list) or False
  def getStats(self):
    d = Download(self.API)
    if d.doRequest():
      return False

    res = []
    j = loads(d.getSOURCE())
    for item in j['resultSets'][1]['rowSet']:
      res.append(item[1:])

    if len(res) == 0:
      return False
    else:
      return res
