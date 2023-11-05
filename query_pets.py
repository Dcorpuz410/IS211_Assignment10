import sqlite3

conn = sqlite3.connect('pets.db')

cur = conn.cursor()


def get_user():
    with conn:

        id = ''

        while id != '-1':
            try:
                id = input("Enter an ID #:")
                if id == '-1':
                    print('Goodbye.')
                    break
                else:
                    cur.execute('''
                    SELECT ppl.first_name, 
                    ppl.last_name,
                    ppl.age, 
                    p.name,
                    p.age,
                    p.dead
                    FROM people_pets pp
                    LEFT JOIN pets p
                    ON pp.pet = p.id
                    LEFT JOIN people ppl
                    ON pp.person = ppl.id
                    WHERE ppl.id == ?''', id)

                    results = cur.fetchall()
                    if len(results) > 0:
                        for r in results:
                            print(f'{r[0]} {r[1]}, {r[2]} years old:')
                            if r[5] == 0:
                                print(f'{r[0]} {r[1]} owned {r[3]} — who was {r[4]} years old.')
                            else:
                                print(f'{r[0]} {r[1]} owns {r[3]} — who is {r[4]} years old.')

                    else:
                        print('No users found with that ID. Please try again.')
            except:
                print('Invalid entry. Please try again.')


if __name__ == "__main__":
    get_user()