CREATE TABLE `Houses` (
  `Id` int PRIMARY KEY,
  `Name` varchar(20),
  `Points` int
);

CREATE TABLE `StudentGroup` (
  `Id` int PRIMARY KEY,
  `Name` varchar(20)
);

CREATE TABLE `Students` (
  `Id` char(7) PRIMARY KEY,
  `AdmissionNo` char(12),
  `Name` varchar(50),
  `House` varchar(20),
  `Points` int
);

CREATE TABLE `Events` (
  `Id` int PRIMARY KEY,
  `Name` varchar(50),
  `HeldOn` date,
  `StudentGroup` varchar(20),
  `Type` varchar(20),
  `Organiser` varchar(50),
  `FirstPositionHouse` varchar(20),
  `SecondPositionHouse` varchar(20),
  `ThirdPositionHouse` varchar(20),
  `FourthPositionHouse` varchar(20)
);

CREATE TABLE `Participations` (
  `Id` int PRIMARY KEY,
  `EventId` int,
  `StudentId` int,
  `PointsAwarded` int
);

ALTER TABLE `Students` ADD FOREIGN KEY (`House`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`StudentGroup`) REFERENCES `StudentGroup` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`FirstPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`SecondPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`ThirdPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Events` ADD FOREIGN KEY (`FourthPositionHouse`) REFERENCES `Houses` (`Id`);

ALTER TABLE `Participations` ADD FOREIGN KEY (`EventId`) REFERENCES `Events` (`Id`);

ALTER TABLE `Participations` ADD FOREIGN KEY (`StudentId`) REFERENCES `Students` (`Id`);
