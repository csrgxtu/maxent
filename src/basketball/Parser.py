#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 05/Aug/2014
# File: Parser.py
# Description: parse the page you give, only work for soccer data
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
from lxml import html as htmlParser

class Parser(object):
  
  Html = None
  Tree = None

  def __init__(self, html):
    self.setHtml(html)
    self.setTree(htmlParser.fromstring(self.getHtml()))
  
  def getHtml(self):
    return self.Html

  def getTree(self):
    return self.Tree

  # @parameter html (string)
  def setHtml(self, html):
    self.Html = html

  # @parameter tree (lxml tree)
  def setTree(self, tree):
    self.Tree = tree

  def __str__(self):
    return "parse the page you give, only work for soccer data"
