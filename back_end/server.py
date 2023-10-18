#boot up with python server.py
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
def test_connect():
    # establish a connection to the database
    conn = sqlite3.connect('../values.db')
    # execute SQL command to calculate the average value for tag12
    c = conn.cursor()
    c.execute("SELECT AVG(value) FROM robot WHERE name = 'tag12'")
    #c.execute("SELECT value FROM robot ORDER BY tag12 DESC LIMIT 10")
    average_tag12 = c.fetchone()[0]

    details = {
        'tag12': average_tag12,
        'data': 'Hello, my name is Jan'
    }
    # emit the average value to the client
    socketio.emit('after connect', details)  

if __name__ == '__main__':
    socketio.run(app)


