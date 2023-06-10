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
    Teams varchar(50)
);

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