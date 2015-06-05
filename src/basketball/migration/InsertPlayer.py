#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer
# Date: 05/Jun/2015
# File: InsertPlayer.py
# Desc: insert into NBA.Player table
#
# Produced By CSRGXTU
import MySQLdb as mdb
import sys
from Utility import loadSeasons, loadTeamIds, loadMatrixFromFile

basePath = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'

seasons = loadSeasons(basePath + 'seasons-18-Nov-2014.txt')
teamIds = loadTeamIds(basePath + 'teamidname-18-Nov-2014.csv')

def insertPlayer(cur):
    for team in teamIds:
        sql = "select TeamID from Team where StatsID = '%s'" % team
        cur.execute(sql)
        TeamID = cur.fetchone()[0]

        for season in seasons:
            sql = "select SeasonID from Season where Season = '%s' and Season_SeasonTypeID = 2" % season
            cur.execute(sql)
            SeasonID = cur.fetchone()[0]

            matrix = loadMatrixFromFile(basePath + team + '.' + season + '.player.csv')
            for row in matrix:
                sql = "insert into Player (\
                        Name,\
                        Position,\
                        Height,\
                        Weight,\
                        Age,\
                        Experience,\
                        CreatedBy,\
                        CreatedTime,\
                        Player_TeamID,\
                        Player_SeasonID) value (\
                        \"%s\", '%s', '%s', '%s', '%s', '%s', 'archer', '2015-06-05 16:44:00', %d, %d)" %\
                        (row[0], row[1], row[2], row[3], row[4], row[5], TeamID, SeasonID)
                print sql
                cur.execute(sql)

con = mdb.connect('localhost', 'root', 'root', 'NBA')

with con:
    cur = con.cursor()
    insertPlayer(cur)
