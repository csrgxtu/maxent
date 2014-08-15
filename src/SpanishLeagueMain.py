#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 14/Aug/2014
# File: SpanishLeagueMain.py
# Description: main script for SpanishLeague class
# Website: http://csrgxtu.blog.com
#
# Produced By CSRGXTU
from SpanishLeague import SpanishLeague

def readLinks(absPath):
  fh = open(absPath, 'r')
  rtvs = fh.readlines()
  return rtvs

def main():
  absPath = '../data/SpanishLeague.txt'
  links = readLinks(absPath)
  for link in links:
    print link
    obj = SpanishLeague(link)
    obj.teamInfo()


if __name__ == '__main__':
  main()
