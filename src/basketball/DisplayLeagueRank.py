#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 21/Nov/2014
# File: DisplayLeagueRank.py
# Desc: display league rank info
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile

DATA_PATH = '/home/archer/Documents/maxent/data/basketball/leaguerank/'

NAME_FILE = DATA_PATH + 'teamidname-18-Nov-2014.csv'

RANK_FILE = DATA_PATH + 'MAR 31:2014.l'
names = [ x[1] for x in loadMatrixFromFile(NAME_FILE)]
ranks = loadMatrixFromFile(RANK_FILE)[0]

res = {}
for i in range(len(names)):
  res[names[i]] = ranks[i]
  # print names[i] + '    ' + ranks[i]
  print ranks[i] + '    ' + names[i]
