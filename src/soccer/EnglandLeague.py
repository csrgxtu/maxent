#!/usr/bin/env python
#coding=utf-8
#
# Author: Archer Reilly
# Date: 15/Aug/2014
# File: EnglandLeague.py 
# Description: glue script make all class work together and
# insert into the database
# Website: http://csrgxtu.blog.com
#
# Produced By CSRXTU
from Download import Download
from TeamInfoParser import TeamInfoParser
from TeamTechStatisticsParser13 import TeamTechStatisticsParser13
from TeamTechStatisticsParser12 import TeamTechStatisticsParser12
from TeamTechStatisticsParser11 import TeamTechStatisticsParser11
from TeamTechStatisticsParser10 import TeamTechStatisticsParser10
from TeamTechStatisticsParser import TeamTechStatisticsParser
from PlayerTechStatisticsParser13League import PlayerTechStatisticsParser13League
from PlayerTechStatisticsParser13Champion import PlayerTechStatisticsParser13Champion
from PlayerTechStatisticsParser12League import PlayerTechStatisticsParser12League
from PlayerTechStatisticsParser12Champion import PlayerTechStatisticsParser12Champion
from PlayerTechStatisticsParser11League import PlayerTechStatisticsParser11League
from PlayerTechStatisticsParser11Champion import PlayerTechStatisticsParser11Champion
from PlayerTechStatisticsParser10League import PlayerTechStatisticsParser10League
from PlayerTechStatisticsParser10Champion import PlayerTechStatisticsParser10Champion
from GoalKeeperParser13League import GoalKeeperParser13League
from GoalKeeperParser13Champion import GoalKeeperParser13Champion
from GoalKeeperParser12League import GoalKeeperParser12League
from GoalKeeperParser12Champion import GoalKeeperParser12Champion
from GoalKeeperParser11League import GoalKeeperParser11League
from GoalKeeperParser11Champion import GoalKeeperParser11Champion
from GoalKeeperParser10League import GoalKeeperParser10League
from GoalKeeperParser10Champion import GoalKeeperParser10Champion
from PlayerInfoParser import PlayerInfoParser
from DatabaseManager import DatabaseManager

class EnglandLeague(object):
  
  htmlObj = None
  dbObj = None

  team = None

  def __init__(self, url):
    self.htmlObj = Download(url)

    if self.htmlObj.doRequest() == 1:
      print "Download cant do request on: ", url
    
    self.dbObj = DatabaseManager()
  
  # teamInfo
  # get team info and insert the data into the database
  #
  # @return true or false
  def teamInfo(self):
    parser = TeamInfoParser(self.htmlObj.getSOURCE())

    name = unicode(parser.getTeamName()).encode('utf-8')
    self.team = name
    name_cn = unicode(parser.getTeamNameCN()).encode('utf-8')
    logo = unicode(parser.getTeamLogo()).encode('utf-8')
    city = unicode(parser.getTeamCity()).encode('utf-8')
    league = unicode(parser.getTeamLeague()).encode('utf-8')
    found_time = unicode(parser.getTeamFoundTime()).encode('utf-8')
    home_court_cn = unicode(parser.getTeamHomeCourtCN()).encode('utf-8')
    current_manager_cn = unicode(parser.getTeamCurrentManagerCN()).encode('utf-8')
    description = unicode(parser.getTeamDescription()).encode('utf-8')
    award_data = unicode(parser.getTeamAwardData()).encode('utf-8')

    sql = "INSERT INTO team (name, name_cn, logo, city, league,\
      found_time, home_court_cn, current_manager_cn, description,\
      award_data) VALUES ('" + name + "', '" + name_cn + "', '"\
      + logo + "', '" + city + "', '" + league + "', '"\
      + found_time + "', '" + home_court_cn + "', '" + current_manager_cn\
      + "', '" + description + "', '" + award_data + "');";
    print sql
    self.dbObj.execSql(sql)

  # teamTechStatistics13
  # get and insert team tech statistics
  #
  # @return true of false
  def teamTechStatistics13(self):
    parser13 = TeamTechStatisticsParser13(self.htmlObj.getSOURCE())

    if parser13.getLeagues() == None:
      return False

    leagues = self.toUtf8(parser13.getLeagues())
    wins = self.toUtf8(parser13.getWins())
    flats = self.toUtf8(parser13.getFlats())
    loses = self.toUtf8(parser13.getLoses())
    goals = self.toUtf8(parser13.getGoals())
    fumbles = self.toUtf8(parser13.getFumbles())
    assistances = self.toUtf8(parser13.getAssistances())
    passes = self.toUtf8(parser13.getPasses())
    steals = self.toUtf8(parser13.getSteals())
    offsides = self.toUtf8(parser13.getOffsides())
    fouls = self.toUtf8(parser13.getFouls())
    redCards = self.toUtf8(parser13.getRedCards())
    yellowCards = self.toUtf8(parser13.getYellowCards())
    shoots = self.toUtf8(parser13.getShoots())
    shootOnGoals = self.toUtf8(parser13.getShootOnGoals())
    shootOnGoalRates = self.toUtf8(parser13.getShootOnGoalRates())
    successRates = self.toUtf8(parser13.getSuccessRates())
    headGoals = self.toUtf8(parser13.getHeadGoals())
    directFreeGoals = self.toUtf8(parser13.getDirectFreeGoals())
    penaltyKicks = self.toUtf8(parser13.getPenaltyKicks())
    penaltyKickGoals = self.toUtf8(parser13.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser13.getIntercepts())
    rescues = self.toUtf8(parser13.getRescues())
    headRescues = self.toUtf8(parser13.getHeadRescues())
    backFieldRescues = self.toUtf8(parser13.getBackFieldRescues())
    successHeaders = self.toUtf8(parser13.getSuccessHeaders())
    failHeaders = self.toUtf8(parser13.getFailHeaders())
    ownGoals = self.toUtf8(parser13.getOwnGoals())

    matrice = []
    #matrice.append([self.team, self.team])
    matrice.append([self.team for i in range(len(leagues))])
    # season 13
    #matrice.append([13, 13])
    matrice.append([13 for i in range(len(leagues))])
    matrice.append(leagues)
    matrice.append(wins)
    matrice.append(flats)
    matrice.append(loses)
    matrice.append(goals)
    matrice.append(fumbles)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(redCards)
    matrice.append(yellowCards)
    matrice.append(shoots)
    matrice.append(shootOnGoals)
    matrice.append(shootOnGoalRates)
    matrice.append(successRates)
    matrice.append(headGoals)
    matrice.append(directFreeGoals)
    matrice.append(penaltyKicks)
    matrice.append(penaltyKickGoals)
    matrice.append(intercepts)
    matrice.append(rescues)
    matrice.append(headRescues)
    matrice.append(backFieldRescues)
    matrice.append(successHeaders)
    matrice.append(failHeaders)
    matrice.append(ownGoals)

    sql = "INSERT INTO team_tech_statistics (team, season, league, win,"\
      + " flat, lose, goal, fumble, assistance, pass, steal, offside,"\
      + " foul, red_card, yellow_card, shoot, shoot_on_goal,"\
      + " shoot_on_goal_rate, success_rate, head_goal,"\
      + " direct_free_goal, penalty_kick, penalty_kick_goal,"\
      + " intercept, rescue, head_rescue, back_field_rescue,"\
      + " success_headers, fail_headers, own_goal) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)
  
  # teamTechStatistics12
  # get and insert team tech statistics
  #
  # @return true of false
  def teamTechStatistics12(self):
    parser12 = TeamTechStatisticsParser12(self.htmlObj.getSOURCE())

    if parser12.getLeagues() == None:
      return False

    leagues = self.toUtf8(parser12.getLeagues())
    wins = self.toUtf8(parser12.getWins())
    flats = self.toUtf8(parser12.getFlats())
    loses = self.toUtf8(parser12.getLoses())
    goals = self.toUtf8(parser12.getGoals())
    fumbles = self.toUtf8(parser12.getFumbles())
    assistances = self.toUtf8(parser12.getAssistances())
    passes = self.toUtf8(parser12.getPasses())
    steals = self.toUtf8(parser12.getSteals())
    offsides = self.toUtf8(parser12.getOffsides())
    fouls = self.toUtf8(parser12.getFouls())
    redCards = self.toUtf8(parser12.getRedCards())
    yellowCards = self.toUtf8(parser12.getYellowCards())
    shoots = self.toUtf8(parser12.getShoots())
    shootOnGoals = self.toUtf8(parser12.getShootOnGoals())
    shootOnGoalRates = self.toUtf8(parser12.getShootOnGoalRates())
    successRates = self.toUtf8(parser12.getSuccessRates())
    headGoals = self.toUtf8(parser12.getHeadGoals())
    directFreeGoals = self.toUtf8(parser12.getDirectFreeGoals())
    penaltyKicks = self.toUtf8(parser12.getPenaltyKicks())
    penaltyKickGoals = self.toUtf8(parser12.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser12.getIntercepts())
    rescues = self.toUtf8(parser12.getRescues())
    headRescues = self.toUtf8(parser12.getHeadRescues())
    backFieldRescues = self.toUtf8(parser12.getBackFieldRescues())
    successHeaders = self.toUtf8(parser12.getSuccessHeaders())
    failHeaders = self.toUtf8(parser12.getFailHeaders())
    ownGoals = self.toUtf8(parser12.getOwnGoals())

    matrice = []
    #matrice.append([self.team, self.team])
    matrice.append([self.team for i in range(len(leagues))])
    # season 13
    #matrice.append([12, 12])
    matrice.append([12 for i in range(len(leagues))])
    matrice.append(leagues)
    matrice.append(wins)
    matrice.append(flats)
    matrice.append(loses)
    matrice.append(goals)
    matrice.append(fumbles)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(redCards)
    matrice.append(yellowCards)
    matrice.append(shoots)
    matrice.append(shootOnGoals)
    matrice.append(shootOnGoalRates)
    matrice.append(successRates)
    matrice.append(headGoals)
    matrice.append(directFreeGoals)
    matrice.append(penaltyKicks)
    matrice.append(penaltyKickGoals)
    matrice.append(intercepts)
    matrice.append(rescues)
    matrice.append(headRescues)
    matrice.append(backFieldRescues)
    matrice.append(successHeaders)
    matrice.append(failHeaders)
    matrice.append(ownGoals)

    sql = "INSERT INTO team_tech_statistics (team, season, league, win,"\
      + " flat, lose, goal, fumble, assistance, pass, steal, offside,"\
      + " foul, red_card, yellow_card, shoot, shoot_on_goal,"\
      + " shoot_on_goal_rate, success_rate, head_goal,"\
      + " direct_free_goal, penalty_kick, penalty_kick_goal,"\
      + " intercept, rescue, head_rescue, back_field_rescue,"\
      + " success_headers, fail_headers, own_goal) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)
  
  # teamTechStatistics11
  # get and insert team tech statistics
  #
  # @return true of false
  def teamTechStatistics11(self):
    parser11 = TeamTechStatisticsParser11(self.htmlObj.getSOURCE())

    if parser11.getLeagues() == None:
      return False

    leagues = self.toUtf8(parser11.getLeagues())
    wins = self.toUtf8(parser11.getWins())
    flats = self.toUtf8(parser11.getFlats())
    loses = self.toUtf8(parser11.getLoses())
    goals = self.toUtf8(parser11.getGoals())
    fumbles = self.toUtf8(parser11.getFumbles())
    assistances = self.toUtf8(parser11.getAssistances())
    passes = self.toUtf8(parser11.getPasses())
    steals = self.toUtf8(parser11.getSteals())
    offsides = self.toUtf8(parser11.getOffsides())
    fouls = self.toUtf8(parser11.getFouls())
    redCards = self.toUtf8(parser11.getRedCards())
    yellowCards = self.toUtf8(parser11.getYellowCards())
    shoots = self.toUtf8(parser11.getShoots())
    shootOnGoals = self.toUtf8(parser11.getShootOnGoals())
    shootOnGoalRates = self.toUtf8(parser11.getShootOnGoalRates())
    successRates = self.toUtf8(parser11.getSuccessRates())
    headGoals = self.toUtf8(parser11.getHeadGoals())
    directFreeGoals = self.toUtf8(parser11.getDirectFreeGoals())
    penaltyKicks = self.toUtf8(parser11.getPenaltyKicks())
    penaltyKickGoals = self.toUtf8(parser11.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser11.getIntercepts())
    rescues = self.toUtf8(parser11.getRescues())
    headRescues = self.toUtf8(parser11.getHeadRescues())
    backFieldRescues = self.toUtf8(parser11.getBackFieldRescues())
    successHeaders = self.toUtf8(parser11.getSuccessHeaders())
    failHeaders = self.toUtf8(parser11.getFailHeaders())
    ownGoals = self.toUtf8(parser11.getOwnGoals())

    matrice = []
    #matrice.append([self.team, self.team])
    matrice.append([self.team for i in range(len(leagues))])
    # season 13
    #matrice.append([11, 11])
    matrice.append([11 for i in range(len(leagues))])
    matrice.append(leagues)
    matrice.append(wins)
    matrice.append(flats)
    matrice.append(loses)
    matrice.append(goals)
    matrice.append(fumbles)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(redCards)
    matrice.append(yellowCards)
    matrice.append(shoots)
    matrice.append(shootOnGoals)
    matrice.append(shootOnGoalRates)
    matrice.append(successRates)
    matrice.append(headGoals)
    matrice.append(directFreeGoals)
    matrice.append(penaltyKicks)
    matrice.append(penaltyKickGoals)
    matrice.append(intercepts)
    matrice.append(rescues)
    matrice.append(headRescues)
    matrice.append(backFieldRescues)
    matrice.append(successHeaders)
    matrice.append(failHeaders)
    matrice.append(ownGoals)

    sql = "INSERT INTO team_tech_statistics (team, season, league, win,"\
      + " flat, lose, goal, fumble, assistance, pass, steal, offside,"\
      + " foul, red_card, yellow_card, shoot, shoot_on_goal,"\
      + " shoot_on_goal_rate, success_rate, head_goal,"\
      + " direct_free_goal, penalty_kick, penalty_kick_goal,"\
      + " intercept, rescue, head_rescue, back_field_rescue,"\
      + " success_headers, fail_headers, own_goal) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)
  
  # teamTechStatistics10
  # get and insert team tech statistics
  #
  # @return true of false
  def teamTechStatistics10(self):
    parser10 = TeamTechStatisticsParser10(self.htmlObj.getSOURCE())

    if parser10.getLeagues() == None:
      return False

    leagues = self.toUtf8(parser10.getLeagues())
    wins = self.toUtf8(parser10.getWins())
    flats = self.toUtf8(parser10.getFlats())
    loses = self.toUtf8(parser10.getLoses())
    goals = self.toUtf8(parser10.getGoals())
    fumbles = self.toUtf8(parser10.getFumbles())
    assistances = self.toUtf8(parser10.getAssistances())
    passes = self.toUtf8(parser10.getPasses())
    steals = self.toUtf8(parser10.getSteals())
    offsides = self.toUtf8(parser10.getOffsides())
    fouls = self.toUtf8(parser10.getFouls())
    redCards = self.toUtf8(parser10.getRedCards())
    yellowCards = self.toUtf8(parser10.getYellowCards())
    shoots = self.toUtf8(parser10.getShoots())
    shootOnGoals = self.toUtf8(parser10.getShootOnGoals())
    shootOnGoalRates = self.toUtf8(parser10.getShootOnGoalRates())
    successRates = self.toUtf8(parser10.getSuccessRates())
    headGoals = self.toUtf8(parser10.getHeadGoals())
    directFreeGoals = self.toUtf8(parser10.getDirectFreeGoals())
    penaltyKicks = self.toUtf8(parser10.getPenaltyKicks())
    penaltyKickGoals = self.toUtf8(parser10.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser10.getIntercepts())
    rescues = self.toUtf8(parser10.getRescues())
    headRescues = self.toUtf8(parser10.getHeadRescues())
    backFieldRescues = self.toUtf8(parser10.getBackFieldRescues())
    successHeaders = self.toUtf8(parser10.getSuccessHeaders())
    failHeaders = self.toUtf8(parser10.getFailHeaders())
    ownGoals = self.toUtf8(parser10.getOwnGoals())

    matrice = []
    #matrice.append([self.team, self.team])
    matrice.append([self.team for i in range(len(leagues))])
    # season 13
    #matrice.append([10, 10])
    matrice.append([10 for i in range(len(leagues))])
    matrice.append(leagues)
    matrice.append(wins)
    matrice.append(flats)
    matrice.append(loses)
    matrice.append(goals)
    matrice.append(fumbles)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(redCards)
    matrice.append(yellowCards)
    matrice.append(shoots)
    matrice.append(shootOnGoals)
    matrice.append(shootOnGoalRates)
    matrice.append(successRates)
    matrice.append(headGoals)
    matrice.append(directFreeGoals)
    matrice.append(penaltyKicks)
    matrice.append(penaltyKickGoals)
    matrice.append(intercepts)
    matrice.append(rescues)
    matrice.append(headRescues)
    matrice.append(backFieldRescues)
    matrice.append(successHeaders)
    matrice.append(failHeaders)
    matrice.append(ownGoals)

    sql = "INSERT INTO team_tech_statistics (team, season, league, win,"\
      + " flat, lose, goal, fumble, assistance, pass, steal, offside,"\
      + " foul, red_card, yellow_card, shoot, shoot_on_goal,"\
      + " shoot_on_goal_rate, success_rate, head_goal,"\
      + " direct_free_goal, penalty_kick, penalty_kick_goal,"\
      + " intercept, rescue, head_rescue, back_field_rescue,"\
      + " success_headers, fail_headers, own_goal) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)
  
  # teamTechStatistics
  # this differs from upper teamTechStatistics#, for the webpage
  # provides the summerizied information of 10, 11, 12, 13 for
  # the team but only detailed information for 13, this method
  # is used to get and insert the datailed information
  #
  # @return true or false
  def teamTechStatistics(self):
    parser = TeamTechStatisticsParser(self.htmlObj.getSOURCE())

    if parser.getLeagues() == None:
      return False

    leagues = self.toUtf8(parser.getLeagues())
    goals = self.toUtf8(parser.getGoals())
    fumbles = self.toUtf8(parser.getFumbles())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    redCards = self.toUtf8(parser.getRedCards())
    yellowCards = self.toUtf8(parser.getYellowCards())
    shoots = self.toUtf8(parser.getShoots())
    shootOnGoals = self.toUtf8(parser.getShootOnGoals())
    shootOnGoalRates = self.toUtf8(parser.getShootOnGoalRates())
    successRates = self.toUtf8(parser.getSuccessRates())
    headGoals = self.toUtf8(parser.getHeadGoals())
    directFreeGoals = self.toUtf8(parser.getDirectFreeGoals())
    penaltyKicks = self.toUtf8(parser.getPenaltyKicks())
    penaltyKickGoals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    headRescues = self.toUtf8(parser.getHeadRescues())
    backFieldRescues = self.toUtf8(parser.getBackFieldRescues())
    successHeaders = self.toUtf8(parser.getSuccessHeaders())
    failHeaders = self.toUtf8(parser.getFailHeaders())
    ownGoals = self.toUtf8(parser.getOwnGoals())

    dates = self.toUtf8(parser.getDates())
    games = self.toUtf8(parser.getGames())
    results = self.toUtf8(parser.getResults())
    

    matrice = []
    matrice.append([self.team for i in range(len(dates))])
    # season 13
    matrice.append([13 for i in range(len(dates))])
    matrice.append(leagues)
    matrice.append(goals)
    matrice.append(fumbles)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(redCards)
    matrice.append(yellowCards)
    matrice.append(shoots)
    matrice.append(shootOnGoals)
    matrice.append(shootOnGoalRates)
    matrice.append(successRates)
    matrice.append(headGoals)
    matrice.append(directFreeGoals)
    matrice.append(penaltyKicks)
    matrice.append(penaltyKickGoals)
    matrice.append(intercepts)
    matrice.append(rescues)
    matrice.append(headRescues)
    matrice.append(backFieldRescues)
    matrice.append(successHeaders)
    matrice.append(failHeaders)
    matrice.append(ownGoals)
    matrice.append(dates)
    matrice.append(games)
    matrice.append(results)

    

    sql = "INSERT INTO team_tech_statistics (team, season, league,"\
      + " goal, fumble, assistance, pass, steal, offside,"\
      + " foul, red_card, yellow_card, shoot, shoot_on_goal,"\
      + " shoot_on_goal_rate, success_rate, head_goal,"\
      + " direct_free_goal, penalty_kick, penalty_kick_goal,"\
      + " intercept, rescue, head_rescue, back_field_rescue,"\
      + " success_headers, fail_headers, own_goal, date, game, result) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      #self.dbObj.execSql(sqla)
  

  # playerTechStatistics13League
  # get and insert player statisitics in 13 league
  #
  # @return true or false
  def playerTechStatistics13League(self):
    parser = PlayerTechStatisticsParser13League(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([13 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)


  # playerTechStatistics12League
  # get and insert player statisitics in 12 league
  #
  # @return true or false
  def playerTechStatistics12League(self):
    parser = PlayerTechStatisticsParser12League(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([12 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # playerTechStatistics11League
  # get and insert player statisitics in 11 league
  #
  # @return true or false
  def playerTechStatistics11League(self):
    parser = PlayerTechStatisticsParser11League(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([11 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # playerTechStatistics10League
  # get and insert player statisitics in 10 league
  #
  # @return true or false
  def playerTechStatistics10League(self):
    parser = PlayerTechStatisticsParser10League(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([10 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # playerTechStatistics13Champion
  # get and insert player statisitics in 13 champion
  #
  # @return true or false
  def playerTechStatistics13Champion(self):
    parser = PlayerTechStatisticsParser13Champion(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([13 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # playerTechStatistics12Champion
  # get and insert player statisitics in 12 champion
  #
  # @return true or false
  def playerTechStatistics12Champion(self):
    parser = PlayerTechStatisticsParser12Champion(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([12 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # playerTechStatistics11Champion
  # get and insert player statisitics in 11 champion
  #
  # @return true or false
  def playerTechStatistics11Champion(self):
    parser = PlayerTechStatisticsParser11Champion(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([11 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # playerTechStatistics10Champion
  # get and insert player statisitics in 10 champion
  #
  # @return true or false
  def playerTechStatistics10Champion(self):
    parser = PlayerTechStatisticsParser10Champion(self.htmlObj.getSOURCE())

    if parser.getPlayerNames() == None:
      return False

    names = self.toUtf8(parser.getPlayerNames())
    numbers = self.toUtf8(parser.getNumbers())
    roles = self.toUtf8(parser.getRoles())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    goals = self.toUtf8(parser.getGoals())
    assistances = self.toUtf8(parser.getAssistances())
    passes = self.toUtf8(parser.getPasses())
    pass_enemies = self.toUtf8(parser.getPassEnemy())
    steals = self.toUtf8(parser.getSteals())
    offsides = self.toUtf8(parser.getOffsides())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())
    shoots = self.toUtf8(parser.getShoots())
    shoot_on_goals = self.toUtf8(parser.getShootOnGoals())
    shoot_on_goal_rates = self.toUtf8(parser.getShootOnGoalRates())
    head_goals = self.toUtf8(parser.getHeadGoals())
    left_goals = self.toUtf8(parser.getLeftGoals())
    right_goals = self.toUtf8(parser.getRightGoals())
    direct_free_goals = self.toUtf8(parser.getDirectFreeGoals())
    penalty_kicks = self.toUtf8(parser.getPenaltyKicks())
    penalty_kick_goals = self.toUtf8(parser.getPenaltyKickGoals())
    intercepts = self.toUtf8(parser.getIntercepts())
    rescues = self.toUtf8(parser.getRescues())
    head_rescues = self.toUtf8(parser.getHeadRescues())
    back_field_rescues = self.toUtf8(parser.getBackFieldRescues())
    success_headers = self.toUtf8(parser.getSuccessHeaders())
    fail_headers = self.toUtf8(parser.getFailHeaders())
    own_goals = self.toUtf8(parser.getOwnGoals())

    matrice = []
    matrice.append(names)
    matrice.append(numbers)
    matrice.append(roles)
    matrice.append([10 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(goals)
    matrice.append(assistances)
    matrice.append(passes)
    matrice.append(pass_enemies)
    matrice.append(steals)
    matrice.append(offsides)
    matrice.append(fouls)
    matrice.append(cards)
    matrice.append(own_goals)
    matrice.append(fail_headers)
    matrice.append(success_headers)
    matrice.append(back_field_rescues)
    matrice.append(head_rescues)
    matrice.append(rescues)
    matrice.append(intercepts)
    matrice.append(penalty_kick_goals)
    matrice.append(penalty_kicks)
    matrice.append(direct_free_goals)
    matrice.append(right_goals)
    matrice.append(left_goals)
    matrice.append(head_goals)
    matrice.append(shoot_on_goal_rates)
    matrice.append(shoot_on_goals)
    matrice.append(shoots)

    sql = "INSERT INTO player_tech_statistics (player, number, role,"\
      + " season, league, start, play_time, goal, assistance, pass,"\
      + " pass_enemy, steal, offside, foul, cards, own_goal, fail_head,"\
      + " success_head, back_field_rescue, head_rescue, rescue, intercept,"\
      + " penalty_kick_goal, penalty_kick, direct_free_goal, right_goal,"\
      + " left_goal, head_goal, shoot_on_goal_rate, shoot_on_goal, shoot)"\
      + " VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)
  
  # goalKeeperStatistics13League
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics13League(self):
    parser = GoalKeeperParser13League(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([13 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # goalKeeperStatistics12League
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics12League(self):
    parser = GoalKeeperParser12League(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([12 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # goalKeeperStatistics11League
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics11League(self):
    parser = GoalKeeperParser11League(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([11 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)


  # goalKeeperStatistics10League
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics10League(self):
    parser = GoalKeeperParser10League(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([10 for i in range(len(names))])
    matrice.append(['英超' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)


  # goalKeeperStatistics13Champion
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics13Champion(self):
    parser = GoalKeeperParser13Champion(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([13 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # goalKeeperStatistics12Champion
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics12Champion(self):
    parser = GoalKeeperParser12Champion(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([12 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)


  # goalKeeperStatistics11Champion
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics11Champion(self):
    parser = GoalKeeperParser11Champion(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([11 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)


  # goalKeeperStatistics10Champion
  # get and insert statistics data about goal keeper
  #
  # @return true or false
  def goalKeeperStatistics10Champion(self):
    parser = GoalKeeperParser10Champion(self.htmlObj.getSOURCE())

    if parser.getPlayers() == None:
      return False

    names = self.toUtf8(parser.getPlayers())
    numbers = self.toUtf8(parser.getNumbers())
    starts = self.toUtf8(parser.getStarts())
    play_times = self.toUtf8(parser.getPlayTime())
    fumbles = self.toUtf8(parser.getFumbles())
    touchs = self.toUtf8(parser.getTouchs())
    attacks = self.toUtf8(parser.getAttacks())
    saves =self.toUtf8(parser.getSaves())
    save_penalties = self.toUtf8(parser.getSavePenalties())
    must_in_goals = self.toUtf8(parser.getMustInGoals())
    one_vs_ones = self.toUtf8(parser.getOneVSOnes())
    fouls = self.toUtf8(parser.getFouls())
    cards = self.toUtf8(parser.getCards())

    matrice = []
    matrice.append(names)
    matrice.append([10 for i in range(len(names))])
    matrice.append(['欧冠' for i in range(len(names))])
    matrice.append(numbers)
    matrice.append(starts)
    matrice.append(play_times)
    matrice.append(fumbles)
    matrice.append(touchs)
    matrice.append(attacks)
    matrice.append(saves)
    matrice.append(save_penalties)
    matrice.append(must_in_goals)
    matrice.append(one_vs_ones)
    matrice.append(fouls)
    matrice.append(cards)

    sql = "INSERT INTO goal_keeper_statistics (player, season,"\
      + " league, number, start, play_time, fumble, touch, attack,"\
      + " save, save_penalty, save_must_in_goal, save_one_one, foul,"\
      + " cards) VALUES (";

    for i in range(len(matrice[0])):
      sqla = sql
      for j in range(len(matrice)):
        if j == (len(matrice) - 1):
          sqla += "'" + str(matrice[j][i]) + "');"
        else:
          sqla += "'" + str(matrice[j][i]) + "', "
      print sqla
      self.dbObj.execSql(sqla)

  # toUtf8
  # transcode an list of item from other coding to utf8
  #
  # @parameter lst (list)
  # @return res (list)
  def toUtf8(self, lst):
    res = []
    for item in lst:
      res.append(unicode(item).encode('utf-8'))

    return res

  def getHtmlObj(self):
    return self.htmlObj

  def setHtmlObj(self, htmlObj):
    self.htmlObj = htmlObj
  
  def getDbObj(self):
    return self.dbObj

  def setDbObj(self, dbObj):
    self.dbObj = dbObj

  def __del__(self):
    class_name = self.__class__.__name__
    print class_name, "destroyed"
