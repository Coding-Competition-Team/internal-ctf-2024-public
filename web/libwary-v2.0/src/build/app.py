from flask import Flask, request, render_template, redirect, url_for, make_response
import sqlite3
import os
from uuid import uuid4

def init_db():
  conn = sqlite3.connect('database.db')
  cur = conn.cursor()
  cur.execute('CREATE TABLE IF NOT EXISTS loans (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, credit INTEGER)')
  cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, session TEXT, credit INTEGER)')
  conn.commit()

def get_user(session: str):
  conn = sqlite3.connect('database.db')
  cur = conn.cursor()
  cur.execute("SELECT * FROM users WHERE session = ?", (session,))
  user = cur.fetchone()
  return user

app = Flask(__name__)
init_db()

@app.route('/')
def index():
  session = request.cookies.get('session')
  user = get_user(session)
  return render_template('index.html', user=user) if user else render_template('index.html', user=False)

@app.route('/auth', methods=['POST'])
def auth():
  session = request.cookies.get('session')
  if session:
    return redirect(url_for('index'))
  
  username = request.form['username']
  password = request.form['password']
  conn = sqlite3.connect('database.db')
  cur = conn.cursor()
  try:
    session = uuid4().hex
    cur.execute("INSERT INTO users (username, password, session, credit) VALUES (?, ?, ?, ?)", (username, password, session, 10))
    conn.commit()
    response = make_response(redirect(url_for('index')))
    response.set_cookie('session', session)
    return response

  except sqlite3.IntegrityError:
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()
    if user:
      session = uuid4().hex
      cur.execute("UPDATE users SET session = ? WHERE username = ?", (session, username))
      conn.commit()
      response = make_response(redirect(url_for('index')))
      response.set_cookie('session', session)
      return response
    else:
      return redirect(url_for('index')) # Either wrong username or password, or username already exists
    
@app.route('/read')
def read():
  session = request.cookies.get('session')
  user = get_user(session)
  if not user:
    return redirect(url_for('index')) 

  allowed = ['mb1', 'mb2', 'mb3', 'mb4', 'mb5', 'rj1', 'rj2', 'rj3', 'rj4', 'rj5', 'flag']

  book = request.args.get('book')
  if book is None:
    return redirect(url_for('index'))
  if book not in allowed:
    return redirect(url_for('index'))
  if book == 'flag':
    return render_template('read.html', error="Access Denied: You are not allowed to read the flag.", size=16, theme="light")

  for key, value in request.args.items(multi=True):
    if key == 'book':
      book = "templates/" + value + ".txt"
      if '..' in book:
        return redirect(url_for('index'))

      requiredcredits = 1000 if value == 'flag' else 10
      if user[4] < requiredcredits:
        return render_template('read.html', error="Insufficient credits, try returning a book. If you reloaded, return and read again.", size=16, theme="light")
      
      conn = sqlite3.connect('database.db')
      cur = conn.cursor()
      cur.execute("SELECT credit FROM users WHERE session = ?", (session,))
      credits = cur.fetchone()[0] - requiredcredits

      cur.execute("UPDATE users SET credit = ? WHERE session = ?", (credits, session))
      cur.execute("INSERT INTO loans (user_id, credit) VALUES (?, ?)", (user[0], requiredcredits))
      conn.commit()

      try:
        with open(book, 'r') as f:
          content = f.read()
      except:
        content = "Error: File not found"

    if key == 'size':
        try:
          value = int(value)
        except:
          value = 16

        size = value if (value < 100 and value > 4) else 16

    if key == 'theme':
      if value == 'light':
        theme = "light"
      elif value == 'dark':
        theme = "dark"
      else:
        theme = "light"
        
  return render_template('read.html', content=content, size=size, theme=theme)

@app.route('/return')
def returnall():
  session = request.cookies.get('session')
  user = get_user(session)
  if not user:
    return redirect(url_for('index')) 
  
  torefund = 0
  conn = sqlite3.connect('database.db')
  cur = conn.cursor()
  cur.execute("SELECT credit FROM loans WHERE user_id = ?", (user[0],))
  torefund += sum([x[0] for x in cur.fetchall()])
  cur.execute("DELETE FROM loans WHERE user_id = ?", (user[0],))
  cur.execute("UPDATE users SET credit = credit + ? WHERE session = ?", (torefund, session))
  conn.commit()

  return redirect(url_for('index'))

app.run(debug=True)