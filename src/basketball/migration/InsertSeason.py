#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer
# File: InsertSeason.py
# Date: 05/Jun/2015
# Desc: insert data into the NBA.Season table
#
# Produced By CSRGXTU
import MySQLdb as mdb
import sys
from Utility import loadSeasons

seasons = loadSeasons('/home/archer/Documents/Python/maxent/data/basketball/seasons-18-Nov-2014.txt')
seasonTypeIDs = [1, 2, 3, 4]

con = mdb.connect('localhost', 'root', 'root', 'NBA')

with con:
    cur = con.cursor()
    for id in seasonTypeIDs:
        for s in seasons:
            sql = "insert into Season (\
                    Season_SeasonTypeID,\
                    Season,\
                    CreatedBy,\
                    CreatedTime) value (\
                    '%d', '%s', '%s', '%s')" %\
                    (id, s, 'archer', '2015-06-05 09:56:00')
            cur.execute(sql)
