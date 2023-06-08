import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="disprojektdata",
    user="tobiasrasmussen",
    password="dis123"
)