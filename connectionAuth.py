import psycopg2

myHost = "localhost"
myPort = "5432"
myDbName = "disprojektdata"
myUser = "tobiasrasmussen"
myPassword = "dis123"
conn = psycopg2.connect(
    host=myHost,
    port=myPort,
    dbname=myDbName,
    user=myUser,
    password=myPassword
)

print(f"username={myUser}")
print(f"database={myDbName}")
print(f"host={myHost}")
print(f"port={myPort}")