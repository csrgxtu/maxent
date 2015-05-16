#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 16/May/2015
# File: ProcessRawData.py
# Desc: Processing the .raw file in the data directory into
# json format and others
#
# Produced By CSRGXTU

class ProcessRawData(Object):
    RAW = None

    def __init__(self, raw):
        self.RAW = raw
        pass

    def rmUnusefulChars(self):
        pass

    def toJson(self):
        pass

    def toCsvMatrix(self):
        pass
