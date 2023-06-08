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

COPY teams FROM 'C:\Users\rasmu\OneDrive - University of Copenhagen\Uni\DIS\DISGroupProject\processedData\uniqTeams.csv' DELIMITER ',' CSV HEADER;
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

create table matchStats(
    datePlayed DATE,
    playingTeams varchar(50),
    fthg varchar(50),
    ftag varchar(50),
    attendance varchar(50),
    refferee varchar(50),
    homeshots varchar(50),
    awayshot varchar(50),
    hshotsontarget varchar(50),
    ashotsontarget varchar(50),
    hhitwoodwork varchar(50),
    ahitwoodwork varchar(50),
    hcorners varchar(50),
    acorners varchar(50),
    hfouls varchar(50),
    afouls varchar(50),
    hfreekicks varchar(50),
    afreekicks varchar(50),
    hoffsides varchar(50),
    aoffsides varchar(50),
    hyellow varchar(50),
    ayellow varchar(50),
    hred varchar(50),
    ared varchar(50),
    hblockingpoints varchar(50),
    ablockingpoints varchar(50),
    primary key(datePlayed,playingTeams)
);

copy season from 'C:\Users\rasmu\OneDrive - University of Copenhagen\Uni\DIS\DISGroupProject\processedData\seasonsGames.csv' delimiter ',' csv header;
alter table season drop column id;
