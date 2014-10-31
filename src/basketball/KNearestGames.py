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

  def __init__(self, teamfile, opponentteamfile, outputfile):
    self.teamFile = teamfile
    self.opponentTeamFile = opponentteamfile
    self.outputFile = outputfile

    self.teamLst = readmatricefromfile(self.teamFile)
    self.opponentTeamLst = readmatricefromfile(self.opponentTeamFile)

  # prepareRecord
  # prepare record use 7 records in teamLst and opponentTeamLst
  #
  # @param lsta in length 7 in 2 dim
  # @param lstb in length 7 in 2 dim
  # @return lst or None
  def prepareRecord(self, lsta, lstb):
    if len(lsta) != 7 or len(lstb) != 7:
      return None

    res = []
    res.append(lsta[6][0])
    for i in range(len(lsta) - 1):
      res.extend(lsta[i])

    for i in range(len(lstb) - 1):
      res.extend(lstb[i])

    return res

  # prepareRecords
  # prepare records
  #
  # @return matrice 2 dim
  def prepareRecords(self):
    for i in range(len(self.teamLst) - 7 + 1):
      print "Prepare " + str(i) + "th record"
      lsta = self.teamLst[i:i+7]
      lstb = self.opponentTeamLst[i:i+7]
      appendlst2file(self.prepareRecord(lsta, lstb), self.outputFile)

if __name__ == '__main__':
  teamFile = '/home/archer/Documents/maxent/data/basketball/Knicksdata-28-Oct-2014-v1.0-modified.csv'
  opponentTeamFile = '/home/archer/Documents/maxent/data/basketball/Lackersdata-29-Oct-2014-v1.0-modified.csv'
  outputFile = '../../data/basketball/6nearestgames.csv'
  k = KNearestGames(teamFile, opponentTeamFile, outputFile)
  k.prepareRecords()  