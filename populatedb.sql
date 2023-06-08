drop table if exists users;
drop table if exists liga;
drop table if exists teams;
drop table if exists teamsInLiga;
drop table if exists season;
drop table if exists matches;
drop table if exists bookmakers;
drop table if exists odds;

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


create table season(
    id varchar(30),
    year varchar(10),
    datePlayed varchar(10),
    playingTeams varchar(100),
    ligaName varchar(50),
    primary key (datePlayed,playingTeams,ligaName)
);

create table matches(
    datePlayed varchar(10),
    playingTeams varchar(100)
);


copy season from '/Users/samuelcadell/Desktop/DISGroupProject-main/processedData/seasonsGames.csv' delimiter ',' csv header;
alter table season drop column id;

copy matches from '/Users/samuelcadell/Desktop/DISGroupProject-main/processedData/matches.csv' delimiter ',' csv header;

create table bookmakers(
    bookmaker varchar(20)
);

create table odds(
    bookmaker varchar(20),
    date varchar(10),
    playingTeams varchar(100),
    home float(10), 
    draw float(10),
    away float(10)
);

insert into bookmakers (bookmaker) values('bet365'),
                                    ('Blue_square'),
                                    ('BetAndWin'),
                                    ('GameBookers'),
                                    ('Interwetten'),
                                    ('Ladbrokes'),
                                    ('Pinnacle'),
                                    ('SportingOdds'),
                                    ('SportingBet'),
                                    ('StanJames'),
                                    ('StanleyBet'),
                                    ('VC'),
                                    ('WilliamHill');

copy odds from '/Users/samuelcadell/Desktop/DISGroupProject-main/data/preprocessing/odds_formatted.csv' delimiter ',' csv header;

