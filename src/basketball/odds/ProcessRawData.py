#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 16/May/2015
# File: ProcessRawData.py
# Desc: Processing the .raw file in the data directory into
# json format and others
#
# Produced By CSRGXTU
import json

class ProcessRawData(object):
    RAW = None

    def __init__(self, raw):
        self.RAW = raw
        self.rmUnusefulChars()
        pass

    def rmUnusefulChars(self):
	self.RAW = self.RAW[85:len(self.RAW) - 2]

    def toJson(self):
        return json.loads(self.RAW)['d']['html']

    def toCsvMatrix(self):
        pass

    def getRAW(self):
        return self.RAW
