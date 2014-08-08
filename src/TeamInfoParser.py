#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 05/Aug/2014
# File: TeamInfoParser.py
# Description: parse the page you give, only work for soccer data
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
from Parser import Parser


class TeamInfoParser(Parser):

  def __init__(self, html):
    Parser.__init__(self, html)

  # getTeamName
  # get the english team name like Barcelona
  #
  # @return name (string) or None
  def getTeamName(self):
    xpathExp = '//*[@id="container"]/div/div[1]/div[1]/div[1]/h2/cite/text()'
    names = self.getTree().xpath(xpathExp)
    if len(names) != 1:
      return None
    else:
      return names[0].strip()
  
  # getTeamNameCN
  # get the Chinese team name like 巴塞罗那
  #
  # @return name (string) or None
  def getTeamNameCN(self):
    xpathExp = '//*[@id="container"]/div/div[1]/div[1]/div[1]/h2/strong/text()'
    names = self.getTree().xpath(xpathExp)
    if len(names) != 1:
      return None
    else:
      return names[0].strip()

  # getTeamLogo
  # get the team logo url
  #
  # @return logo (string) or None
  def getTeamLogo(self):
    xpathExp = 'string(//*[@id="container"]/div/div[1]/div[1]/div[1]/h2/img/@src)'
    logo = self.getTree().xpath(xpathExp)
    if logo == "":
      return None
    else:
      return logo.strip()

  # getTeamCity
  # get the city that team belongs
  #
  # @return city (string) or None
  def getTeamCity(self):
    xpathExp = '//td[@class="color-1044ba"]/following-sibling::td[1]/text()'
    citys = self.getTree().xpath(xpathExp)
    if len(citys) != 1:
      return None
    else:
      return citys[0].strip()

  # getTeamLeague
  # get the league that the team belongs
  #
  # @return league (string) or None
  def getTeamLeague(self):
    xpathExp = '//td[@class="color-1044ba"]/a/text()'
    leagues = self.getTree().xpath(xpathExp)
    if len(leagues) != 1:
      return None
    else:
      return leagues[0].strip()

  # getTeamFoundTime
  # get the found time of the team
  #
  # @return year (string) or None
  def getTeamFoundTime(self):
    xpathExp = '//td[@class="color-1044ba"]/../following-sibling::tr/td[1]/text()'
    years = self.getTree().xpath(xpathExp)
    if len(years) != 1:
      return None
    else:
      return years[0][0:4].strip()

  # getTeamHomeCourtCN
  # get home court of the team CN name
  #
  # @return court (string) or None
  def getTeamHomeCourtCN(self):
    xpathExp = '//td[@class="color-1044ba"]/../following-sibling::tr/td[2]/text()'
    courts = self.getTree().xpath(xpathExp)
    if len(courts) != 1:
      return None
    else:
      return courts[0].strip()

  # getTeamCurrentManagerCN
  # get current manager with cn name
  #
  # @return manager (string) or None
  def getTeamCurrentManagerCN(self):
    xpathExp = '//td[@class="color-1044ba"]/following-sibling::td[2]/text()'
    managers = self.getTree().xpath(xpathExp)
    if len(managers) != 1:
      return None
    else:
      return managers[0].strip()

  # getTeamDescription
  # get team description
  #
  # @return description (string) or None
  def getTeamDescription(self):
    xpathExp = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div/div[2]/p[2]/text()'
    descriptions = self.getTree().xpath(xpathExp)
    if len(descriptions) != 1:
      return None
    else:
      return descriptions[0].strip()

  # getTeamAwardData
  # get award data of the team
  #
  # @return data (string) or None
  def getTeamAwardData(self):
    xpathExp = '//*[@id="more_mess"]/text()'
    datas = self.getTree().xpath(xpathExp)
    if len(datas) != 1:
      return None
    else:
      return datas[0].strip()
  
  def getHtml(self):
    return self.Html

  def getTree(self):
    return self.Tree

  # @parameter html (string)
  def setHtml(self, html):
    self.Html = html

  # @parameter tree (lxml tree)
  def setTree(self, tree):
    self.Tree = tree

  def __str__(self):
    return "parse the page you give, only work for soccer data"
