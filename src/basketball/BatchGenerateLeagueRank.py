#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 21/Nov/2014
# File: BatchGenerateLeagueRank.py
# Desc: use LeagueRank batch generate the league rank for each .m
# file in the data dir
#
# Produced By CSRGXTU
from LeagueRank import LeagueRank
from Utility import loadMatrixFromFile, readmatricefromfile, appendlst2file

DATA_PATH = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
DATES_FILE = DATA_PATH + 'dates.csv'
L = [1/float(30) for e in range(1, 31)]

dates = loadMatrixFromFile(DATES_FILE)[0]

for d  in dates[3633:]:
  print 'INFO: generate LeagueRank for ' + d + '.m'
  #o = LeagueRank(L, readmatricefromfile(DATA_PATH + d + '.m'), 0.00000001, 100000)
  o = LeagueRank(L, readmatricefromfile(DATA_PATH + d + '.m'), 0.001, 10)
  # print 'Debug: ',
  # print o.rank()
  appendlst2file(o.rank(), DATA_PATH + d + '.l')
  print '    Done'
  # break
