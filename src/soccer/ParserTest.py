#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 05/Aug/2014
# File: Parser.py
# Description: test Parser class
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
import requests
from Download import Download
from Parser import Parser
from TeamInfoParser import TeamInfoParser

"""
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
print page.text
parser = Parser(page.text)
#print parser.getBuyers()
"""
URL = "http://sports.qq.com/d/f_teams/1/42/"
soccer = Download(URL)
if soccer.doRequest() == 0:
  print "Successfully do request"
else:
  print "Failed do request"

html = soccer.getSOURCE()
parser = TeamInfoParser(html)
name = parser.getTeamName()
print "name:", unicode(name).encode('utf8')
name_cn = parser.getTeamNameCN()
print "name_cn:", unicode(name_cn).encode('utf8')
logo = parser.getTeamLogo()
print "logo:", logo
city = parser.getTeamCity()
print "city:", city
league = parser.getTeamLeague()
print "league:", league
found_time = parser.getTeamFoundTime()
print "found_time:", found_time
home_court_cn = parser.getTeamHomeCourtCN()
print "home_court_cn:", home_court_cn
current_manager_cn = parser.getTeamCurrentManagerCN()
print "current_manager_cn:", current_manager_cn
description = parser.getTeamDescription()
print "description:", description
award_data = parser.getTeamAwardData()
print "award_data:", award_data

