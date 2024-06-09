from flask import Flask, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE users (username TEXT, password TEXT)')
    conn.execute('INSERT INTO users (username, password) VALUES ("admin", "ACSI{p0k1ng_bl1nd_1n_th3_d4rk}")')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return """
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="username">
        <input type="password" name="password" placeholder="password">
        <input type="submit">
    </form>
    """

@app.route('/login', methods=['POST'])
def login():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{request.form['username']}' AND password='{request.form['password']}'")
    result = cursor.fetchone()
    conn.close()
    if result:
        return 'Login success!'
    else:
        return 'Login failed!'