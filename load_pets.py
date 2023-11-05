import sqlite3

conn = sqlite3.connect('pets.db') #connect to the database

cur = conn.cursor() #once you have a cursor you can start executing sql commnands

data = {

    'people' : [(1, 'James', 'Smith', 41), (2, 'Diana', 'Greene', 23), (3, 'Sara', 'White', 27), (4, 'William', 'Gibson', 23)],
    'pets' : [(1, 'Rusty', 'Dalmation', 4, 1), (2, 'Bella', 'Alaskan Malamute', 3, 0), (3, 'Max', 'Cocker Spaniel', 1, 0), (4, 'Rocky', 'Beagle', 7, 0), (5, 'Rufus', 'Cocker Spaniel', 1, 0), (6, 'Spot', 'Bloodhound', 2, 1)],
    'people_pets' : [(1,1),(1,2),(2,3),(2,4),(3,5),(4,6)]}

cur.execute('''CREATE TABLE IF NOT EXISTS people
            (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)''')

cur.execute('''CREATE TABLE IF NOT EXISTS pets
            (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)''')

cur.execute('''CREATE TABLE IF NOT EXISTS people_pets
            (person INTEGER, pet INTEGER)''')

conn.commit()

if __name__ == "__main__":

    for d in range(len(data['people'])):
        cur.execute('INSERT INTO people VALUES (?,?,?,?)', data['people'][d])

    for d in range(len(data['pets'])):
        cur.execute('INSERT INTO pets VALUES (?,?,?,?,?)', data['pets'][d])

    for d in range(len(data['people_pets'])):
        cur.execute('INSERT INTO people_pets VALUES (?,?)', data['people_pets'][d])

    conn.commit()

    conn.close()