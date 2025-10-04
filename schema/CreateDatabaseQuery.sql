CREATE DATABASE HousePointsManagementSystem;

CREATE TABLE `Users` (
  `Id` int PRIMARY KEY,
  `Username` char(15) NOT NULL,
  `Password` char(15) NOT NULL,
  `Role` varchar(10) DEFAULT "User"
);

CREATE TABLE `Houses` (
  `Id` int PRIMARY KEY,
  `Name` varchar(20) NOT NULL,
  `Points` int DEFAULT 0
);

CREATE TABLE `StudentGroup` (
  `Id` int PRIMARY KEY,
  `Name` varchar(20) NOT NULL
);

CREATE TABLE `Students` (
  `Id` char(7) PRIMARY KEY,
  `AdmissionNo` char(12),
  `Name` varchar(50) NOT NULL,
  `House` varchar(20) NOT NULL,
  `Points` int DEFAULT 0
);

CREATE TABLE `Events` (
  `Id` int PRIMARY KEY,
  `Name` varchar(50) NOT NULL,
  `HeldOn` date NOT NULL,
  `StudentGroup` varchar(20) NOT NULL,
  `Type` varchar(20),
  `Organiser` varchar(50),
  `FirstPositionHouse` varchar(20),
  `SecondPositionHouse` varchar(20),
  `ThirdPositionHouse` varchar(20),
  `FourthPositionHouse` varchar(20)
);

CREATE TABLE `Participations` (
  `Id` int PRIMARY KEY,
  `EventId` int NOT NULL,
  `StudentId` CHAR(7) NOT NULL,
  `PointsAwarded` int NOT NULL
);

ALTER TABLE `Students` ADD FOREIGN KEY (`House`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`StudentGroup`) REFERENCES `StudentGroup` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`FirstPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`SecondPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`ThirdPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`FourthPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Participations` ADD FOREIGN KEY (`EventId`) REFERENCES `Events` (`Id`);

ALTER TABLE `Participations` ADD FOREIGN KEY (`StudentId`) REFERENCES `Students` (`Id`);
