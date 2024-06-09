from flask import Flask, request, render_template, render_template_string, redirect
import sqlite3
from uuid import uuid4
import re
import subprocess

phone_regex = r'\+\d{5,20}'
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS reports (id TEXT PRIMARY KEY, data TEXT, description TEXT)')
    conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def handle():
    data = request.form['data']
    description = request.form['description']
    uuid = str(uuid4())

    if not (re.search(phone_regex, data) or re.search(email_regex, data)):
        return render_template('index.html', error='Data must contain a phone number or email')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO reports (id, data, description) VALUES (?, ?, ?)', (uuid, data, description))
    conn.commit()

    return redirect(f'/report/{uuid}')

@app.route('/report/<uuid>')
def view(uuid):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reports WHERE id = ?', (uuid,))
    report = c.fetchone()

    if report is None:
        return render_template('index.html', error='Report not found')

    out = render_template_string('''
    <h1>Report</h1>
    <p>Data: {data}</p>
    <p>Description: {description}</p>
    '''
    .format(data=report[1], description=report[2]))

    if "ACSI" in out:
        return render_template('index.html', error='NO HACKING!')
    return out
