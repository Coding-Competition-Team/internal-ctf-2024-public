from flask import Flask, request, make_response, redirect, url_for
from hashlib import sha256

flag = open("flag.txt", 'r')

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>CREATE ACCOUNT</h1>
    <form action="/createAcc" method="post">
        <input type="text" name="username" placeholder="username">
        <br><br>
        <input type="password" name="password" placeholder="password">
        <br><br>
        <input type="submit" href="/authentication" value="Create">
    </form>
    """

@app.route('/createAcc', methods=['POST'])
def login():
    resp = make_response("""
    <h1>Authentication</h1>
    <form action="/authentication" method="post">
        <input type="submit" value="authenticate (100% secure)">
    </form>
""")  
    if (request.form['password']!='admin' and request.form['username']!='admin'):
        password=sha256(request.form['password'].encode('utf-8')).hexdigest()
        resp.set_cookie('username', 'bar', max_age=0)
        resp.set_cookie('password', 'bar', max_age=0)
        resp.set_cookie('username',f"'{request.form['username']}'") 
        resp.set_cookie('password',f"'{password}'") 
        return resp
    else:
        return redirect('/')

@app.route('/authentication', methods=['POST'])
def authentication():
    user = request.cookies.get('username').replace("'","")
    pw = request.cookies.get('password').replace("'","")
    plain='admin';
    plain=sha256(plain.encode('utf-8')).hexdigest()
    if (pw==plain and user=='admin'):
        return f"<h1>{flag.read()}</h1>"
    else:
        return """    
        <h1>You didnt log in</h1>
        <a href="/"><input type="submit" value="Try again"></a>
        """
    
app.run()