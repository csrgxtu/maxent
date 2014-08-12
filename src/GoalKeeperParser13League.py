#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 12/Aug/2014
# File: GoalKeeperParser13League.py
# Description: parser for goal keeper
# Website: http:csrgxtu.blog.com
#
# Produced By CSRGXTU
from Parser import Parser

class GoalKeeperParser13League(Parser):
  
  Length = 0

  def __init__(self, html):
    Parser.__init__(self, html)

  # getPlayers
  #
  # @return rtvs (list(string)) or None
  def getPlayers(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[1]/a/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0:
      return None
    else:
      self.setLength(len(rtvs))
      return rtvs

  # getNumbers
  #
  # @return rtvs (list(string)) or None
  def getNumbers(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[2]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getStarts
  #
  # @return rtvs (list(string)) or None
  def getStarts(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[3]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getPlayTime
  #
  # @return rtvs (list(string)) or None
  def getPlayTime(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[4]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getFumbles
  #
  # @return rtvs (list(string)) or None
  def getFumbles(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[5]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getTouchs
  #
  # @return rtvs (list(string)) or None
  def getTouchs(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[6]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getAttacks
  #
  # @return rtvs (list(string)) or None
  def getAttacks(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[7]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getSaves
  #
  # @return rtvs (list(string)) or None
  def getSaves(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[8]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getSavePenalties
  #
  # @return rtvs (list(string)) or None
  def getSavePenalties(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[9]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getMustInGoals
  #
  # @return rtvs (list(string)) or None
  def getMustInGoals(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[10]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getOneVSOnes
  #
  # @return rtvs (list(string)) or None
  def getOneVSOnes(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[11]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getFouls
  #
  # @return rtvs (list(string)) or None
  def getFouls(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[12]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  # getCards
  #
  # @return rtvs (list(string)) or None
  def getCards(self):
    xpathExp = '//div[@class="table" and @id="table3_con_0"]/div[4]/table/tbody/tr/td[13]/text()'
    rtvs = self.getTree().xpath(xpathExp)
    if len(rtvs) == 0 or len(rtvs) != self.getLength():
      return None
    else:
      return rtvs

  def getLength(self):
    return self.Length

  def setLength(self, length):
    self.Length = length
