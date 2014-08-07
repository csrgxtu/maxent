CREATE TABLE `player_role` (
  `player_role_id` INT NOT NULL,
  `name` VARCHAR(255) NULL COMMENT 'name of the role',
  `name_cn` VARCHAR(255) NULL,
  `create_time` DATETIME NULL,
  `create_by` VARCHAR(255) NULL,
  `update_time` DATETIME NULL,
  `update_by` VARCHAR(255) NULL,
  PRIMARY KEY (`player_role_id`)
)
