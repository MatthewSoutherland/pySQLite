import sqlite3

# Query the DB and return all records


def show_all():
    # Connect to database
    conn = sqlite3.connect('specs.db')

    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM drillSizes")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()

    # Close our connection
    conn.close()


# Add a new record to the table
def add_one(drill, size):
    conn = sqlite3.connect('specs.db')
    c = conn.cursor()
    c.execute("INSERT INTO drillSizes VALUES (?, ?)", (drill, size))
    conn.commit()
    conn.close()


# Add many new records to table
def add_many(list):
    conn = sqlite3.connect('specs.db')
    c = conn.cursor()
    c.executemany("INSERT INTO drillSizes VALUES (?, ?)", (list))
    conn.commit()
    conn.close()


# Delete record from database
def delete_one(id):
    conn = sqlite3.connect('specs.db')
    c = conn.cursor()
    c.execute("DELETE FROM drillSizes WHERE rowid = (?)", id)
    conn.commit()
    conn.close()
