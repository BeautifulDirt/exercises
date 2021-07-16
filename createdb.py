import sqlite3

connection = sqlite3.connect('users1.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (id INTEGER, name TEXT, email TEXT, is_verified BOOL)''')
connection.commit()
cursor.execute('''INSERT INTO users
                        (id, name, email, is_verified)
                        VALUES
                        (1111, 'ivanov', 'ivanov@mail.ru', 'true')''')
f = connection.commit()
print(f)
connection.close()