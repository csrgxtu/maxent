#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 13/Aug/2014
# File: CheckService.py
# Description: check if a service is up and running
# Website: http://csrgxtu.blog.com
#
# Produced By CSRGXTU
import os
import re

# CheckService
# check if a service is open
#
# @parameter name(string)
# @return rtvs (list) or None
def CheckService(name):
  cmd = 'sudo netstat -nlpt | grep -i ' + name
  f = os.popen(cmd)
  rtvs = f.readlines()
  if len(rtvs) == 0:
    return None
  else:
    return rtvs

# main
# main method
def main():
  # add your service name here
  # case insensitive
  services = [
    'node',
    'nginx2',
    'mosquitto',
    'freeswitch',
    'mongod', 
    'DarwinStreamin',
    'apache2',
    'vsftpd',
    'sshd'
  ]

  for item in services:
    rtvs = CheckService(item)
    if rtvs == None:
      #print "%20s\t\tOFF" % item
      #print "%20s\t\tOFF" % item
      print '\033[1;31m%25s\t\tOFF\033[1;m' % item
    else:
      for res in rtvs:
        matchObj = re.match(r'.*:(\d+) .*', res, re.M|re.I)
        tmp = item + '\\' + matchObj.group(1)
        print '\033[1;32m%25s\t\tON\033[1;m' % tmp


if __name__ == '__main__':
  main()
