import time
import sys
from opcua import Client
from datetime import datetime
import sqlite3
import signal
import sys

url = "opc.tcp://desktop-080ph8v:62640/IntegrationObjects/ServerSimulator"

try:
    
    Client = Client(url)
    Client.connect()
    print("Connected with OPC UA server")

except Exception as err:
    print(err)
    sys.exit(1)

class sub_handler(object):
    def __init__(self, nodes):
        self.conn = sqlite3.connect('values.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.nodes = nodes
        self.current_logged_user_level_val = None
        self.robot_running_val = None
        self.alarm_code_val = None

    def __del__(self):
        self.conn.close()

    def datachange_notification(self, node, val, data):
        if node in self.nodes:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            if node == self.nodes[0]:
                self.current_logged_user_level_val = val
            if node == self.nodes[1]:
                self.robot_running_val = val
            if node == self.nodes[2]:
                self.alarm_code_val = val
            self.c.execute("INSERT INTO robot VALUES (?, ?, ?, ?)", (current_time, self.current_logged_user_level_val, self.robot_running_val, self.alarm_code_val))
            self.conn.commit()


if __name__ == '__main__':
    current_logged_user_level = Client.get_node("ns=2;s=current_logged_user_level")
    robot_running = Client.get_node("ns=2;s=robot_running")
    alarm_code = Client.get_node("ns=2;s=alarm_code")

    current_logged_user_level_val = 0
    robot_running_val = 0
    alarm_code_val = 0

    # subscription handler
    handler = sub_handler([current_logged_user_level, robot_running, alarm_code])
    # subscriptions
    sub = Client.create_subscription(500, handler)
    # nodes of interest
    handle = sub.subscribe_data_change(handler.nodes)

    # Exiting the app with Ctrl+C
    try:
        while True:
            pass  # Your main loop or other processing goes here
    except KeyboardInterrupt:
        print("Exiting.")
    finally:
        Client.disconnect()