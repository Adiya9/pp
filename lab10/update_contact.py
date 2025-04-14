import psycopg2

def update_contact():
    c = psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="87087214958adiya",
        host="localhost",
        port="5432"
    )
    cur = c.cursor()

    id = input("Write ID of contact which you want to change: ")

    print("What do you want to change?")
    print("1. Name")
    print("2. Phone number")
    choice = input("Choose 1 or 2: ")

    if choice == "1":
        new_name = input("Write new name: ")
        cur.execute("""
            UPDATE contacts
            SET name = %s
            WHERE id = %s;
        """, (new_name, id))
    elif choice == "2":
        new_phone = input("Write new phone number  ")
        cur.execute("""
            UPDATE contacts
            SET phone_number = %s
            WHERE id = %s;
        """, (new_phone, id))
    else:
        print("Choose 1 or 2")

    c.commit()
    print("Successfully")
    cur.close()
    c.close()

update_contact()
