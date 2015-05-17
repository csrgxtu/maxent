#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 17/May/2015
# File: PrettyHtml.py
# Desc: turn the html into beautiful printed html with beautifulsoup
#
# Produced By CSRGXTU
from BeautifulSoup import BeautifulSoup as bs

class PrettyHtml(object):
  HTML = None

  def __init__(self, html):
    self.HTML = html

  def pretty(self):
    soup = bs(self.HTML)
    return soup.prettify()

  def getHTML(self):
    return self.HTML
