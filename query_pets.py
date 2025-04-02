import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    person_id = int(input("Enter a person's ID (or -1 to exit): "))
    
    if person_id == -1:
        break
    
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()
    
    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")
        
        cursor.execute("""
            SELECT p.name, p.breed, p.age 
            FROM pet p
            JOIN person_pet pp ON p.id = pp.pet_id
            WHERE pp.person_id = ?
        """, (person_id,))
        
        pets = cursor.fetchall()
        
        if pets:
            for pet in pets:
                print(f"{person[0]} {person[1]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
        else:
            print(f"{person[0]} {person[1]} has no pets.")
    else:
        print("Error: Person not found.")
    
    print()

conn.close()
