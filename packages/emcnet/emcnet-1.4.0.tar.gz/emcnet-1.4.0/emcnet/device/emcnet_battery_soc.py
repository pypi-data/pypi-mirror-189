# -*- coding: utf-8 -*-
""" Monitor the emcnet MQTT broker for ina22c messages.  Use the data to update 
a battery SoC state estimator, and publish the state back to the emcnet MQTT broker. 

The messages are expected to be in json format.  

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import argparse
import json
import time
import sys
import logging
from dotenv import load_dotenv
import os
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import Point
import paho.mqtt.client as mqtt
import battery_soc_estimator 

log = logging.getLogger(__name__)

# cell capacity
Q_TOT_CELL = 3.2    # Ah

# Thevenin model values
R0 = 0.18
R1 = 0.001
C1 = 3000

# battery assy
N_PARALLEL = 30
N_SERIES = 4
    

class EMCNETBatterySoC:
    """ Monitor for ina226 data and maintain battery SoC estimate 
    """

    def __init__(self, mqttbrokeraddress='localhost', mqttbrokerport=1883, 
                 lineoutput=False):
        """ Instantiate
        Args:
            mqttbrokeraddress (str): MQTT broker address, e.g. "localhost"
            mqttbrokerport (str): MQTT broker port, e.g. "8086"
        """
        self.bucket = "st"
        log.info(f"EMCNET Battery SoC Class Initialized")
        log.info(f"MQTT Broker: {mqttbrokeraddress + ':' + str(mqttbrokerport)}")
        
        # Set up MQTT Client
        self.mqtt_client = mqtt.Client(client_id='emcnet_recorder', clean_session=True)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.lineoutput = lineoutput
        self.measurement = "batterysocestimator"
        # set password
        # self.mqtt_client.username_pw_set(username=emcnetremotebrokerid, password=emcnetremotebrokerpw)
        # handle the case of not being able to make an initial connection
        connected = False
        while not connected:
            try:
                self.mqtt_client.connect(mqttbrokeraddress, mqttbrokerport, 60)
            except ConnectionRefusedError:
                log.info(f"Error connecting to MQTT broker at "
                         f"{mqttbrokeraddress + ':' + str(mqttbrokerport)}. Waiting...")
                time.sleep(10)
            else:
                connected = True

        # Instantiate battery SoC estimator
        self.soc_estimator = battery_soc_estimator.BatteryEKF(Q_TOT_CELL, R0, R1, C1, 
                                                              N_PARALLEL, N_SERIES)
        self.t_last = 0
                                               
    def on_connect(self, client, userdata, flags, rc):
        log.info(f"Connected with result code {rc}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        log.info(f"Subscribing to topic emcnet/ina226/#")
        client.subscribe("emcnet/ina226/#")

    def on_message(self, client, userdata, msg):
        log.debug(f"Received message on topic {msg.topic}: {str(msg.payload)}")
        # Messages topics should be structured as emcnet/<measurement>[/<id>]
        msg_split = msg.topic.split('/')
        if len(msg_split) >= 2:
            measurement = msg_split[1]
            if len(msg_split) >= 3:
                id = msg_split[2]
            else:
                id = None
            self.update_and_publish(msg.payload, id)
        else:
            log.error("No measurement in emcnet topic string.")

    def update_and_publish(self, payload, id):
        """
        Update SoC estimator and publish new SoC
        """
        log.debug(f"Received: {payload}")
        try:
            payload_dict = json.loads(payload)
        except json.decoder.JSONDecodeError:
            log.error(f"JSON decode error on {payload}")
            return
        if isinstance(payload_dict, dict):
            if "fields" in payload_dict:
                # if an ID was included in the topic string, grab it
                if "tags" in payload_dict:
                    if "id" in payload_dict["tags"]:
                        id = payload_dict["tags"]["id"]
                if "I" in payload_dict["fields"] \
                    and "V" in payload_dict["fields"]:
                    i = -payload_dict["fields"]["I"]
                    v = payload_dict["fields"]["V"]
                    t = payload_dict["time"]
                    dt_s = (t - self.t_last)/1e9
                    self.t_last = t     
                    # only update if we are seeing a continuous stream
                    if dt_s <= 20.0:
                        # update filter
                        self.soc_estimator.update(i, dt_s, v)
                        soc = self.soc_estimator.soc
                        # publish 
                        self.publish(t, soc, id)
            else:
                log.error(f"No fields in payload.")
        else:
            log.error(f"Unsupported payload type: {payload!r}")
            
    def publish(self, time_ns, soc, id):
        topic = "emcnet/soc_estimator"
        newrecord = dict()
        newrecord["time"] = time_ns
        newrecord["measurement"] = self.measurement
        newrecord["fields"] = dict()
        newrecord["fields"]["SoC"] = soc
        if id:
            if not "tags" in newrecord:
                newrecord["tags"] = dict()
            newrecord["tags"]["id"] = id  
            topic = topic + "/" + id.strip()           
        log.debug(f"Publishing: {newrecord}")
        # publish the record
        newrecord_json = json.dumps(newrecord, separators=(',', ':'))
        if self.lineoutput:
            # print the data to stdout
            print(newrecord_json)
            sys.stdout.flush()  # important - otherwise when piping, Python may buffer this output for some reason
        else:
            # publish record to MQTT broker
            self.mqtt_client.publish(topic, newrecord_json)
        
    def run(self):
        """ Continuously watch emcnet MQTT topic and respond on message 
        """
        while True:
            # Blocking call that processes network traffic, dispatches callbacks and
            # handles reconnecting.
            # Other loop*() functions are available that give a threaded interface and a
            # manual interface.
            self.mqtt_client.loop_forever()
            
def main():
    # set the default path to the EMCNET directory - from the environment if set
    emcnetdir = os.getenv("EMCNET_DIR", '/etc/emcnet').rstrip('/')
    load_dotenv(emcnetdir + '/config.env', override=True)
    # read command-line arguments and override environment variables if given
    parser = argparse.ArgumentParser(description=(
        'EMCNET Battery SoC - makes battery SoC estimates from ina226 data'))
    parser.add_argument('--mqttbrokeraddress', help='MQTT broker address', type=str,
                        default=os.getenv("MQTT_BROKER_ADDRESS", 'localhost'))
    parser.add_argument('--mqttbrokerport', help='MQTT broker port', type=int,
                        default=os.getenv("MQTT_BROKER_PORT", 1883))    
    parser.add_argument('--loglevel', help='logging level one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]',
        default=os.getenv("EMCNET_LOG_LEVEL", 'INFO'))
    parser.add_argument('-l', '--lineoutput', help='do not publish - write to stdout instead',
                        action = "store_true")

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper())
    log.info("EMCNET Battery SoC - makes battery SoC estimates from ina226 data")
    log.info(f"EMCNet directory: {emcnetdir}")
    ds = EMCNETBatterySoC(mqttbrokeraddress=args.mqttbrokeraddress, mqttbrokerport=args.mqttbrokerport,
                          lineoutput=args.lineoutput)
    ds.run()


if __name__ == '__main__':
    main()
