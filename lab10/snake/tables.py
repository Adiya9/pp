import psycopg2

c = psycopg2.connect(
    dbname = "suppliers1",
    user="postgres",
    password="87087214958adiya",
    host="localhost",
    port="5432"
)

cur = c.cursor()

cur.execute("DROP TABLE IF EXISTS snake;")
cur.execute("""
CREATE TABLE snake(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(50),
    score INTEGER,
    level INTEGER,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

c.commit()
cur.close()
c.close()
