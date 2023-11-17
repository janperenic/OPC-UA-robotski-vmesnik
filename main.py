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
        self.conn = sqlite3.connect('values.db', check_same_thread=False)  # create a connection to the database
        self.c = self.conn.cursor()  # create a cursor
        self.nodes = nodes

    def __del__(self):
        self.conn.close()

    def datachange_notification(self, node, val, data):
        if node in self.nodes:
            print(f"Value of {node} is:", val)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.c.execute(f"INSERT INTO robot VALUES ('{node}', ?, ?)", (val, current_time))
            self.conn.commit()

if __name__ == '__main__':
    current_logged_user_level = Client.get_node("ns=2;s=current_logged_user_level")
    robot_running = Client.get_node("ns=2;s=robot_running")
    
    #subscription handler
    handler = sub_handler()
    #subscriptions
    sub = Client.create_subscription(500, handler)
    #nodes of interest
    handle = sub.subscribe_data_change((current_logged_user_level,robot_running,robot_playback,robot_energy_saving,product_code,serial_number,alarm,alarm_axes,alarm_code,alarm_date,alarm_job,alarm_mode,alarm_active,error_active,reset_alarm,reset_error,axis_name_1,axis_name_2,axis_name_3,axis_name_4,axis_name_5,axis_name_6,axis_position_1,axis_position_2,axis_position_3,axis_position_4,axis_position_5,axis_position_6,axis_degree_1,axis_degree_2,axis_degree_3,axis_degree_4,axis_degree_5,axis_degree_6,axis_speed_1,axis_speed_2,axis_speed_3,axis_speed_4,axis_speed_5,axis_speed_6,speed_reducer_design_lifetime_1,speed_reducer_design_lifetime_2,speed_reducer_design_lifetime_3,speed_reducer_design_lifetime_4,speed_reducer_design_lifetime_5,speed_reducer_design_lifetime_6,speed_reducer_remaining_lifetime_1,speed_reducer_remaining_lifetime_2,speed_reducer_remaining_lifetime_3,speed_reducer_remaining_lifetime_4,speed_reducer_remaining_lifetime_5,speed_reducer_remaining_lifetime_6,amplifiers_designed_lifetime_1,amplifiers_designed_lifetime_2,amplifiers_designed_lifetime_3,amplifiers_designed_lifetime_4,amplifiers_designed_lifetime_5,amplifiers_designed_lifetime_6,amplifiers_remaining_lifetime_1,amplifiers_remaining_lifetime_2,amplifiers_remaining_lifetime_3,amplifiers_remaining_lifetime_4,amplifiers_remaining_lifetime_5,amplifiers_remaining_lifetime_6,capacitors_design_lifetime_1,capacitors_design_lifetime_2,capacitors_design_lifetime_3,capacitors_design_lifetime_4,capacitors_design_lifetime_5,capacitors_design_lifetime_6,capacitors_remaining_lifetime_1,capacitors_remaining_lifetime_2,capacitors_remaining_lifetime_3,capacitors_remaining_lifetime_4,capacitors_remaining_lifetime_5,capacitors_remaining_lifetime_6,contactors_design_lifetime_1,contactors_design_lifetime_2,contactors_design_lifetime_3,contactors_design_lifetime_4,contactors_design_lifetime_5,contactors_design_lifetime_6,contactors_remaining_lifetime_1,contactors_remaining_lifetime_2,contactors_remaining_lifetime_3,contactors_remaining_lifetime_4,contactors_remaining_lifetime_5,contactors_remaining_lifetime_6,cps_fan_designed_lifetime,cps_fan_remaining_lifetime,controller_box_fan_designed_lifetime,controller_box_fan_remaining_lifetime,regenerative_fan_designed_lifetime,regenerative_box_fan_remaining_lifetime,manipulator_fan_designed_lifetime,manipulator_box_fan_remaining_lifetime,set_job,flange_load,device_manufacturer,device_model,device_moving,total_moving_time,total_playback_time,total_servo_on_time,encoder_temperature_1,encoder_temperature_2,encoder_temperature_3,encoder_temperature_4,encoder_temperature_5,encoder_temperature_6,device_serial_number,grease_supply_design_lifetime,grease_supply_remaining_lifetime,wire_harness_design_lifetime,wire_harness_remaining_lifetime,battery_exchange_design_lifetime,battery_exchange_remaining_lifetime,overhaul_design_lifetime,overhaul_remaining_lifetime,emergency_stop,protective_stop))
