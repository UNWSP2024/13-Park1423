##
# --Display Cities database--
# by Parker Jolly and Tony Gaddis
# 12/5/2025
# Code adapted from Tony's create_cities_db.py by Parker
##

import sqlite3

# The display_cities function displays the contents of the Cities table.
def display_cities(cur):
    # Header
    print('Contents of cities.db/Cities table:')
    # Select all
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    # Print selected
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

if __name__ == "__main__":
    # Connect to the database and create cursor
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    # Call function
    display_cities(cur)

    # Close file
    conn.close()