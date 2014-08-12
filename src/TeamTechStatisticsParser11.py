#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 12/Aug/2014
# File: TeamTechStatisticsParser11.py
# Description: parser for 11 season soccer data on QQ sports
# Website: http://csrgxtu.blog.com
#
# Produced By CSRGXTU
from Parser import Parser

class TeamTechStatisticsParser11(Parser):
  
  def __init__(self, html):
    Parser.__init__(self, html)

  # getLeagues
  # get leauges of the game
  #
  # @return leagues (list(string)) or None
  def getLeagues(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[1]/text()'
    leagues = self.getTree().xpath(xpathExp)
    if len(leagues) == 0:
      return None
    else:
      return leagues

  # getWins
  # get results of the games wins
  #
  # @return rtvs (list(string)) or None
  def getWins(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[2]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getFlats
  # get the number of flats of the game
  #
  # @return rtvs (list(string)) or None
  def getFlats(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[3]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getLoses
  # get the number of loses
  #
  # @return rtvs (list(string)) or None
  def getLoses(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getGoals
  # get number of goals
  #
  # @return rtvs (list(string)) or None
  def getGoals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getFumbles
  # get number of fumbles
  #
  # @return rtvs (list(string)) or None
  def getFumbles(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getAssistances
  # get number of assistances
  #
  # @return rtvs (list(string)) or None
  def getAssistances(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getPasses
  # get number of passes
  #
  # @return rtvs (list(string)) or None
  def getPasses(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getSteals
  # get number of steals
  #
  # @return rtvs (list(string)) or None
  def getSteals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getOffsides
  # get number os offsides
  #
  # @return rtvs (list(string)) or None
  def getOffsides(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getFouls
  # get number of fouls
  #
  # @return rtvs (list(string)) or None
  def getFouls(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[11]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getRedCards
  # get number of red cards
  #
  # @return rtvs (list(string)) or None
  def getRedCards(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[12]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getYellowCards
  # get number of yellow cards
  #
  # @return rtvs (list(string)) or None
  def getYellowCards(self): 
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[1]/table/tbody/tr/td[13]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getShoots
  # get number of shoots
  #
  # @return rtvs (list(string)) or None
  def getShoots(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[2]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getShootOnGoals
  # get number of shoot on goals
  #
  # @return rtvs (list(string)) or None
  def getShootOnGoals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[3]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getShootOnGoalRates
  # get number of rate of shoot on goal
  #
  # @return rtvs (list(string)) or None
  def getShootOnGoalRates(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getSuccessRates
  # get rates of success
  #
  # @return rtvs (list(string)) or None
  def getSuccessRates(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getHeadGoals
  # get number of head goals
  #
  # @return rtvs (list(string)) or None
  def getHeadGoals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getDirectFreeGoals
  # get number of direct free goals
  #
  # @return rtvs (list(string)) or None
  def getDirectFreeGoals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getPenaltyKicks
  # get number of penalty kicks
  #
  # @return rtvs (list(string)) or None
  def getPenaltyKicks(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getPenaltyKickGoals
  # get number of penalty kick goals
  #
  # @return rtvs (list(string)) or None
  def getPenaltyKickGoals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[2]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getIntercepts
  # get number of intercepts
  #
  # @return rtvs (list(string)) or None
  def getIntercepts(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[2]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getRescues
  # get number of rescues
  #
  # @return rtvs (list(string)) or None
  def getRescues(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[3]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getHeadRescues
  # get number of head rescues
  #
  # @return rtvs (list(string)) or None
  def getHeadRescues(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getBackFieldRescues
  # get number of back field rescues
  #
  # @return rtvs (list(string)) or None
  def getBackFieldRescues(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getSuccessHeaders
  # get number of success headers
  #
  # @return rtvs (list(string)) or None
  def getSuccessHeaders(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getFailHeaders
  # get number of fail headers
  #
  # @return rtvs (list(string)) or None
  def getFailHeaders(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs

  # getOwnGoals
  # get number of own goals
  #
  # @return rtvs (list(string)) or None
  def getOwnGoals(self):
    xpathExp = '//*[@id="table1_con_2" and @class="table"]/div[2]/div[3]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      return rtvs
