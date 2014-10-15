#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 12/Aug/2014
# File: PlayerTechStatisticsParser10League.py
# Description: parser for player statistics
# Website: http://csrgxtu.blog.com
#
# Produced By CSRGXTU
from Parser import Parser

class PlayerTechStatisticsParser10League(Parser):
  
  Length = 0

  def __init__(self, html):
    Parser.__init__(self, html)
    self.getPlayerNames()
    

  # getPlayerNames
  # get the name of the player
  #
  # @return rtvs (list(string)) or None
  def getPlayerNames(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[1]/a/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      self.setLength(len(rtvs))
      return rtvs

  # getPlayerLinks
  # get the links to the player detailed page
  #
  # @return rtvs (list(string)) or None
  def getPlayerLinks(self, exp):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[1]/a/@href'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getNumbers
  # get player numbers
  #
  # @return rtvs (list(string)) or None
  def getNumbers(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[2]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getRoles
  # get roles of the player
  #
  # @return rtvs (list(string)) or None
  def getRoles(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[3]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getStarts
  # get starts of the player
  #
  # @return rtvs (list(string)) or None
  def getStarts(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getPlayTime
  # get play time of the player
  #
  # @return rtvs (list(string)) or None
  def getPlayTime(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getGoals
  # get goals of the player
  #
  # @return rtvs (list(string)) or None
  def getGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getAssistances
  # get assistance numbers of the player
  #
  # @return rtvs (list(string)) or None
  def getAssistances(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getPasses
  # get pass numbers of the player
  #
  # @return rtvs (list(string)) or None
  def getPasses(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getPassEnemy
  # get pass enemy numbers of the player
  #
  # @return rtvs (list(string)) or None
  def getPassEnemy(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getSteals
  # get steal numbers of the player
  #
  # @return rtvs (list(string)) or None
  def getSteals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getOffsides
  # get number of offsides of the player
  #
  # @return rtvs (list(string)) or None
  def getOffsides(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[11]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getFouls
  # get number of fouls
  #
  # @return rtvs (list(string)) or None
  def getFouls(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[12]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getCards
  # get red and yellow cards
  #
  # @return rtvs (list(string)) or None
  def getCards(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[1]/table/tbody/tr/td[13]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getShoots
  # get number of shoots
  #
  # @return rtvs (list(string)) or None
  def getShoots(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getShootOnGoals
  # get number of shoot on goals
  #
  # @return rtvs (list(string)) or None
  def getShootOnGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getShootOnGoalRates
  # get the rate of the shoot on goals
  #
  # @return rtvs (list(string)) or None
  def getShootOnGoalRates(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getHeadGoals
  # get number of head goals
  #
  # @return rtvs (list(string)) or None
  def getHeadGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getLeftGoals
  # get number of left foot goals
  #
  # @return rtvs (list(string)) or None
  def getLeftGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getRightGoals
  # get number of right foot goals
  #
  # @return rtvs (list(string)) or None
  def getRightGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getDirectFreeGoals
  # get number of direct free goals
  #
  # @return rtvs (list(string)) or None
  def getDirectFreeGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getPenaltyKicks
  # get number of penalty kicks
  #
  # @return rtvs (list(string)) or None
  def getPenaltyKicks(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[11]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getPenaltyKickGoals
  # get number of penalty kick goals
  #
  # @return rtvs (list(string)) or None
  def getPenaltyKickGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[2]/table/tbody/tr/td[12]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getIntercepts
  # get number of intercepts
  #
  # @return rtvs (list(string)) or None
  def getIntercepts(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getRescues
  # get number of resuces
  #
  # @return rtvs (list(string)) or None
  def getRescues(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getHeadRescues
  # get number of head rescues
  #
  # @return rtvs (list(string)) or None
  def getHeadRescues(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getBackFieldRescues
  # get number of back field rescues
  #
  # @return rtvs (list(string)) or None
  def getBackFieldRescues(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getSuccessHeaders
  # get number of success headers
  #
  # @return rtvs (list(string)) or None
  def getSuccessHeaders(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getFailHeaders
  # get number of fail headers
  #
  # @return rtvs (list(string)) or None
  def getFailHeaders(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getOwnGoals
  # get number of own goals
  #
  # @return rtvs (list(string)) or None
  def getOwnGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_6"]/div[2]/div[3]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  def getLength(self):
    return self.Length

  def setLength(self, length):
    self.Length = length

