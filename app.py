import sqlite3
from flask import Flask, render_template, jsonify

#creat a flask instance
app = Flask(__name__)

#create a route 
@app.route('/')

def index():
    # establish a connection to the database
    conn = sqlite3.connect('values.db')
    # create a cursor to execute SQL commands
    c = conn.cursor()
    # execute SQL command to calculate the average value for tag11
    c.execute("SELECT AVG(value) FROM robot WHERE name = 'tag12'")
    # fetch the result and print the average value
    average_tag11 = c.fetchone()[0]
    # execute SQL command to select the latest value for tag12
    c.execute("SELECT value FROM robot WHERE name = 'tag12' ORDER BY date DESC LIMIT 1")
    # fetch the result and print the value
    result = c.fetchone()[0]
    # close the connection
    conn.close()
    return render_template("index.html", average_tag11=average_tag11, result=result)


# @app.route('/user/<name>')

# def user(name):
#     return "<h1>hello {name}</h1>".format(name)