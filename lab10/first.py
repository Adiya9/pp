import psycopg2

c = psycopg2.connect(
    dbname = "suppliers",
    user="postgres",
    password="87087214958adiya",
    host="localhost",
    port="5432"
)

cur = c.cursor()

cur.execute("DROP TABLE IF EXISTS contacts;")
cur.execute("""
CREATE TABLE contacts (

    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone_number VARCHAR(11) 
);
""")

c.commit()
cur.close()
c.close()
