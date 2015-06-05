#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer
# Date: 05/Jun/2015
# File: GetTeamInfo.py
# Desc: get the team short name and teamid, will be used in InsertTeamStats.py
#
# Produced By CSRGXTU
import MySQLdb as mdb
import sys
from Utility import saveMatrixToFile

con = mdb.connect('localhost', 'root', 'root', 'NBA')
basePath = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'

with con:
    cur = con.cursor()
    sql = "select TeamID, ShortNameEN from Team"
    cur.execute(sql)

    rows = cur.fetchall()
    res = []
    for row in rows:
        res.append([int(row[0]), row[1]])
    saveMatrixToFile(basePath + 'TeamID2TeamShortName.csv', res)
