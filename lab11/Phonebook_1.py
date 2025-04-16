import psycopg2
import re


def connect():
    config = psycopg2.connect(
        host='localhost',
        database='suppliers',
        user='postgres',
        password='87087214958adiya'
    )
    cursor = config.cursor()
    return config, cursor


def return_all():
    conn, cur = connect()

    sql = '''SELECT id, name, phone_number FROM contacts ORDER BY id;'''

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    cur.close()
    conn.close()
print(return_all())

def search_contacts(pattern):
    config, cursor = connect()
    pattern = f"%{pattern}%"

    sql = """
        SELECT * FROM contacts
        WHERE name ILIKE %s OR
              phone_number ILIKE %s
    """
    cursor.execute(sql, (pattern, pattern))
    results = cursor.fetchall()

    cursor.close()
    config.close()
    return results

print(search_contacts("nur"))

def insert_update_user(id, name, number):
    config, cursor = connect()

    cursor.execute("SELECT COUNT(*) FROM contacts WHERE name = %s", (name,))
    user_count = cursor.fetchone()[0]

    if user_count == 0:
        cursor.execute("INSERT INTO contacts (id,name, phone_number) VALUES (%s,%s, %s)", (id, name, number))
        print(f"Added user {name} with phone number {number}.")

    else:
        cursor.execute("UPDATE contacts SET phone_number = %s WHERE name = %s", (number, name))
        print(f"Phone number for user {name} updated to {number}.")

    config.commit()
    cursor.close()
    config.close()

print(insert_update_user(4,'Adiya', '87087255588'))



def is_valid_phone(phone):
    return (
            re.fullmatch(r'87\d{9}', phone) or
            re.fullmatch(r'\+77\d{9}', phone) or
            re.fullmatch(r'7\d{9}', phone)
    )


def insert_users(names, phones):
    incorrect_phones = []
    config, cursor = connect()

    for name, phone in zip(names, phones):
        if is_valid_phone(phone):
            cursor.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (name, phone))
        else:
            incorrect_phones.append((name, phone))

    config.commit()
    cursor.close()
    config.close()
    return incorrect_phones


names = ["Adi", "Kama", "Non"]
phones = ["87076039179", "7777777777777777777777777", "7777777777777777777777777"]
bad = insert_users(names, phones)
print("Uncorrect: ", bad)


def pagination(table_name, limit, offset):
    config, cursor = connect()

    cursor.execute(f"SELECT * FROM {table_name} ORDER BY id ASC LIMIT {limit} OFFSET {offset};")
    rows = cursor.fetchall()

    cursor.close()
    config.close()

    return rows

print(pagination('contacts',3,2))

def delete(name=None, number=None):
    config, cursor = connect()

    if name is not None:
        cursor.execute("DELETE FROM contacts WHERE name = %s;", (name,))

    elif number is not None:
        cursor.execute("DELETE FROM contacts WHERE phone_number = %s;", (number,))

    else:
        raise ValueError("write phone number or name ")

    config.commit()
    cursor.close()
    config.close()
print(delete("Nazym"))
