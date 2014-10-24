#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# File: TeamTechStatsExtractor.py
# Desc: this class responsible extract team tech stats
#
# Produced By CSRGXTU
from Download import Download
from json import loads
from numpy import array

class TeamTechStatsExtractor(object):
  teamId = None
  opponentTeamId = None
  season = None
  seasonType = None
  leagueId = None

  currentLeagueRankingApi = "http://stats.nba.com/stats/teaminfocommon?"
  techStatsApi = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?"
  teamProfileApi = "http://stats.nba.com/stats/commonteamroster/?"

  def __init__(self, teamId, opponentTeamId, season, seasonType, leagueId):
    self.teamId = teamId
    self.opponentTeamId = opponentTeamId
    self.season = season
    self.seasonType = seasonType.replace(" ", "+")
    self.leagueId = leagueId

    # specify the parameters for apis
    self.currentLeagueRankingApi += "LeagueId=" + self.leagueId
    self.currentLeagueRankingApi += "&Season=" + self.season
    self.currentLeagueRankingApi += "&SeasonType=" + self.seasonType
    self.currentLeagueRankingApi += "&TeamId=" + self.teamId

    self.techStatsApi += "DateFrom="
    self.techStatsApi += "&DateTo="
    self.techStatsApi += "&GameScope="
    self.techStatsApi += "&GameSegment="
    self.techStatsApi += "&LastNGames=0"
    self.techStatsApi += "&LeagueID=" + self.leagueId
    self.techStatsApi += "&Location="
    self.techStatsApi += "&MeasureType=Base"
    self.techStatsApi += "&Month=0"
    self.techStatsApi += "&OpponentTeamID=" + self.opponentTeamId
    self.techStatsApi += "&Outcome="
    self.techStatsApi += "&PaceAdjust=N"
    self.techStatsApi += "&PerMode=PerGame"
    self.techStatsApi += "&Period=0"
    self.techStatsApi += "&PlusMinus=N"
    self.techStatsApi += "&Rank=N"
    self.techStatsApi += "&Season=" + self.season
    self.techStatsApi += "&SeasonSegment="
    self.techStatsApi += "&SeasonType=" + self.seasonType
    self.techStatsApi += "&TeamID=" + self.teamId
    self.techStatsApi += "&VsConference="
    self.techStatsApi += "&VsDivision="

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
      j = loads(ranking)
      res['PPG'] = j["resultSets"][1]["rowSet"][0][3]
      res['RPG'] = j["resultSets"][1]["rowSet"][0][5]
      res['APG'] = j["resultSets"][1]["rowSet"][0][7]
      res['OPPG'] = j["resultSets"][1]["rowSet"][0][9]
      return res

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
    res['Home'] = {}
    res['Road'] = {}
    techStats = self.doRequest(self.techStatsApi)
    if techStats == None:
      return None
    else:
      j = loads(techStats)
      res['Home']['Location'] = str(j["resultSets"][1]['rowSet'][0][2])
      res['Road']['Location'] = str(j["resultSets"][1]['rowSet'][1][2])
      res['Home']['Win'] = j["resultSets"][1]['rowSet'][0][4]
      res['Road']['Win'] = j["resultSets"][1]['rowSet'][1][4]
      res['Home']['FGM'] = j["resultSets"][1]['rowSet'][0][8]
      res['Road']['FGM'] = j["resultSets"][1]['rowSet'][1][8]
      res['Home']['FGA'] = j["resultSets"][1]['rowSet'][0][9]
      res['Road']['FGA'] = j["resultSets"][1]['rowSet'][1][9]
      res['Home']['FG3M'] = j["resultSets"][1]['rowSet'][0][11]
      res['Road']['FG3M'] = j["resultSets"][1]['rowSet'][1][11]
      res['Home']['FG3A'] = j["resultSets"][1]['rowSet'][0][12]
      res['Road']['FG3A'] = j["resultSets"][1]['rowSet'][1][12]
      res['Home']['FTM'] = j["resultSets"][1]['rowSet'][0][14]
      res['Road']['FTM'] = j["resultSets"][1]['rowSet'][1][14]
      res['Home']['FTA'] = j["resultSets"][1]['rowSet'][0][15]
      res['Road']['FTA'] = j["resultSets"][1]['rowSet'][1][15]
      res['Home']['OREB'] = j["resultSets"][1]['rowSet'][0][17]
      res['Road']['OREB'] = j["resultSets"][1]['rowSet'][1][17]
      res['Home']['DREB'] = j["resultSets"][1]['rowSet'][0][18]
      res['Road']['DREB'] = j["resultSets"][1]['rowSet'][1][18]
      res['Home']['AST'] = j["resultSets"][1]['rowSet'][0][20]
      res['Road']['AST'] = j["resultSets"][1]['rowSet'][1][20]
      res['Home']['TOV'] = j["resultSets"][1]['rowSet'][0][21]
      res['Road']['TOV'] = j["resultSets"][1]['rowSet'][1][21]
      res['Home']['STL'] = j["resultSets"][1]['rowSet'][0][22]
      res['Road']['STL'] = j["resultSets"][1]['rowSet'][1][22]
      res['Home']['BLK'] = j["resultSets"][1]['rowSet'][0][23]
      res['Road']['BLK'] = j["resultSets"][1]['rowSet'][1][23]
      res['Home']['BLKA'] = j["resultSets"][1]['rowSet'][0][24]
      res['Road']['BLKA'] = j["resultSets"][1]['rowSet'][1][24]
      res['Home']['PF'] = j["resultSets"][1]['rowSet'][0][25]
      res['Road']['PF'] = j["resultSets"][1]['rowSet'][1][25]
      res['Home']['PTS'] = j["resultSets"][1]['rowSet'][0][27]
      res['Road']['PTS'] = j["resultSets"][1]['rowSet'][1][27]
      res['Home']['PLUS-MINUS'] = j["resultSets"][1]['rowSet'][0][28]
      res['Road']['PLUS-MINUS'] = j["resultSets"][1]['rowSet'][1][28]

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
      res['Height'] = self.avg([self.convertHeight(str(x)) for x in matrix[:,6].tolist()])
      res['Weight'] = self.avg([int(x) for x in matrix[:,7].tolist()])
      res['Age'] = self.avg([int(x) for x in matrix[:,9].tolist()])
      return res

  """ Helper Method, should not invoke directly """
  # convertHeight
  # convert height from str to int
  #
  # @param string '6-4'
  # @return int
  def convertHeight(self, string):
    lst = string.split("-")
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