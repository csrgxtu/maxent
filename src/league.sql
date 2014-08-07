CREATE TABLE `league` (
  `league_id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `name_abbreviation` VARCHAR(255),
  `name_cn` VARCHAR(255) NULL,
  `name_abbreviation_cn` VARCHAR(255),
  `district` VARCHAR(255) NULL,
  `logo` VARCHAR(255) NULL,
  `found_time` YEAR NULL,
  `team_number` INT NULL,
  `description` TEXT NULL,
  `location_id` INT NOT NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  PRIMARY KEY (`league_id`)
)
