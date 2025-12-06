##
# --Program 4--
# by Parker Jolly
# 12/5/2025
# Read, write, and delete entries in the phonebook database
##


import sqlite3

# Connect and create cursor
conn = sqlite3.connect("phonebook.db")
cur = sqlite3.Cursor(conn)

def main():
    while True:

        # Options menu
        option = input("""
Select an option:
  1) Read Database
  2) Write to Database
  3) Delete Database entry
  4) Exit Program
=====>""")
        
        # Check input and run corrisponding file, or tell the user their input was bad
        if option.strip() == "1":
            option_1()
        elif option.strip() == "2":
            option_2()
        elif option.strip() == "3":
            option_3()
        elif option.strip() == "4":
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

    # Close file and giver user output
    print("Exiting program...")
    conn.commit()
    conn.close()    
    

def option_1():
    # Bunch of header print statements
    print(" ")
    print('Contents of phonebook.db/Entries table:')
    print('Name                    Number')
    print('**********************************************************************************************************************')

    # Select all
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    # Print selected
    for row in results:
        print(f'{row[0]:20}    {row[1]:0}')
    print('**********************************************************************************************************************')


def option_2():
    # Get 2 inputs
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    # Put them into the database
    cur.execute('''INSERT INTO Entries (Name, Number)
                       VALUES (?, ?)''', (name, number))


def option_3():
    # Get number input
    number = input("Enter the number of entry you want to delete: ")

    # Select all entries with that number
    cur.execute("SELECT rowid FROM Entries WHERE number = ?", (number,))
    data = cur.fetchall()
    # If there were none, tell the user, otherwise delete the entry and tell us we deleted it.
    if len(data)==0:
        print(f'There is no entry with the number "{number}"')
    else:
        print(f'Entry with number "{number}" found and removed')
        cur.execute("delete from Entries where Number=(?)", (number, ))

# Call main function
if __name__ == "__main__":
    main()
