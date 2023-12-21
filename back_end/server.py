from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from threading import Thread
import sqlite3
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# constant update
app.config.from_object(__name__)

# CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r"/*":{'origins':"*", "allow_headers":"Access-Control-Allow-Origin"}})

# create a route
@app.route('/')
def index():
  return render_template('index.html')

def emit_data():
  while True:
    # connect to db
    conn = sqlite3.connect('../values.db')

    # SQL commands
    c = conn.cursor()
    c.execute("SELECT alarm_code, robot_running, current_logged_user_level FROM robot ORDER BY date DESC LIMIT 1")

    # get the alarm_code, robot_running, and logged_user_level values
    last_alarm_code, last_robot_running, last_current_logged_user_level = c.fetchone()

    # update details
    details = {}
    details['last_alarm_code'] = last_alarm_code
    details['last_robot_running'] = last_robot_running
    details['last_current_logged_user_level'] = last_current_logged_user_level
    details['data'] = last_current_logged_user_level, "test"

    # emit data to clients
    socketio.emit('after connect', details)

    c.execute("SELECT alarm_code, robot_running, current_logged_user_level FROM robot ORDER BY date DESC LIMIT 1")
    latest_alarm_code, latest_robot_running, latest_current_logged_user_level = c.fetchone()

    if (last_alarm_code != latest_alarm_code or
        last_robot_running != latest_robot_running or
        last_current_logged_user_level != latest_current_logged_user_level):
      # emit events for the changed values
      if last_alarm_code != latest_alarm_code:
        socketio.emit('alarm_code_changed', latest_alarm_code)
      if last_robot_running != latest_robot_running:
        socketio.emit('robot_running_changed', latest_robot_running)
      if last_current_logged_user_level != latest_current_logged_user_level:
        socketio.emit('current_logged_user_level_changed', latest_current_logged_user_level)

    # sleep for 5 seconds
    time.sleep(1)


# start the emitting thread
emit_thread = Thread(target=emit_data)
emit_thread.daemon = True
emit_thread.start()

if __name__ == '__main__':
  socketio.run(app)
