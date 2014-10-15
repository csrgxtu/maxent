#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 05/Aug/2014
# File: DownloadTest.py
# Description: test Download class
# Website: https://csrgxtu.blog.com
#
# Produced By CSRGXTU
from Download import Download

soccer = Download("http://sports.qq.com/d/f_teams/1/42/")
if soccer.doRequest() == 0:
  print "Successfully do request"
else:
  print "Failed do request"

html = soccer.getSOURCE()
html_unicode = unicode(html, soccer.getEncoding())
html_utf8 = html_unicode.encode("utf8")
print html_utf8
