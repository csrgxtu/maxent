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

    def run(self):
        url = self.BASE_URL + self.SeasonId + self.BASE_URL_PART_3 + str(self.PageNumber) + self.BASE_URL_PART_5
        d = Download(url)
        if d.doRequest():
            # fail
            print 'ERROR: ' + self.SeasonId + '-' + str(self.PageNumber)
        else:
            utfstr2file(d.getSOURCE(), './data/' + self.SeasonId + '-' + str(self.PageNumber) + '.raw')

        return url

    def getSeasonId(self):
        return self.SeasonId

    def setSeasonId(self, seasonId):
        self.SeasonId = seasonId

    def getPageNumber(self):
        return self.PageNumber

    def setPageNumber(self, pageNumber):
        self.PageNumber = pageNumber
