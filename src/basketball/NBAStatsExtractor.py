#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 28/Oct/2014
# File: NBAStatsExtractor.py
# Desc: this class responsible extract data from
# nbastats.com
#
# Produced By CSRGXTU
from Download import Download
from json import loads
from numpy import array

class NBAStatsExtractor(object):
  teamId = None
  season = None
  seasonType = None
  leagueId = None

  currentLeagueRankingApi = "http://stats.nba.com/stats/teaminfocommon?"
  techStatsApi = "http://stats.nba.com/stats/teamgamelog?"
  teamProfileApi = "http://stats.nba.com/stats/commonteamroster/?"

  def __init__(self, teamId, season, seasonType, leagueId):
    self.teamId = teamId
    self.season = season
    self.seasonType = seasonType.replace(" ", "+")
    self.leagueId = leagueId

    # specify the parameters for apis
    self.currentLeagueRankingApi += "LeagueId=" + self.leagueId
    self.currentLeagueRankingApi += "&Season=" + self.season
    self.currentLeagueRankingApi += "&SeasonType=" + self.seasonType
    self.currentLeagueRankingApi += "&TeamId=" + self.teamId

    self.techStatsApi += "LeagueID=" + self.leagueId
    self.techStatsApi += "&Season=" + self.season
    self.techStatsApi += "&SeasonType=" + self.seasonType
    self.techStatsApi += "&TeamID=" + self.teamId
    #self.techStatsApi += "&pageNo=1&rowsPerPage=1000"

    self.teamProfileApi += "LeagueId=" + self.leagueId
    self.teamProfileApi += "&Season=" + self.season
    self.teamProfileApi += "&TeamID=" + self.teamId


  # getCurrentLeagueRankingInfo
  # get current league ranking information of the teamid
  # season, seasonType, leagueid
  #
  # @param teamId #
  # @param season #
  # @param seasonType #
  # @param leagueId #
  # @return dict or None
  def getCurrentLeagueRankingInfo(self):
    res = {}
    ranking = self.doRequest(self.currentLeagueRankingApi)
    if ranking == None:
      return None
    else:
      try:
        j = loads(ranking)
        res['PPG'] = j["resultSets"][1]["rowSet"][0][3]
        res['RPG'] = j["resultSets"][1]["rowSet"][0][5]
        res['APG'] = j["resultSets"][1]["rowSet"][0][7]
        res['OPPG'] = j["resultSets"][1]["rowSet"][0][9]
        return res
      except IndexError:
        return None

  # getTechStatsInfo
  # get teach tech stats of the teamid, opponentTeamId, season
  # seasonType and leagueid
  #
  # @param teamId #
  # @param opponentTeamId #
  # @param season #
  # @param seasonType #
  # @param laegueId #
  # @return dict or None
  def getTechStatsInfo(self):
    res = {}
    res['stats'] = []
    techStats = self.doRequest(self.techStatsApi)
    if techStats == None:
      return None
    else:
      j = loads(techStats)
      for item in j['resultSets'][0]['rowSet']:
        tmpDict = {}
        tmpDict['DATE'] = item[2]
        tmpDict['MATCHUP'] = item[3]
        tmpDict['WIN'] = item[4]
        # if item[4] is 'W':
        #   tmpDict['WIN'] = 1
        # else:
        #   tmpDict['WIN'] = 0
        tmpDict['FGM'] = item[6]
        tmpDict['FGA'] = item[7]
        tmpDict['FG3M'] = item[9]
        tmpDict['FG3A'] = item[10]
        tmpDict['FTM'] = item[12]
        tmpDict['FTA'] = item[13]
        tmpDict['OREB'] = item[15]
        tmpDict['DREB'] = item[16]
        tmpDict['AST'] = item[18]
        tmpDict['STL'] = item[19]
        tmpDict['BLK'] = item[20]
        tmpDict['TOV'] = item[21]
        tmpDict['PF'] = item[22]
        tmpDict['PTS'] = item[23]

        res['stats'].append(tmpDict)

      return res

  # getTeamProfileInfo
  # get teams profile, mainly players height weight and age of the
  # teamid, season, leagueid
  #
  # @param teamId #
  # @param season #
  # @param leagueId #
  # @return dict or None
  def getTeamProfileInfo(self):
    res = {}
    profile = self.doRequest(self.teamProfileApi)
    if profile == None:
      return None
    else:
      j = loads(profile)
      matrix = array(j['resultSets'][0]['rowSet'])

      # turn '' and None to 0
      for k in range(len(matrix)):
        for l in range(len(matrix[0])):
          if matrix[k][l] == '':
            matrix[k][l] = 0
          if matrix[k][l] == 'None':
            matrix[k][l] = 0
          if matrix[k][l] == ' ':
            matrix[k][l] = 0
      try:
        res['Height'] = self.avg([self.convertHeight(str(x)) for x in matrix[:,6].tolist()])
      except IndexError:
        res['Height'] = 0
      
      # print 'Debug Here: '
      # print matrix[:, 9].tolist()
      try:
        res['Weight'] = self.avg([int(x) if x else 0 for x in matrix[:,7].tolist()])
      except IndexError:
        res['Weight'] = 0
      # res['Age'] = self.avg([int(float(x)) for x in matrix[:,9].tolist()])
      try:
        res['Age'] = self.avg([int(float(x)) if x != None else 0 for x in matrix[:, 9].tolist()])
      except IndexError:
        res['Age'] = 0
      return res

  """ Helper Method, should not invoke directly """
  # convertHeight
  # convert height from str to int
  #
  # @param string '6-4'
  # @return int
  def convertHeight(self, string):
    lst = string.split("-")
    """
    print 'Debug convertHeight: '
    print lst
    if len(lst) == 0:
      return 0
    if len(lst) == 1:
      lst.append(0)
    """

    if len(lst) == 0:
      return 0

    if len(lst) == 1:
      lst.append(0)

    for i in range(len(lst)):
      if lst[i] == 'None':
        lst[i] = 0

    return int(lst[0]) * 12 + int(lst[1])

  # avg
  # get avg of a list of numbers
  #
  # @param lst numbers
  # @return avg
  def avg(self, lst):
    return sum(lst) / len(lst)

  # doRequest
  # use Download module get the resource
  #
  # @param url
  # @return content in string format or None
  def doRequest(self, url):
    d = Download(url)
    if d.doRequest() == None:
      return None
    else:
      return d.getSOURCE()
