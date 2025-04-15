import psycopg2
def query_contacts():
    c = psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="87087214958adiya",
        host="localhost",
        port="5432"
    )

    cur = c.cursor()

    print("Select the type of query you want to perform:")
    print("1. Get all contacts")
    print("2. Find contact by name")
    print("3. Find contact by phone number")
    print("4. Order contacts by name")
    print("5. Get contacts whose name starts with a specific letter")

    num = input("Write number to execute query ")

    if num == '1':
        cur.execute("SELECT * FROM contacts;")
        res = cur.fetchall()
        print("All contacts:")
        for i in res:
            print(i)

    elif num == '2':
        name = input("Write the exact name: ")
        cur.execute("SELECT * FROM contacts WHERE name = %s;", (name,))
        res = cur.fetchall()
        print(f"Contacts with name '{name}':")
        for i in res:
            print(i)

    elif num == '3':
        phone_number = input("Write the phone number: ")
        cur.execute("SELECT * FROM contacts WHERE phone_number = %s;", (phone_number,))
        res = cur.fetchall()
        print(f"Contacts with phone number '{phone_number}':")
        for i in res:
            print(i)

    elif num == '4':
        cur.execute("SELECT * FROM contacts ORDER BY name ASC;")
        res = cur.fetchall()
        print("Contacts ordered by name:")
        for i in res:
            print(i)

    elif num == '5':
        letter = input("Write the starting letter of the name: ")
        cur.execute("SELECT * FROM contacts WHERE name LIKE %s;", (letter + '%',))
        res = cur.fetchall()
        print(f"Contacts whose name starts with '{letter}':")
        for i in res:
            print(res)

    else:
        print("Choose num from 1 to 5")
    c.commit()
    cur.close()
    c.close()

query_contacts()
