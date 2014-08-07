CREATE TABLE `league` (
  `league_id` INT NOT NULL,
  `name` VARCHAR(255) NULL COMMENT 'the name of the league',
  `name_abbreviation` VARCHAR(255) NULL COMMENT 'abbreviation of the name',
  `name_cn` VARCHAR(255) NULL COMMENT 'Chinese version of the league name, i.e, 西甲',
  `name_abbreviation_cn` VARCHAR(255) NULL COMMENT 'Chinese abbreviation of the name',
  `district` VARCHAR(255) NULL COMMENT 'the district that league belongs too',
  `logo` VARCHAR(255) NULL COMMENT 'the logo of the league',
  `found_time` YEAR NULL COMMENT 'the foundation time of the league',
  `team_number` INT NULL COMMENT 'number of teams this league contains',
  `description` TEXT NULL COMMENT 'description of the league',
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  `location_location_id` INT NOT NULL,
  PRIMARY KEY (`league_id`),
  UNIQUE INDEX `league_id_UNIQUE` (`league_id` ASC),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  UNIQUE INDEX `name_abbreviation_UNIQUE` (`name_abbreviation` ASC),
  UNIQUE INDEX `name_cn_UNIQUE` (`name_cn` ASC),
  UNIQUE INDEX `name_abbreviation_cn_UNIQUE` (`name_abbreviation_cn` ASC),
  UNIQUE INDEX `logo_UNIQUE` (`logo` ASC),
  INDEX `fk_league_location1_idx` (`location_location_id` ASC),
  CONSTRAINT `fk_league_location1`
    FOREIGN KEY (`location_location_id`)
    REFERENCES `football_db`.`location` (`location_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'information table of league'
