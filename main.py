import time
import sys
from opcua import Client
from datetime import datetime
import sqlite3

url = "opc.tcp://desktop-080ph8v:62640/IntegrationObjects/ServerSimulator"

try:
    
    Client = Client(url)
    Client.connect()
    print("Connected with OPC UA server")

except Exception as err:
    print(err)
    sys.exit(1)

class sub_handler(object):
    def __init__(self):
        self.conn = sqlite3.connect('values.db', check_same_thread=False)  # create a connection to the database
        self.c = self.conn.cursor()  # create a cursor

    def datachange_notification(self, node, val, data):
        if node == node_tag11:
            print("Value of Tag 11 is:", val)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.c.execute("INSERT INTO robot VALUES ('tag11', ?, ?)", (val, current_time))
            self.conn.commit()
        elif node == node_tag12:
            print("Value of Tag 12 is:", val)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.c.execute("INSERT INTO robot VALUES ('tag12', ?, ?)", (val, current_time))
            self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    node_tag11 = Client.get_node("ns=2;s=Tag11")
    node_tag12 = Client.get_node("ns=2;s=Tag12")

    #subscription handler
    handler = sub_handler()
    #subscriptions
    sub = Client.create_subscription(500, handler)
    #nodes of interest
    handle = sub.subscribe_data_change((node_tag11,node_tag12))