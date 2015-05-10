#!/usr/bin/env python
# Author: Archer Reilly
# Date: 09/May/2015
# File: OddsDownloader.py
# Desc: download the html snippet from the www.oddsportal.com
#
# Produced By CSRGXTU
from Download import Download
from Utility import utfstr2file

class OddsDownloader(object):
    BASE_URL = 'http://fb.oddsportal.com/ajax-sport-country-tournament-archive/3/';
    BASE_URL_PART_3 = '/X0/1/0/'
    BASE_URL_PART_5 = '/?_=1431172180754'

    SeasonId = None
    PageNumber = None

    def __init__(self, seasonId, pageNumber):
        self.SeasonId = seasonId
        self.PageNumber = pageNumber

    def run():
        url = BASE_URL + SeasonId + BASE_URL_PART_3 + PageNumber + BASE_URL_PART_5
        return url

    def getSeasonId():
        return self.SeasonId

    def setSeasonId(seasonId):
        self.SeasonId = seasonId

    def getPageNumber():
        return self.PageNumber

    def setPageNumber(pageNumber):
        self.PageNumber = pageNumber
