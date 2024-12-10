-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema examen
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `examen` ;

-- -----------------------------------------------------
-- Schema examen
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `examen` DEFAULT CHARACTER SET utf8 ;
USE `examen` ;

-- -----------------------------------------------------
-- Table `examen`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `examen`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `fecha_de_inicio` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `examen`.`parques`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `examen`.`parques` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `ubicacion` VARCHAR(45) NULL,
  `descripcion` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `examen`.`visitas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `examen`.`visitas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `parque_id` INT NULL,
  `usuario_id` INT NULL,
  `fecha_de_visita` DATETIME NOT NULL,
  `rating` INT NULL,
  `acciones` TEXT NULL,
  `visitascol` VARCHAR(45) NULL,
  `usuario_id` INT NOT NULL,
  `parque_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_visitas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_visitas_parques1_idx` (`parque_id` ASC) VISIBLE,
  CONSTRAINT `fk_visitas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `examen`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_visitas_parques1`
    FOREIGN KEY (`parque_id`)
    REFERENCES `examen`.`parques` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
