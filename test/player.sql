CREATE TABLE `player` (
  `player_id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `name_abbreviation` VARCHAR(255) NULL,
  `name_cn` VARCHAR(255) NULL,
  `name_abbreviation_cn` VARCHAR(255) NULL,
  `location_id` INT NULL COMMENT 'reference to location table',
  `weight` DECIMAL NULL,
  `height` DECIMAL NULL,
  `age` INT NULL,
  `number` INT NULL COMMENT 'number representation of this player',
  `birthday` DATETIME NULL,
  `player_role_id` INT NULL COMMENT 'reference to the player_role table',
  `team_id` INT NULL COMMENT 'reference to team table to indicate which team it belongs',
  `description` TEXT NULL,
  `award_data` TEXT NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  `team_id` INT NOT NULL,
  `player_tech_statistics_id` INT NOT NULL,
  `player_role_id` INT NOT NULL,
  `goal_keeper_statistics_id` INT NOT NULL,
  PRIMARY KEY (`player_id`),
  UNIQUE INDEX `player_id_UNIQUE` (`player_id` ASC),
  INDEX `fk_player_team1_idx` (`team_team_id` ASC),
  INDEX `fk_player_player_tech_statistics1_idx` (`player_tech_statistics_player_tech_statistics_id` ASC),
  INDEX `fk_player_player_role1_idx` (`player_role_player_role_id` ASC),
  INDEX `fk_player_goal_keeper_statistics1_idx` (`goal_keeper_statistics_goal_keeper_statistics_id` ASC),
  CONSTRAINT `fk_player_team1`
    FOREIGN KEY (`team_team_id`)
    REFERENCES `football_db`.`team` (`team_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_player_tech_statistics1`
    FOREIGN KEY (`player_tech_statistics_player_tech_statistics_id`)
    REFERENCES `football_db`.`player_tech_statistics` (`player_tech_statistics_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_player_role1`
    FOREIGN KEY (`player_role_player_role_id`)
    REFERENCES `football_db`.`player_role` (`player_role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_goal_keeper_statistics1`
    FOREIGN KEY (`goal_keeper_statistics_goal_keeper_statistics_id`)
    REFERENCES `football_db`.`goal_keeper_statistics` (`goal_keeper_statistics_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'information table of player'
