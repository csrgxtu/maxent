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
  
  # getCurrentSeasonStats
  # get current season stats, like ["6.6", "6.8", "0.5", "10.1%"]
  #
  # @return recs(list) or None
  def getCurrentSeasonStats(self):
    xpathExp = '//table[@class="season quickstats text-shadow"]/tbody/tr[3]/td/text()'
    print xpathExp
    recs = self.getTree().xpath(xpathExp)
    if len(recs) != 4:
      return None
    else:
      return recs
