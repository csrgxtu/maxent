#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 29/Oct/2014
# File: KNearestGames.py
# Desc: used for prepareing data for maxent model
#
# Produced By CSRGXTU
from Utility import readmatricefromfile
from Utility import appendlst2file

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

    self.teamLst = readmatricefromfile(self.teamFile)
    self.opponentTeamLst = readmatricefromfile(self.opponentTeamFile)

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
    # res.append(lsta[self.k - 1][0])
    res.extend(lsta[self.k - 1])
    for i in range(len(lsta) - 1):
      res.extend(lsta[i])

    res.extend(lstb[self.k - 1][1:])
    for i in range(len(lstb) - 1):
      res.extend(lstb[i])

    return res

  # prepareRecords
  # prepare records
  #
  # @return matrice 2 dim
  def prepareRecords(self):
    for i in range(len(self.teamLst) - self.k + 1):
      print "Prepare " + str(i) + "th record"
      lsta = self.teamLst[i:i+self.k]
      lstb = self.opponentTeamLst[i:i+self.k]
      appendlst2file(self.prepareRecord(lsta, lstb), self.outputFile)

if __name__ == '__main__':
  teamFile = '/home/archer/Documents/maxent/data/basketball/Knicksdata-28-Oct-2014-v1.0-modified.csv'
  opponentTeamFile = '/home/archer/Documents/maxent/data/basketball/Lackersdata-29-Oct-2014-v1.0-modified.csv'
  outputFile = '../../data/basketball/knearestgames.csv'
  k = KNearestGames(teamFile, opponentTeamFile, outputFile, 4)
  k.prepareRecords()