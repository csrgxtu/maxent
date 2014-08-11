#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 11/Aug/2014
# File: PlayerInfoParserTest.py
# Description: test the PlayerInfoParser class
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
from PlayerInfoParser import PlayerInfoParser
from Download import Download

URL = "http://sports.qq.com/d/f_players/3/2890/"
player = Download(URL)
if player.doRequest() != 0:
  print "Download Cant Do Requst"
else:
  print "Successfully Do Request"

playerParser = PlayerInfoParser(player.getSOURCE())

