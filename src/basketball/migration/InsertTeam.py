#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer
# Date: 05/Jun/2015
# File: InsertTeam.py
# Desc: insert the Team NBA.Team table
#
# Produced By CSRGXTU
import MySQLdb as mdb
import sys
from Utility import loadMatrixFromFile

id_names = loadMatrixFromFile('/home/archer/Documents/Python/maxent/data/basketball/leaguerank/teamidname-18-Nov-2014.csv')
id_shortnames = loadMatrixFromFile('/home/archer/Documents/Python/maxent/data/basketball/leaguerank/teamidshortname.csv')
matrix = []
for item in id_names:
    tmp = [item[0], item[1]]
    for item1 in id_shortnames:
        if item1[0] == item[0]:
            tmp.append(item1[1])
    matrix.append(tmp)

con = mdb.connect('localhost', 'root', 'root', 'NBA')

with con:
    cur = con.cursor()
    for item in matrix:
        sql = "insert into Team (\
                StatsID,\
                NameEN,\
                ShortNameEN,\
                CreatedBy,\
                CreatedTime) value (\
                '%s', '%s', '%s', '%s', '%s')" %\
                (item[0], item[1], item[2], 'archer', '2015-06-05 10:40:00')
        cur.execute(sql)
