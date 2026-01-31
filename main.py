from flask import Flask, render_template
import json
import urllib.request
import re

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def details():
    location = input("Enter the location here: ")
    api_key = 'AQw4sNOX1A9KQf6L5TTn_2Ggsrgc63hY04_h8ps' 
    
    try:
        source = urllib.request.urlopen(
            'https://geocode.search.hereapi.com/v1/geocode?apikey=' + api_key + '&q=' + location
        ).read()

        responseData = json.loads(source)

        data = {
            "latitude": str(responseData['items'][0]['position']['lat']),
            "longitude": str(responseData['items'][0]['position']['lng']),
        }
        return render_template('index.html', data=data, apikey=api_key)
    except (Exception):
        return render_template('index.html', error="Give the correct location")

@app.route('/')
def index():
    return render_template('index.html')

def login():
            msg = ''
            if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']
                mydb = mysql.connector.connect(
                    host="remotemyql.com",
                    user="Rz8hqnldk4",
                    password="nd0wk03xe0"
                    database="Rz8hqnldk4"
             )
def login():
            msg = ''
            if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']
                mydb = mysql.connector.connect(
                    host="remotemyql.com",
                    user="Rz8hqnldk4",
                    password="nd0wk03xe0"
                    database="Rz8hqnldk4"
             )
             mycursor = mydb.cursor()
                mycursor.execute(
                    "SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s",
                    (username, password)
                )
            account = mycursor.fetchone()
           if account:
                print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful')
            return render_template('index.html', msg = msg, name = name, id = id)
            else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('login.html', msg = msg)
            else:
            return render_template('login.html')
            def logout():
                name = ''
                id = ''
                msg = 'Logged out succesfully'
@app.route('/register', methods=['GET', 'POST'])
def register():
       msg = ''
       if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
             username = request.form['username']
             password = request.form['password']
             email = request.form['email']
             mydb = mysql.connector.connect(
                    host='remotemysql.com',
                    user='Rz8hqn1k4',
                    password='nd6w0k03xe0',
                    database='Rz8hqn1k4'
                    )
             mycursor = mydb.cursor()
@app.route('/register',methods=['GET','POST']) # type: ignore GET-open page,POST=submit form

def register():
       msg = ''
       if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
              username = request.form['username']
              password = request.form['password']
              email = request.form['email']
              mydb = mysql.connector.connect(
                     host='remoteysql.com',
                     user='Rz8hqnlk4',
                     password='nd6wK03xe0',
                     database='Rz8hqnlk4'
                     )
              mycursor = mydb.cursor()
              mycursor.execute(
                     'SELECT * FROM LoginDetails WHERE Name=%s AND Email_id=%s',(username, email)
                     )
              account = mycursor.fetchone()
              if account:
                     msg = 'Account already exists!'
              elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                     msg = 'Invalid email address!'
              elif not re.match(r'^[A-Za-z0-9]+$', username):
                     msg = 'Username must contain only letters and numbers!'
              else:
                     mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)',(username, password, email)
                    )
                     mydb.commit() #save data in dATABASE
                     msg = 'Your Registration is Successful'
                     return render_template('index.html', msg=msg, name=username) #welcome page
       elif request.method == 'POST':
            msg = 'Kindly fill the details!'
       return render_template('registration.html', msg=msg) #else if will ask to register
app.run(host='0.0.0.0', port=8080)