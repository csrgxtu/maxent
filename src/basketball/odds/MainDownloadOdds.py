#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 15/May/2015
# File: MainDownloadOdds.py
# Desc: download the raw data from web site
#
# Produced By CSRGXTU
from Utility import loadMatrixFromFile
from OddsDownloader import OddsDownloader

res = loadMatrixFromFile('./SeasonId')

for item in res:
    for index in range(1, int(item[2]) + 1):
        o = OddsDownloader(item[0], index)
        o.run()
