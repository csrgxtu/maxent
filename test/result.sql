CREATE TABLE `result` (
  `result_id` INT NOT NULL,
  `result` INT NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  PRIMARY KEY (`result_id`),
  UNIQUE INDEX `result_id_UNIQUE` (`result_id` ASC),
  UNIQUE INDEX `result_UNIQUE` (`result` ASC))
ENGINE = InnoDB
COMMENT = 'result of the game'
