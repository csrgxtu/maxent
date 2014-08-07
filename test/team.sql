CREATE TABLE `team` (
  `team_id` INT NOT NULL,
  `name` VARCHAR(255) NULL COMMENT 'name of the team',
  `name_cn` VARCHAR(255) NULL COMMENT 'Chinese team name',
  `logo` VARCHAR(255) NULL COMMENT 'logo of the team, it is a url',
  `location_id` INT NULL COMMENT 'reference to the location table, since every team must belongs a country, state, city',
  `league_id` INT NULL COMMENT 'reference league id, every team must belongs to a league.',
  `found_time` YEAR NULL COMMENT 'foundation time of the team',
  `home_court` VARCHAR(255) NULL COMMENT 'the court where the host team plays its home games',
  `home_court_cn` VARCHAR(255) NULL COMMENT 'the Chinese name of the home court',
  `current_manager` VARCHAR(255) NULL,
  `current_manager_cn` VARCHAR(255) NULL COMMENT 'Chinese version of the current manager',
  `description` TEXT NULL COMMENT 'description of the team',
  `award_data` TEXT NULL COMMENT 'award data of the team',
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  `league_league_id` INT NOT NULL,
  `team_tech_statistics_team_tech_statistics_id` INT NOT NULL,
  `location_location_id` INT NOT NULL,
  PRIMARY KEY (`team_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  UNIQUE INDEX `name_cn_UNIQUE` (`name_cn` ASC),
  UNIQUE INDEX `logo_UNIQUE` (`logo` ASC),
  UNIQUE INDEX `team_id_UNIQUE` (`team_id` ASC),
  INDEX `fk_team_league_idx` (`league_league_id` ASC),
  INDEX `fk_team_team_tech_statistics1_idx` (`team_tech_statistics_team_tech_statistics_id` ASC),
  INDEX `fk_team_location1_idx` (`location_location_id` ASC),
  CONSTRAINT `fk_team_league`
    FOREIGN KEY (`league_league_id`)
    REFERENCES `mydb`.`league` (`league_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_team_team_tech_statistics1`
    FOREIGN KEY (`team_tech_statistics_team_tech_statistics_id`)
    REFERENCES `mydb`.`team_tech_statistics` (`team_tech_statistics_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_team_location1`
    FOREIGN KEY (`location_location_id`)
    REFERENCES `mydb`.`location` (`location_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'information table of the team or club'
