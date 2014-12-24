#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 24/DEC/2014
# File: NBAStatsTeamPlayerExtractor-V1.0.py
# Desc: extract the team's player tech stats for each season
#       use new API
#
# Produced By CSRGXTU
from Download import Download
from json import loads

class NBAStatsTeamPlayerExtractor(object):
  teamId = False
  season = False
  seasonType = False

  API = 'http://stats.nba.com/stats/commonteamroster?'

  # initialization the api url
  #
  # @param teamId int
  # @param season int (2013-14)
  # @param seasonType string (Regular Season, Playoffs)
  def __init__(self, teamId, season, seasonType):
    self.teamId = teamId
    self.season = season
    self.seasonType = seasonType.replace(" ", "+")

    self.API = self.API + 'LeagueID=00'
    self.API = self.API + '&Season=' + season
    self.API = self.API + '&TeamId=' + teamId

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
    for item in j['resultSets'][0]['rowSet']:
      tmp = []
      name = item[3]
      pos = item[5]
      if item[6] == 'null':
        height = 'None'
      else:
        height = item[6]
      if item[7] == " ":
        weight = 'None'
      else:
        weight = item[7]
      age = item[9]
      if item[10] == 'R' or item[10] == 'None' or item[10] == None:
        exp = 0
      else:
        exp = item[10]

      tmp.append(name)
      tmp.append(pos)
      tmp.append(height)
      tmp.append(weight)
      tmp.append(age)
      tmp.append(exp)
      res.append(tmp)

    if len(res) == 0:
      return False
    else:
      return res
