#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer
# File: InsertTeamStats.py
# Date: 05/Jun/2015
# Desc: insert NBA.TeamStats table
#
# Produced By CSRGXTU
import MySQLdb as mdb
import sys
from Utility import loadMatrixFromFile, loadSeasons, loadTeamIds

teamIds = loadTeamIds('/home/archer/Documents/Python/maxent/data/basketball/leaguerank/teamidshortname.csv')
seasons = loadSeasons('/home/archer/Documents/Python/maxent/data/basketball/leaguerank/seasons-18-Nov-2014.txt')

def insertPlayoff(teamIds):
    basePath = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'

    for team in teamIds:
        matrix = loadMatrixFromFile(basePath + team + '.playoff.csv')
        for row in matrix:
            

def insertRegular(teamIds, seasons):
    pass

# con = mdb.connect('localhost', 'root', 'root', 'NBA')
#
# with con:
#     cur = con.cursor()
#     for team in teamIds:
#         for season in seasons:
