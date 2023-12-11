import sqlite3
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

#constant update
app.config.from_object(__name__)

#CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r"/*":{'origins':"*", "allow_headers":"Access-Control-Allow-Origin"}})

#create a route 
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    # establish a connection to the database
    conn = sqlite3.connect('../values.db')
    # execute SQL command to get the last alarm_code
    c = conn.cursor()
    c.execute("SELECT alarm_code FROM robot ORDER BY date DESC LIMIT 1")

    # get the alarm_code
    last_alarm_code = c.fetchone()[0]

    details = {}
    details['last_alarm_code'] = last_alarm_code
    details['data'] = 'Hello, my name is Jan'
    # change and add names of variables in template/index.html to test it out on webpage
    # emit the alarm_code to the client
    socketio.emit('after connect', details)


if __name__ == '__main__':
    socketio.run(app)
