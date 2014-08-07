CREATE TABLE `player_tech_statistics` (
  `player_tech_statistics_id` INT NOT NULL,
  `player_id` INT NULL COMMENT 'reference to the player table indicate which player',
  `start` VARCHAR(255) NULL COMMENT 'i.e 出场/首发 	',
  `play_time` INT NULL COMMENT 'how long the player played',
  `goal` INT NULL,
  `assistance` INT NULL,
  `pass` INT NULL,
  `pass_enemy` INT NULL,
  `steal` INT NULL,
  `offside` INT NULL,
  `foul` INT NULL,
  `red_card` INT NULL,
  `yellow_card` INT NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  `season` VARCHAR(45) NULL COMMENT 'which season\'s statistics data',
  `result_result_id` INT NOT NULL,
  PRIMARY KEY (`player_tech_statistics_id`),
  UNIQUE INDEX `player_tech_statistics_id_UNIQUE` (`player_tech_statistics_id` ASC),
  INDEX `fk_player_tech_statistics_result1_idx` (`result_result_id` ASC),
  CONSTRAINT `fk_player_tech_statistics_result1`
    FOREIGN KEY (`result_result_id`)
    REFERENCES `mydb`.`result` (`result_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'player technical statistics data'
