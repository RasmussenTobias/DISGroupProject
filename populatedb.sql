drop table if exists users;
drop table if exists liga;
drop table if exists teams;
drop table if exists teamsInLiga;
drop table if exists season;
drop table if exists matches;

create table users(
    username varchar(20),
    password varchar(20),
    primary key (username)
);

create table liga(
    ligaName varchar(50),
    primary key (ligaName)
);

create table teams(
    id varchar(20),
    teamName varchar(50)
);

COPY teams FROM '/Users/samuelcadell/Desktop/DISGroupProject-main/processedData/uniqTeams.csv' DELIMITER ',' CSV HEADER;
alter table teams drop column id;

insert into liga (ligaName) values('Premier League'),
                            ('Championship'),
                            ('League 1'),
                            ('League 2'),
                            ('Conference');

create table teamsInLiga(
    teamName varchar(50),
    ligaName varchar(50),
    primary key(teamName,ligaName)
);

create table season(
    id varchar(30),
    year varchar(10),
    datePlayed DATE,
    playingTeams varchar(100),
    ligaName varchar(50),
    primary key (datePlayed,playingTeams,ligaName)
);

create table matches(
    datePlayed DATE,
    playingTeams varchar(100)
);


copy season from '/Users/samuelcadell/Desktop/DISGroupProject-main/processedData/seasonsGames.csv' delimiter ',' csv header;
alter table season drop column id;
