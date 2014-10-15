#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 15/Aug/2014
# File: LeagueMain.py
# Description: main script for five big League class
# Website: http://csrgxtu.blog.com
#
# Produced By CSRGXTU
from SpanishLeague import SpanishLeague
from ItalyLeague import ItalyLeague
from GermanLeague import GermanLeague
from FranceLeague import FranceLeague
from EnglandLeague import EnglandLeague

def readLinks(absPath):
  fh = open(absPath, 'r')
  rtvs = fh.readlines()
  return rtvs

def main():
  # first, spanish
  absPath = '../data/SpanishLeague.txt'
  links = readLinks(absPath)
  for link in links:
    print link
    obj = SpanishLeague(link.rstrip())
    obj.teamInfo()
    obj.teamTechStatistics13()
    obj.teamTechStatistics12()
    obj.teamTechStatistics11()
    obj.teamTechStatistics10()
    obj.teamTechStatistics()
    obj.playerTechStatistics13League()
    obj.playerTechStatistics12League()
    obj.playerTechStatistics11League()
    obj.playerTechStatistics10League()
    obj.playerTechStatistics13Champion()
    obj.playerTechStatistics12Champion()
    obj.playerTechStatistics11Champion()
    obj.playerTechStatistics10Champion()
    obj.goalKeeperStatistics13League()
    obj.goalKeeperStatistics12League()
    obj.goalKeeperStatistics11League()
    obj.goalKeeperStatistics10League()
    obj.goalKeeperStatistics13Champion()
    obj.goalKeeperStatistics12Champion()
    obj.goalKeeperStatistics11Champion()
    obj.goalKeeperStatistics10Champion()
  
  # second, Italy
  absPath = '../data/ItalyLeague.txt'
  links = readLinks(absPath)
  for link in links:
    print link
    obj = ItalyLeague(link.rstrip())
    obj.teamInfo()
    obj.teamTechStatistics13()
    obj.teamTechStatistics12()
    obj.teamTechStatistics11()
    obj.teamTechStatistics10()
    obj.teamTechStatistics()
    obj.playerTechStatistics13League()
    obj.playerTechStatistics12League()
    obj.playerTechStatistics11League()
    obj.playerTechStatistics10League()
    obj.playerTechStatistics13Champion()
    obj.playerTechStatistics12Champion()
    obj.playerTechStatistics11Champion()
    obj.playerTechStatistics10Champion()
    obj.goalKeeperStatistics13League()
    obj.goalKeeperStatistics12League()
    obj.goalKeeperStatistics11League()
    obj.goalKeeperStatistics10League()
    obj.goalKeeperStatistics13Champion()
    obj.goalKeeperStatistics12Champion()
    obj.goalKeeperStatistics11Champion()
    obj.goalKeeperStatistics10Champion()

  # third, German
  absPath = '../data/GermanLeague.txt'
  links = readLinks(absPath)
  for link in links:
    print link
    obj = GermanLeague(link.rstrip())
    obj.teamInfo()
    obj.teamTechStatistics13()
    obj.teamTechStatistics12()
    obj.teamTechStatistics11()
    obj.teamTechStatistics10()
    obj.teamTechStatistics()
    obj.playerTechStatistics13League()
    obj.playerTechStatistics12League()
    obj.playerTechStatistics11League()
    obj.playerTechStatistics10League()
    obj.playerTechStatistics13Champion()
    obj.playerTechStatistics12Champion()
    obj.playerTechStatistics11Champion()
    obj.playerTechStatistics10Champion()
    obj.goalKeeperStatistics13League()
    obj.goalKeeperStatistics12League()
    obj.goalKeeperStatistics11League()
    obj.goalKeeperStatistics10League()
    obj.goalKeeperStatistics13Champion()
    obj.goalKeeperStatistics12Champion()
    obj.goalKeeperStatistics11Champion()
    obj.goalKeeperStatistics10Champion()
  
  # fourth, France
  absPath = '../data/FranceLeague.txt'
  links = readLinks(absPath)
  for link in links:
    print link
    obj = FranceLeague(link.rstrip())
    obj.teamInfo()
    obj.teamTechStatistics13()
    obj.teamTechStatistics12()
    obj.teamTechStatistics11()
    obj.teamTechStatistics10()
    obj.teamTechStatistics()
    obj.playerTechStatistics13League()
    obj.playerTechStatistics12League()
    obj.playerTechStatistics11League()
    obj.playerTechStatistics10League()
    obj.playerTechStatistics13Champion()
    obj.playerTechStatistics12Champion()
    obj.playerTechStatistics11Champion()
    obj.playerTechStatistics10Champion()
    obj.goalKeeperStatistics13League()
    obj.goalKeeperStatistics12League()
    obj.goalKeeperStatistics11League()
    obj.goalKeeperStatistics10League()
    obj.goalKeeperStatistics13Champion()
    obj.goalKeeperStatistics12Champion()
    obj.goalKeeperStatistics11Champion()
    obj.goalKeeperStatistics10Champion()
  
  # finally, england
  absPath = '../data/EnglandLeague.txt'
  links = readLinks(absPath)
  for link in links:
    print link
    obj = EnglandLeague(link.rstrip())
    obj.teamInfo()
    obj.teamTechStatistics13()
    obj.teamTechStatistics12()
    obj.teamTechStatistics11()
    obj.teamTechStatistics10()
    obj.teamTechStatistics()
    obj.playerTechStatistics13League()
    obj.playerTechStatistics12League()
    obj.playerTechStatistics11League()
    obj.playerTechStatistics10League()
    obj.playerTechStatistics13Champion()
    obj.playerTechStatistics12Champion()
    obj.playerTechStatistics11Champion()
    obj.playerTechStatistics10Champion()
    obj.goalKeeperStatistics13League()
    obj.goalKeeperStatistics12League()
    obj.goalKeeperStatistics11League()
    obj.goalKeeperStatistics10League()
    obj.goalKeeperStatistics13Champion()
    obj.goalKeeperStatistics12Champion()
    obj.goalKeeperStatistics11Champion()
    obj.goalKeeperStatistics10Champion()

  print "Done"



if __name__ == '__main__':
  main()
