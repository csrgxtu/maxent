SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `NBA` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `NBA` ;

-- -----------------------------------------------------
-- Table `NBA`.`Team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`Team` (
  `TeamID` INT NOT NULL AUTO_INCREMENT,
  `StatsID` CHAR(10) NULL COMMENT 'the ID stats.com gives to the team',
  `NameEN` VARCHAR(128) NULL COMMENT 'the full name of the team',
  `ShortNameEN` VARCHAR(64) NULL,
  `NameCN` VARCHAR(128) NULL,
  `ShortNameCN` VARCHAR(64) NULL,
  `Description` TEXT NULL,
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` DATETIME NULL,
  PRIMARY KEY (`TeamID`),
  UNIQUE INDEX `TeamsID_UNIQUE` (`TeamID` ASC),
  UNIQUE INDEX `Teamscol_UNIQUE` (`StatsID` ASC),
  UNIQUE INDEX `TeamName_UNIQUE` (`NameEN` ASC),
  UNIQUE INDEX `NameCN_UNIQUE` (`NameCN` ASC),
  UNIQUE INDEX `ShortNameEN_UNIQUE` (`ShortNameEN` ASC),
  UNIQUE INDEX `ShortNameCN_UNIQUE` (`ShortNameCN` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `NBA`.`TeamBackground`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`TeamBackground` (
  `TeamBackgroundID` INT NOT NULL AUTO_INCREMENT,
  `TeamBackground_TeamID` INT NULL,
  `FoundDate` DATE NULL,
  `City` VARCHAR(128) NULL,
  `Arena` VARCHAR(128) NULL,
  `Owner` VARCHAR(128) NULL,
  `Manager` VARCHAR(128) NULL,
  `HeadCoach` VARCHAR(128) NULL,
  `DLeague` VARCHAR(128) NULL,
  `History` VARCHAR(128) NULL,
  `OfficialWebsite` VARCHAR(256) NULL,
  `Facebook` VARCHAR(256) NULL,
  `Twitter` VARCHAR(256) NULL,
  `Instagram` VARCHAR(256) NULL,
  `Logo` VARCHAR(256) NULL,
  `Description` TEXT NULL,
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` DATETIME NULL,
  PRIMARY KEY (`TeamBackgroundID`),
  UNIQUE INDEX `TeamBackgroundID_UNIQUE` (`TeamBackgroundID` ASC),
  INDEX `fk_TeamBackground_Team_idx` (`TeamBackground_TeamID` ASC),
  CONSTRAINT `fk_TeamBackground_Team`
    FOREIGN KEY (`TeamBackground_TeamID`)
    REFERENCES `NBA`.`Team` (`TeamID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `NBA`.`SeasonType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`SeasonType` (
  `SeasonTypeID` INT NOT NULL AUTO_INCREMENT,
  `Type` VARCHAR(128) NULL,
  `Description` TEXT NULL,
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` DATETIME NULL,
  PRIMARY KEY (`SeasonTypeID`),
  UNIQUE INDEX `SeasonTypeID_UNIQUE` (`SeasonTypeID` ASC),
  UNIQUE INDEX `Type_UNIQUE` (`Type` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `NBA`.`Season`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`Season` (
  `SeasonID` INT NOT NULL AUTO_INCREMENT,
  `Season_SeasonTypeID` INT NULL,
  `Season` VARCHAR(128) NULL,
  `Description` TEXT NULL,
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` VARCHAR(45) NULL,
  PRIMARY KEY (`SeasonID`),
  UNIQUE INDEX `SeasonID_UNIQUE` (`SeasonID` ASC),
  INDEX `fk_Season_SeasonType_idx` (`Season_SeasonTypeID` ASC),
  CONSTRAINT `fk_Season_SeasonType`
    FOREIGN KEY (`Season_SeasonTypeID`)
    REFERENCES `NBA`.`SeasonType` (`SeasonTypeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `NBA`.`TeamStats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`TeamStats` (
  `TeamStatsID` INT NOT NULL AUTO_INCREMENT,
  `TeamStats_TeamID` INT NULL,
  `TeamStats_SeasonID` INT NULL,
  `Result` CHAR(1) NULL,
  `Date` VARCHAR(128) NULL,
  `Home` TINYINT(1) NULL,
  `Min` INT NULL COMMENT 'the number of minutes a team played',
  `Points` INT NULL COMMENT 'the number of points a team scores',
  `Fgm` INT NULL COMMENT 'field goal made',
  `Fga` INT NULL COMMENT 'field goal attempt',
  `3pm` INT NULL COMMENT '3 point filed goal made',
  `3pa` INT NULL COMMENT '3 point field goal attempted',
  `Ftm` INT NULL COMMENT 'free throw made',
  `Fta` INT NULL COMMENT 'free throw attempted',
  `Oreb` INT NULL COMMENT 'Offensive rebounds',
  `Dreb` INT NULL COMMENT 'defensive rebounds',
  `Ast` INT NULL COMMENT 'assit occurs',
  `Stl` INT NULL COMMENT 'steal made',
  `Blk` INT NULL COMMENT 'blocks made',
  `Tov` INT NULL COMMENT 'turn over throwover',
  `Pf` INT NULL COMMENT 'personal fouls team made',
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` DATETIME NULL,
  `Description` TEXT NULL,
  `OpponentTeamID` INT NULL,
  PRIMARY KEY (`TeamStatsID`),
  UNIQUE INDEX `TeamStatsID_UNIQUE` (`TeamStatsID` ASC),
  INDEX `fk_TeamStats_Season_idx` (`TeamStats_SeasonID` ASC),
  INDEX `fk_TeamStats_Team_idx` (`TeamStats_TeamID` ASC),
  CONSTRAINT `fk_TeamStats_Team`
    FOREIGN KEY (`TeamStats_TeamID`)
    REFERENCES `NBA`.`Team` (`TeamID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TeamStats_Season`
    FOREIGN KEY (`TeamStats_SeasonID`)
    REFERENCES `NBA`.`Season` (`SeasonID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `NBA`.`OddsCompany`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`OddsCompany` (
  `OddsComapanyID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(128) NULL,
  `OfficialWebsite` VARCHAR(256) NULL,
  `Description` TEXT NULL,
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` DATETIME NULL,
  PRIMARY KEY (`OddsComapanyID`),
  UNIQUE INDEX `OddsComapanyID_UNIQUE` (`OddsComapanyID` ASC),
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `NBA`.`Odds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `NBA`.`Odds` (
  `OddsID` INT NOT NULL AUTO_INCREMENT,
  `Odds_TeamStatsID` INT NULL,
  `Odds_OddsCompanyID` INT NULL,
  `Value1` FLOAT NULL,
  `Value2` FLOAT NULL,
  `CreatedBy` VARCHAR(128) NULL,
  `CreatedTime` DATETIME NULL,
  `UpdatedBy` VARCHAR(128) NULL,
  `UpdatedTime` DATETIME NULL,
  PRIMARY KEY (`OddsID`),
  UNIQUE INDEX `OddsID_UNIQUE` (`OddsID` ASC),
  INDEX `fk_Odds_TeamStats_idx` (`Odds_TeamStatsID` ASC),
  INDEX `fk_Odds_OddsCompany_idx` (`Odds_OddsCompanyID` ASC),
  CONSTRAINT `fk_Odds_TeamStats`
    FOREIGN KEY (`Odds_TeamStatsID`)
    REFERENCES `NBA`.`TeamStats` (`TeamStatsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Odds_OddsCompany`
    FOREIGN KEY (`Odds_OddsCompanyID`)
    REFERENCES `NBA`.`OddsCompany` (`OddsComapanyID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
