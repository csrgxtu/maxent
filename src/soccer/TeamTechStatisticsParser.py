#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 11/Aug/2014
# File: TeamTechStatisticsParser.py
# Description: parse the page you give, only work for soccer data
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
from Parser import Parser

class TeamTechStatisticsParser(Parser):
  
  Length = 0
  
  def __init__(self, html):
    Parser.__init__(self, html)
    # init Length, or it will be messed up
    self.getDates()

  # getSeason
  # get the season of the game
  #
  # @return season (string) or None
  def getSeason(self):
    xpathExp = '//*[@id="table1"]/li[1]/a/text()'
    seasons = self.getTree().xpath(xpathExp)
    if len(seasons) != 1:
      return None
    else:
      return seasons[0][0:2]

  # getDates
  # get the dates of the game
  #
  # @return date (list(string)) or None
  def getDates(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[1]/text()'
    dates = self.getTree().xpath(xpathExp)
    self.Length = len(dates)
    if len(dates) == 0:
      return None
    else:
      return dates

  # getLeagues
  # get the league of the game
  #
  # @return leagues (list(string)) or None
  def getLeagues(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[2]/text()'
    leagues = self.getTree().xpath(xpathExp)
    if len(leagues) == 0 or len(leagues) != self.Length:
      return None
    else:
      return leagues

  # getGames
  # get the games of the season, a vs b
  #
  # @return games (list(string)) or None
  def getGames(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[3]/a/text()'
    games = self.getTree().xpath(xpathExp)
    if len(games) == 0 or len(games) != self.Length:
      return None
    else:
      return games

  # getResults
  # get the result of the game
  #
  # @return results (list(string)) or None
  def getResults(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[4]/text()'
    results = self.getTree().xpath(xpathExp)
    if len(results) == 0 or len(results) != self.Length:
      return None
    else:
      return results

  # getGoals
  # get the number of goal
  # 
  # @return goals (list(string)) or None
  def getGoals(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[5]/text()'
    goals = self.getTree().xpath(xpathExp)
    if len(goals) == 0 or len(goals) != self.Length:
      return None
    else:
      return goals

  # getFumbles
  # get the number of fummble
  #
  # @return fumbles (list(string)) or None
  def getFumbles(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[6]/text()'
    fumbles = self.getTree().xpath(xpathExp)
    if len(fumbles) == 0 or len(fumbles) != self.Length:
      return None
    else:
      return fumbles

  # getAssistances
  # get the number of assistance
  #
  # @return assistances (list(string)) or None
  def getAssistances(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[7]/text()'
    assistances = self.getTree().xpath(xpathExp)
    if len(assistances) == 0 or len(assistances) != self.Length:
      return None
    else:
      return assistances
    

  # getPass
  # get the number of pass balls
  #
  # @return pass (string) or None
  def getPasses(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[8]/text()'
    passes = self.getTree().xpath(xpathExp)
    if len(passes) == 0 or len(passes) != self.Length:
      return None
    else:
      return passes

  # getSteals
  # get the number of steal
  #
  # @return steals (list(tring)) or None
  def getSteals(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[9]/text()'
    steals = self.getTree().xpath(xpathExp)
    if len(steals) == 0 or len(steals) != self.Length:
      return None
    else:
      return steals
    

  # getOffsides
  # get the number of offside
  #
  # @return offsides (list(tring)) or None
  def getOffsides(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[10]/text()'
    offsides = self.getTree().xpath(xpathExp)
    if len(offsides) == 0 or len(offsides) != self.Length:
      return None
    else:
      return offsides
    

  # getFouls
  # get the number of Foul
  #
  # @return fouls (list(string)) or None
  def getFouls(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[11]/text()'
    fouls = self.getTree().xpath(xpathExp)
    if len(fouls) == 0 or len(fouls) != self.Length:
      return None
    else:
      return fouls
    

  # getRedCards
  # get the number of red card
  #
  # @return readCards (list(string)) or None
  def getRedCards(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[12]/text()'
    cards = self.getTree().xpath(xpathExp)
    if len(cards) == 0 or len(cards) != self.Length:
      return None
    else:
      return cards
    

  # getYellowCards
  # get the number of yellow card
  #
  # @return yellowCards (list(string)) or None
  def getYellowCards(self):
    xpathExp = '//div[@id="table22_con_0"]/table/tbody/tr/td[13]/text()'
    cards = self.getTree().xpath(xpathExp)
    if len(cards) == 0 or len(cards) != self.Length:
      return None
    else:
      return cards
    

  # getShoots
  # get the number of shoot
  #
  # @return shoots (list(string)) or None
  def getShoots(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[4]/text()'
    shoots = self.getTree().xpath(xpathExp)
    if len(shoots) == 0 or len(shoots) != self.Length:
      return None
    else:
      return shoots
    

  # getShootOnGoals
  # get the number of shoot on goal
  #
  # @return rtvs (list(string)) or None
  def getShootOnGoals(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs


  # getShootOnGoalRates
  # get the number of shoot on goal rate
  #
  # @return rtvs (list(string)) or None
  def getShootOnGoalRates(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getSuccessRates
  # get the number of success rate
  #
  # @return rtvs (list(string)) or None
  def getSuccessRates(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getHeadGoals
  # get the number of head goal
  #
  # @return rtvs list((string)) or None
  def getHeadGoals(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs
    

  # getDirectFreeGoals
  # get the number of direct free goal
  #
  # @return rtvs list((string)) or None
  def getDirectFreeGoals(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getPenaltyKickGoals
  # get the number of penalty kick goal
  #
  # @return rtvs list((string)) or None
  def getPenaltyKickGoals(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[11]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getPenaltyKicks
  # get the number of penalty kick
  #
  # @return rtvs (list(string)) or None
  def getPenaltyKicks(self):
    xpathExp = '//div[@id="table22_con_1"]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getIntercepts
  # get the number of intercept
  #
  # @return rtvs (list(string)) or None
  def getIntercepts(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs


  # getRescues
  # get the number of rescue
  #
  # @return rtvs (list(string)) or None
  def getRescues(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs


  # getHeadRescues
  # get the number of head rescue
  #
  # @return rtvs (list(string)) or None
  def getHeadRescues(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getBackFieldRescues
  # get the number of back field rescue
  #
  # @return rtvs (list(string)) or None
  def getBackFieldRescues(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getSuccessHeaders
  # get the number of success headers
  #
  # @return rtvs (list(string)) or None
  def getSuccessHeaders(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs
    

  # getFailHeaders
  # get the number of failed headers
  #
  # @return rtvs (list(string)) or None
  def getFailHeaders(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getOwnGoals
  # get the number of own goal
  #
  # @return rtvs (list(string)) or None
  def getOwnGoals(self):
    xpathExp = '//div[@id="table22_con_2"]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.Length:
      return None
    else:
      return rtvs

  # getLength
  # get the length property
  #
  # @return length
  def getLength(self):
    return self.Length

  # setLength
  # set the length property
  #
  # @parameter length (int)
  def setLength(self, length):
    self.Length = length
