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
TeamID2TeamShortNames = loadMatrixFromFile('/home/archer/Documents/Python/maxent/data/basketball/leaguerank/TeamID2TeamShortName.csv')

def findId(shortName):
    for row in TeamID2TeamShortNames:
        if row[1] == shortName:
            return row[0]
    return False

def isHome(matchUpString):
    if '@' in matchUpString:
        return 1
    else:
        return 0

def none20(lst):
    for i in range(len(lst)):
        if lst[i] == 'None':
            lst[i] = 0
    return lst

def insertPlayoff(teamIds, cur):
    basePath = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'

    for team in teamIds:
        matrix = loadMatrixFromFile(basePath + team + '.playoff.csv')
        for row in matrix:
            row = none20(row)

            teamID = findId(row[6][0:3])
            opponentTeamID = findId(row[6][-3:])
            home = isHome(row[6])

            sql = "select SeasonID from Season where Season = '%s' and Season_SeasonTypeID = 3" % row[3]
            cur.execute(sql)
            seasonID = cur.fetchone()[0]

            sql = "insert into TeamStats (\
                    TeamStats_TeamID,\
                    TeamStats_SeasonID,\
                    Result,\
                    Date,\
                    Home,\
                    Fgm,\
                    Fga,\
                    3pm,\
                    3pa,\
                    Ftm,\
                    Fta,\
                    Oreb,\
                    Dreb,\
                    Ast,\
                    Stl,\
                    Blk,\
                    Tov,\
                    Pf,\
                    CreatedBy,\
                    CreatedTime,\
                    Points,\
                    OpponentTeamID) value (\
                    %d,\
                    %d,\
                    '%c',\
                    '%s',\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    %d,\
                    'archer',\
                    '2015-06-05 15:02:22',\
                    %d,\
                    %d)" %\
                    (\
                        int(teamID),\
                        int(seasonID),\
                        row[0],\
                        row[1] + ' ' + row[2],\
                        int(home),\
                        int(row[7]),\
                        int(row[8]),\
                        int(row[9]),\
                        int(row[10]),\
                        int(row[11]),\
                        int(row[12]),\
                        int(row[13]),\
                        int(row[14]),\
                        int(row[15]),\
                        int(row[16]),\
                        int(row[17]),\
                        int(row[18]),\
                        int(row[19]),\
                        int(row[20]),\
                        int(opponentTeamID)
                    )

            # print sql
            cur.execute(sql)
            # print sql
            # print sql, seasonID
            # print row[6], row[6][0:3], row[6][-3:], teamID, opponentTeamID, home

def insertRegular(teamIds, seasons, cur):
    basePath = '/home/archer/Documents/Python/maxent/data/basketball/leaguerank/'
    for team in teamIds:
        for season in seasons:
            print 'INFO: ', team, season
            matrix = loadMatrixFromFile(basePath + team + '.' + season + '.csv.sorted.csv')
            for row in matrix:
                row = none20(row)

                teamID = findId(row[5][0:3])
                opponentTeamID = findId(row[5][-3:])
                home = isHome(row[5])

                sql = "select SeasonID from Season where Season = '%s' and Season_SeasonTypeID = 2" % row[2]
                cur.execute(sql)
                seasonID = cur.fetchone()[0]

                sql = "insert into TeamStats (\
                                    TeamStats_TeamID,\
                                    TeamStats_SeasonID,\
                                    Result,\
                                    Date,\
                                    Home,\
                                    Fgm,\
                                    Fga,\
                                    3pm,\
                                    3pa,\
                                    Ftm,\
                                    Fta,\
                                    Oreb,\
                                    Dreb,\
                                    Ast,\
                                    Stl,\
                                    Blk,\
                                    Tov,\
                                    Pf,\
                                    CreatedBy,\
                                    CreatedTime,\
                                    Points,\
                                    OpponentTeamID) value (\
                                    %d,\
                                    %d,\
                                    '%c',\
                                    '%s',\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    %d,\
                                    'archer',\
                                    '2015-06-05 15:52:22',\
                                    %d,\
                                    %d)" %\
                                    (\
                                        int(teamID),\
                                        int(seasonID),\
                                        row[0],\
                                        row[1],\
                                        int(home),\
                                        int(row[6]),\
                                        int(row[7]),\
                                        int(row[8]),\
                                        int(row[9]),\
                                        int(row[10]),\
                                        int(row[11]),\
                                        int(row[12]),\
                                        int(row[13]),\
                                        int(row[14]),\
                                        int(row[15]),\
                                        int(row[16]),\
                                        int(row[17]),\
                                        int(row[18]),\
                                        int(row[19]),\
                                        int(opponentTeamID)
                                    )
                cur.execute(sql)

con = mdb.connect('localhost', 'root', 'root', 'NBA')

with con:
    cur = con.cursor()
    # insertPlayoff(teamIds, cur)
    insertRegular(teamIds, seasons, cur)
