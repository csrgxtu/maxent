#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 05/Aug/2014
# File: PlayerInfoParser.py
# Description: parse the page you give, only work for soccer data
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
from Parser import Parser

class PlayerInfoParser(Parser):
  
  def __init__(self, html):
    Parser.__init__(self, html)

  # getName
  # get english name of the player
  #
  # @return name (string) or None
  #def getName(self):
  # getNameCN
  # get Chinese Name of the plaer
  #
  # @return name (string) or None
  #def getNameCN(self):
  # getNameAbbr
  # get english name abbreivation
  #
  # @return name (string) or None
  def getNameAbbr(self):
    xpathExp = '//*[@id="container"]/div/div[1]/div[1]/div[1]/h2/cite/text()'
    names = self.getTree().xpath(xpathExp)
    if len(names) != 1:
      return None
    else:
      return names[0]


  # getNameCNAbbr
  # get Chinese name abbreviation
  #
  # @return name (string) or None
  def getNameCNAbbr(self):
    xpathExp = '//*[@id="container"]/div/div[1]/div[1]/div[1]/h2/strong/text()'
    names = self.getTree().xpath(xpathExp)
    if len(names) != 1:
      return None
    else:
      return names[0]

  # getCountry
  # get the coutry the player belongs to
  #
  # @return country (string) or None
  def getCountry(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[1]/td[1]/text()'
    countries = self.getTree().xpath(xpathExp)
    if len(countries) != 1:
      return None
    else:
      return countries[0]

  # getWeight
  # get weight of the player
  #
  # @return weight (string) or None
  def getWeight(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[1]/td[2]/text()'
    weights = self.getTree().xpath(xpathExp)
    if len(weights) != 1:
      return None
    else:
      return weights[0][0:2]

  # getBirthday
  # get birthday of the player
  #
  # @return birthday (string) or None
  def getBirthday(self, exp):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[1]/td[3]/text()'
    birthdays = self.getTree().xpath(xpathExp)
    if len(birthdays) != 1:
      return None
    else:
      return birthdays[0]

  # getRole
  # get player's role in the team
  #
  # @return role (string) or None
  def getRole(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[2]/td[1]/text()'
    roles = self.getTree().xpath(xpathExp)
    if len(roles) != 1:
      return None
    else:
      return roles[0]

  # getHeight
  # get the height of the player
  #
  # @return height (string) or None
  def getHeight(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[2]/td[2]/text()'
    heights = self.getTree().xpath(xpathExp)
    if len(heights) != 1:
      return None
    else:
      return heights[0][0:3]

  # getTeam
  # get the team that player works for
  #
  # @return team (string) or None
  def getTeam(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[2]/td[3]/a/text()'
    teams = self.getTree().xpath(xpathExp)
    if len(teams) != 1:
      return None
    else:
      return teams[0]

  # getNumber
  # get the player number in the team
  #
  # @return number (string) or None
  def getNumber(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[3]/td[1]/text()'
    numbers = self.getTree().xpath(xpathExp)
    if len(numbers) != 1:
      return None
    else:
      return numbers[0]

  # getAge
  # get the age of the player
  #
  # @return age (string) or None
  def getAge(self):
    xpathExp = '//div[@class="intro-con player-con"]/table//tr[3]/td[2]/text()'
    ages = self.getTree().xpath(xpathExp)
    if len(ages) != 1:
      return None
    else:
      return ages[0]

  # getDescription
  # get the description of the player
  #
  # @return description (string) or None
  def getDescription(self):
    xpathExp = '//p[@class="intro-con-p"]/text()'
    descriptions = self.getTree().xpath(xpathExp)
    if len(descriptions) != 1:
      return None
    else:
      return descriptions[0]

  # getAwardData
  # get the award data of the player
  #
  # @return data (string) or None
  def getAwardData(self):
    xpathExp = '//*[@id="more_mess"]/text()'
    data = self.getTree().xpath(xpathExp)
    if len(data) != 1:
      return None
    else:
      return data[0]
