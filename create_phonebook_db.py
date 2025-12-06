##
# --Create Phone Database
# by Parker Jolly and Tony Gaddis
# 12/5/2025
# Adapted from Tony Gaddis create_cities_db.py
##


import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the phonebook table.
    add_phonebook_table(cur)
    
    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()

# The add_phonebook_table adds the phonebook table to the database.
def add_phonebook_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS phonebook')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (Name TEXT PRIMARY KEY NOT NULL,
                                        Number INTEGER)''')

# Execute the main function.
if __name__ == '__main__':
    main()
