import psycopg2

def get_from_console():
    c = psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="87087214958adiya",
        host="localhost",
        port="5432"
    )
    cur = c.cursor()

    while True:
        name = input("Write name (write 'exit' to stop): ")
        if name.lower() == 'exit':
            break

        phone = input("Write phone number: ")
        print(f"Inserted: Name = {name}, Phone = {phone}")

        try:
            cur.execute("""
                INSERT INTO contacts (name, phone_number)
                VALUES (%s, %s);
            """, (name, phone))

            c.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")

    cur.close()
    c.close()
get_from_console()
