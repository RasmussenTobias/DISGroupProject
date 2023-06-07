import psycopg2
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="disProjektData",
    user="samuelcadell",
    password="dis123"
)
cur = conn.cursor()