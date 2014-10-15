CREATE TABLE `team` (
  `team_id` INT NOT NULL,
  `name` VARCHAR(255) NULL UNIQUE,
  `name_cn` VARCHAR(255) NULL UNIQUE,
  `logo` VARCHAR(255) NULL UNIQUE,
  `location_id` INT NULL,
  `league_id` INT NULL,
  `found_time` YEAR NULL,
  `home_court` VARCHAR(255) NULL,
  `home_court_cn` VARCHAR(255) NULL,
  `current_manager` VARCHAR(255) NULL,
  `current_manager_cn` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `award_data` TEXT NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  PRIMARY KEY (`team_id`)
)

