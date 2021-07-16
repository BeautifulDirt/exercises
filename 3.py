from os import name
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_pyfile('settings.conf')
app.secret_key = app.config['SECRET_KEY']

# я не поняла существующую структуру хранения данных из задания, поэтому создала свою с полями id, name, email, is_verified
connection = sqlite3.connect('users.db', check_same_thread=False)
cursor = connection.cursor()

@app.route('/users/<user_id>')
def get_user(user_id):
    cursor.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
    info_test = cursor.fetchall()
    if info_test:
        return jsonify(info_test), 200
    else:
        return "user with id=" + user_id + " not found", 404

@app.route('/users/<user_id>/', methods=['PUT'])
def put_user(user_id):
    name = 'sidorov'
    email = 'sidorov@mail.ru'
    is_verified = False
    cursor.execute('''UPDATE users SET name = ?, email = ?, is_verified = ? WHERE id = ?''', (name, email, is_verified, user_id,))
    connection.commit()
    return 'user was updated', 200

@app.route('/users/', methods=['POST'])
def add_user():
    user_id = 1112
    name = 'petrov'
    email = 'petrov@mail.ru'
    is_verified = True
    cursor.execute('''INSERT INTO users (id, name, email, is_verified) VALUES (?, ?, ?, ?)''', (user_id, name, email, is_verified,))
    connection.commit()
    return 'user was added', 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
    connection.commit()
    return  "user with id=" + user_id + " has been delete", 200

if __name__ == '__main__':
    app.run()