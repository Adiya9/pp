import psycopg2
import csv

def get_from_csv(file):
    c = psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="87087214958adiya",
        host="localhost",
        port="5432"
    )
    cur = c.cursor()

    with open(file, newline='') as csvfile:
        read = csv.DictReader(csvfile)
        for i in read:
            print(f"Inserted: {i['name']}, {i['phone_number']}")
            cur.execute("""
                INSERT INTO contacts (name, phone_number)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING;
            """, (i['name'], i['phone_number']))

    c.commit()
    cur.close()
    c.close()

get_from_csv("contacts.csv")
