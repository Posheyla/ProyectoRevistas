-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema schema_magazines
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema schema_magazines
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schema_magazines` DEFAULT CHARACTER SET utf8 ;
USE `schema_magazines` ;

-- -----------------------------------------------------
-- Table `schema_magazines`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_magazines`.`usuarios` (
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `conf_password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`email`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `schema_magazines`.`revistas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_magazines`.`revistas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `autor` VARCHAR(45) NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `contenido` VARCHAR(255) NOT NULL,
  `usuario_email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_revistas_usuarios_idx` (`usuario_email` ASC) VISIBLE,
  CONSTRAINT `fk_revistas_usuarios`
    FOREIGN KEY (`usuario_email`)
    REFERENCES `schema_magazines`.`usuarios` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


select *
from usuarios





