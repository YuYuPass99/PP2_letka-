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


def load_sql_file(filepath):
    """Execute a .sql file (creates functions/procedures in DB)."""
    conn = connect()
    cur = conn.cursor()
    with open(filepath, 'r') as f:
        sql = f.read()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Loaded: {filepath}")


# ── INSERT ────────────────────────────────────────────────────────────────────

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
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


# ── UPSERT (procedure) ────────────────────────────────────────────────────────

def upsert_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Done: '{name}' saved.")


def insert_many():
    """Insert multiple users at once; invalid phones are printed."""
    print("Enter name,phone pairs. Empty name to finish.")
    names = []
    phones = []
    while True:
        name = input("  Name (or Enter to stop): ")
        if not name:
            break
        phone = input("  Phone: ")
        names.append(name)
        phones.append(phone)

    if not names:
        print("Nothing to insert.")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CALL insert_many_users(%s::varchar[], %s::varchar[], NULL)",
        (names, phones)
    )
    # OUT parameter comes back as a result row
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if result:
        print("\nInvalid entries:")
        print(result[0])


# ── UPDATE ────────────────────────────────────────────────────────────────────

def update_contact():
    name = input("Current name: ")
    new_name = input("New name (Enter to skip): ") or None
    new_phone = input("New phone (Enter to skip): ") or None
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()


# ── SEARCH ────────────────────────────────────────────────────────────────────

def search_by_pattern():
    pattern = input("Enter pattern (part of name or phone): ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if rows:
        for row in rows:
            print(f"  ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    else:
        print("No results.")


def get_paginated():
    limit = int(input("Records per page: "))
    offset = int(input("Skip (offset): "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if rows:
        for row in rows:
            print(f"  ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    else:
        print("No results.")


# ── DELETE ────────────────────────────────────────────────────────────────────

def delete_contact():
    print("Delete by: 1) Name  2) Phone")
    choice = input("Choose: ")
    conn = connect()
    cur = conn.cursor()
    if choice == "1":
        name = input("Name: ")
        cur.execute("CALL delete_contact(p_name => %s)", (name,))
    elif choice == "2":
        phone = input("Phone: ")
        cur.execute("CALL delete_contact(p_phone => %s)", (phone,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")


def clear_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE phonebook RESTART IDENTITY;")
    conn.commit()
    cur.close()
    conn.close()
    print("All contacts deleted, ID counter reset.")


def show_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if rows:
        for row in rows:
            print(f"  ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    else:
        print("Phonebook is empty.")


# ── MENU ──────────────────────────────────────────────────────────────────────

def menu():
    create_table()
    # Load functions and procedures into DB on first run
    load_sql_file("functions.sql")
    load_sql_file("procedures.sql")

    while True:
        print("\n=== PhoneBook ===")
        print("1.  Add from console")
        print("2.  Add from CSV")
        print("3.  Upsert contact (insert or update)")
        print("4.  Insert many users")
        print("5.  Update contact")
        print("6.  Search by pattern")
        print("7.  Get paginated")
        print("8.  Show all")
        print("9.  Delete contact")
        print("10. Clear all")
        print("0.  Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            upsert_contact()
        elif choice == "4":
            insert_many()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            search_by_pattern()
        elif choice == "7":
            get_paginated()
        elif choice == "8":
            show_all()
        elif choice == "9":
            delete_contact()
        elif choice == "10":
            clear_all()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()
