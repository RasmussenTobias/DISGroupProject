drop table if exists users;
drop table if exists liga;
drop table if exists teams;
drop table if exists teamsInLiga;
drop table if exists season;
drop table if exists matches;
drop table if exists bookmakers;
drop table if exists odds;
drop table if exists matchstats;

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


create table matchstats(
    id varchar(30),
    datePlayed varchar(50),
    playingTeams varchar(50),
    fthg varchar(50),
    ftag varchar(50),
    attendance varchar(50),
    refferee varchar(50),
    homeshots varchar(50),
    awayshots varchar(50),
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
    primary key(datePlayed,playingTeams)
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


COPY teams FROM '/processedData/uniqTeams.csv' DELIMITER ',' CSV HEADER;
ALTER TABLE teams DROP COLUMN id;

COPY season FROM '/processedData/seasonsGames.csv' DELIMITER ',' CSV HEADER;
ALTER TABLE season DROP COLUMN id;

COPY matches FROM '/processedData/matches.csv' DELIMITER ',' CSV HEADER;

COPY odds FROM 'C:/Users/rasmu/OneDrive - University of Copenhagen/Uni/DIS/DISGroupProject/processedData/gameStats.csv' DELIMITER ',' CSV HEADER;

COPY matchstats FROM '/processedData/gameStats.csv' DELIMITER ',' CSV HEADER;
ALTER TABLE matchstats DROP COLUMN id;
