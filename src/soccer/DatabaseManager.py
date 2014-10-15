#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 12/Aug/2014
# File: DatabaseManager.py
# Description: class for database related operations
# Website: http://csrgxtu.blog.com
#
# Produced By CSRGXTU
import MySQLdb as MySQL

class DatabaseManager(object):
  
  host = 'localhost'
  port = '3306'
  userName = 'root'
  passWord = 'root'
  dataBase = 'football_db'

  conn = None
  curs = None

  def __init__(self):
    self.conn = MySQL.connect(host = self.host,\
      user = self.userName, passwd = self.passWord,\
      db = self.dataBase)
    self.curs = self.conn.cursor()

  # execSql
  # execute an sql statement
  #
  # @parameter sqlStatement (string)
  # @return void
  def execSql(self, sqlStatement):
    try:
      self.curs.execute(sqlStatement)
    finally:
      self.commitConn()

  # getResults
  # get the execute results
  #
  # @return list
  def getResults(self):
    return self.curs.fetchall()

  # test
  #
  def test(self):
    for row in self.curs.fetchall():
      print row[1]

  def gethost(self):
    return self.host

  def getPort(self):
    return self.port

  def getUserName(self):
    return self.userName

  def getPassWord(self):
    return self.passWord

  def getDataBase(self):
    return self.dataBase

  def getConn(self):
    return self.conn

  def getCurs(self):
    return self.curs

  def setHost(self, host):
    self.host = host

  def setPort(self, port):
    self.port = port

  def setUserName(self, userName):
    self.userName = userName

  def setPassWord(self, passWord):
    self.passWord = passWord

  def setDataBase(self, dataBase):
    self.dataBase = dataBase

  def setConn(self, conn):
    self.conn = conn

  def setCurs(self, curs):
    self.curs = curs

  def commitConn(self):
    self.conn.commit()

  def closeCurs(self):
    self.curs.close()

  def closeConn(self):
    self.conn.close()

  def close(self):
    self.commitConn()
    self.closeCurs()
    self.closeConn()

  def __del__(self):
    self.conn.commit()
    self.closeCurs()
    self.closeConn()
