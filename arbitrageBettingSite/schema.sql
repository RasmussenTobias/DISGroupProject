\i schema_drop.sql

CREATE TABLE IF NOT EXISTS logins(
    uId integer PRIMARY KEY,	
    uName varchar(60),
	password varchar(120),	
);

CREATE TABLE IF NOT EXISTS users(
    uId integer PRIMARY KEY,
	name varchar(60),
	surname varchar(60),    
	accessType varchar(60)	
);