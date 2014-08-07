#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 05/Aug/2014
# File: Parser.py
# Description: test Parser class
# Website: http://csrgxtu.blog.com/
#
# Produced By CSRGXTU
import requests
from Parser import Parser

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
print page.text
parser = Parser(page.text)
#print parser.getBuyers()
