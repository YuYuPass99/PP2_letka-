import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()

def update_contact(name, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE phonebook SET name=%s WHERE name=%s",
            (new_name, name)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE name=%s",
            (new_phone, name)
        )

    conn.commit()
    cur.close()
    conn.close()

def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE name=%s", (name,))
    print(cur.fetchall())

    cur.close()
    conn.close()

def search_by_prefix(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + "%",))
    print(cur.fetchall())

    cur.close()
    conn.close()

def delete_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()

    cur.close()
    conn.close()

def delete_by_phone(phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.commit()

    cur.close()
    conn.close()

def clear_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE phonebook RESTART IDENTITY;")
    conn.commit()

    cur.close()
    conn.close()
    print("All contacts deleted, ID counter reset.")


def menu():
    create_table()

    while True:
        print("\n1. Add from console")
        print("2. Add from CSV")
        print("3. Update contact")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Delete by name")
        print("7. Delete by phone")
        print("8. Clear all contacts")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            name = input("Old name: ")
            new_name = input("New name (or Enter): ")
            new_phone = input("New phone (or Enter): ")
            update_contact(name, new_name or None, new_phone or None)
        elif choice == "4":
            search_by_name(input("Name: "))
        elif choice == "5":
            search_by_prefix(input("Prefix: "))
        elif choice == "6":
            delete_by_name(input("Name: "))
        elif choice == "7":
            delete_by_phone(input("Phone: "))
        elif choice == "8":          
            clear_all()
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()