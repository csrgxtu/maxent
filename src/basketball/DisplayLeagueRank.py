#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 21/Nov/2014
# File: DisplayLeagueRank.py
# Desc: display league rank info
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile
import operator

DATA_PATH = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'

NAME_FILE = DATA_PATH + 'teamidname-18-Nov-2014.csv'

#RANK_FILE = DATA_PATH + 'MAR 31:2014.l'
#RANK_FILE = DATA_PATH + 'APR 16:2014.l'
RANK_FILE = DATA_PATH + '2013-14.l'
names = [ x[1] for x in loadMatrixFromFile(NAME_FILE)]
ranks = loadMatrixFromFile(RANK_FILE)[0]

res = {}
for i in range(len(names)):
  res[names[i]] = ranks[i]
  # print names[i] + '    ' + ranks[i]
  # print ranks[i] + '    ' + names[i]

sorted_res = sorted(res.items(), key=operator.itemgetter(1))
print 'INFO: All Teams'
print("%22s    %-15s" % ('Team', 'LeagueRank'))
for item in sorted_res:
  # print item[0], '    ', item[1]
  print("%22s    %-15s" % (item[0], item[1]))

eastern_res = {}
for i in range(15):
  eastern_res[names[i]] = ranks[i]
sorted_eastern_res = sorted(eastern_res.items(), key=operator.itemgetter(1))
print 'INFO: Eastern Teams'
print("%22s    %-15s" % ('Team', 'LeagueRank'))
for item in sorted_eastern_res:
  print("%22s    %-15s" % (item[0], item[1]))

weastern_res = {}
for i in range(15, 30):
  weastern_res[names[i]] = ranks[i]
sorted_weatern_res = sorted(weastern_res.items(), key=operator.itemgetter(1))
print 'INFO: Weastern Teams'
print("%22s    %-15s" % ('Team', 'LeagueRank'))
for item in sorted_weatern_res:
  print("%22s    %-15s" % (item[0], item[1]))
