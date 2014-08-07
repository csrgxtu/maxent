CREATE TABLE `goal_keeper_statistics` (
  `goal_keeper_statistics_id` INT NOT NULL,
  `player_id` INT NULL COMMENT 'reference to the player table to indicate which player',
  `start` VARCHAR(255) NULL,
  `play_time` INT NULL,
  `lose` INT NULL,
  `touch` INT NULL,
  `attack` INT NULL COMMENT ' 	出击',
  `save` INT NULL,
  `save_penalty` INT NULL,
  `save_must_in_goal` INT NULL,
  `foul` INT NULL,
  `red_card` INT NULL,
  `yellow_card` INT NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  `result_result_id` INT NOT NULL,
  PRIMARY KEY (`goal_keeper_statistics_id`),
  UNIQUE INDEX `goal_keeper_statistics_id_UNIQUE` (`goal_keeper_statistics_id` ASC),
  INDEX `fk_goal_keeper_statistics_result1_idx` (`result_result_id` ASC),
  CONSTRAINT `fk_goal_keeper_statistics_result1`
    FOREIGN KEY (`result_result_id`)
    REFERENCES `mydb`.`result` (`result_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'statistics data about the goal keeper'
