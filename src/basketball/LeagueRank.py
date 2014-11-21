#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 20/Nov/2014
# File: LeagueRank.py
# Desc: reimplementation of the PageRank algorithm, since what I
# found on Google all use a graph as input, hell, I dont have a
# gragh.
#
# Produced By CSRGXTU
from numpy import dot

class LeagueRank(object):
  # initial league rank value in list
  L = None
  # transform matrix
  H = None
  # tolerance
  T = None
  # iteration times
  I = None

  def __init__(self, l, h, t, i):
    self.L = l
    self.H = h
    self.T = t
    self.I = i

    # pre process the rank mtrix L
    tmpMatrix = []
    for row in self.H:
      if all(element == 0 for element in row):
        tmpMatrix.append([1/float(len(row)) for e in row])
      else:
        tmpMatrix.append(row)
    self.H = tmpMatrix

  # rank
  # do the actually league rank
  def rank(self):
    for i in range(self.I):
      l = dot(self.L, self.H).tolist()
      # print 'DEBUG: ',
      # print l
      if self.maxDistance(l, self.L) < self.T:
        # print 'DEBUG: Accuracy ok'
        return l
      else:
        self.L = l
    return self.L

  # maxDistance
  # calculate the maximum distance between two list
  # used for check the stop condition
  #
  # @param lst1
  # @param lst2
  # @return distance in float
  def maxDistance(self, lst1, lst2):
    if len(lst1) != len(lst2):
      raise NameError('lenth should be same between two list')

    dis = 0.0
    for i in range(len(lst1)):
      tmp = abs(lst1[i] - lst2[i])
      if tmp > dis:
        dis = tmp

    return dis