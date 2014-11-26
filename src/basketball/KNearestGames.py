#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 29/Oct/2014
# File: KNearestGames.py
# Desc: used for prepareing data for maxent model
#
# Produced By CSRGXTU
from Utility import readmatricefromfile
from Utility import appendlst2file, loadMatrixFromFile

class KNearestGames(object):
  # the tech data of the team
  teamFile = None
  opponentTeamFile = None

  # output File
  outputFile = None

  # lst for teamFile
  teamLst = []
  opponentTeamLst = []

  # for k nearest games
  k = None

  def __init__(self, teamfile, opponentteamfile, outputfile, k):
    self.teamFile = teamfile
    self.opponentTeamFile = opponentteamfile
    self.outputFile = outputfile

    self.teamLst = loadMatrixFromFile(self.teamFile)
    self.opponentTeamLst = loadMatrixFromFile(self.opponentTeamFile)

    self.k = k

  # prepareRecord
  # prepare record use 7 records in teamLst and opponentTeamLst
  #
  # @param lsta in length 7 in 2 dim
  # @param lstb in length 7 in 2 dim
  # @return lst or None
  def prepareRecord(self, lsta, lstb):
    if len(lsta) != self.k or len(lstb) != self.k:
      return None

    res = []
    res.append(lsta[self.k - 1][0])
    #res.extend(lsta[self.k - 1])
    for i in range(len(lsta) - 1):
      # res.extend(lsta[i][1:])
      res.extend(lsta[i])

    # res.extend(lstb[self.k - 1][1:])
    for i in range(len(lstb) - 1):
      # res.extend(lstb[i][1:])
      res.extend(lstb[i])
    
    return res

  # prepareRecords
  # prepare records
  #
  # @param teamida
  # @param teamidb
  # @return matrice 2 dim
  def prepareRecords(self, teamida, teamidb):
    for i in range(len(self.teamLst) - self.k + 1):
      print "Prepare " + str(i) + "th record"
      lsta = self.teamLst[i:i+self.k]
      lstb = self.opponentTeamLst[i:i+self.k]
      lstaa = self.selectColumns(lsta, teamida)
      lstbb = self.selectColumns(lstb, teamidb)
      # print "Debug: "
      # print lstb
      appendlst2file(self.prepareRecord(lstaa, lstbb), self.outputFile)

  # selectColumns
  # select columns from matrix
  #
  # @param matrix 2d list
  # @param teamid
  # @return res 2d list
  def selectColumns(self, matrix, teamid):
    DATA_PATH = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
    TEAMID_FILE = DATA_PATH + 'teamidshortname.csv'
    TEAMIDS = [x[0] for x in loadMatrixFromFile(TEAMID_FILE)]
    res = []
    for i in range(len(matrix)):
      win = 1 if matrix[i][0] == 'W' else 0
      home = 1 if 'vs' in matrix[i][5] else 0
      points = matrix[i][19]
      lr = loadMatrixFromFile(DATA_PATH + matrix[i][1] + '.l')[0][TEAMIDS.index(teamid)]
      # res.append([win, points, lr])
      res.append([win, home, points, lr])
      # res.append([matrix[i][0], matrix[i][1], matrix[i][5], matrix[i][19]])
    return res

if __name__ == '__main__':
  DATA_PATH = '/home/archer/Documents/maxent/data/basketball/leaguerank/'
  teamFile = DATA_PATH + '1610612746-1610612747.csv.sorted'
  opponentTeamFile = DATA_PATH + '1610612747-1610612746.csv.sorted'
  outputFile = DATA_PATH + '7nearestgames-traning-testing-csv'
  k = KNearestGames(teamFile, opponentTeamFile, outputFile, 7)
  k.prepareRecords('1610612746', '1610612747')