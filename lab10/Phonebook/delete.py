import psycopg2


def delete():
    c = psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="87087214958adiya",
        host="localhost",
        port="5432"
    )
    cur = c.cursor()

    choice = input("Choose 1(Name) or 2(Phone number) to delete by this element: ")

    if choice == "1":
        name = input("Write name of contact to delete: ")
        cur.execute("""
            DELETE FROM contacts
            WHERE name = %s;
        """, (name,))
        print(f"Contact {name} deleted .")

    elif choice == "2":
        phone = input("Write phone number of contact to delete: ")
        cur.execute("""
            DELETE FROM contacts
            WHERE phone_number = %s;
        """, (phone,))
        print(f"Contact with phone number {phone} deleted .")

    else:
        print("Only choose 1 or 2")

    c.commit()
    cur.close()
    c.close()
delete()
