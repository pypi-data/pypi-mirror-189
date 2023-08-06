""" Monitor and publish INA226 data to to MQTT.

Set up and monitor INA226 chip on I2C on Raspberry Pi.
Publish to MQTT topic `emcnet/ina226[/<id>]`.  
`measurement` is the name of the service or device that generated 
`id` can be included if 
one wishes to further denote a mesaurement id, but it will not
override an "id" field within the "tag" object or the json payload 
unless overridemeasurment=True.  
ID may be a serial number or a location.  Examples could be "ina226/0001",
"vmppt/vanbattery."

Typical usage example:

  $ ../ina226_publish --id=0001

"""

import argparse
from emcnet.emcnet_data_publisher import MQTTDataPublisher
import emcnet.device.vedirect_types as vedirect_types
import json
import sys
import logging
import fieldday
import time
import math
from dotenv import load_dotenv
import os

PYTHON_SMBUS2_LIB_PRESENT = True
try:
    import smbus2
except ImportError as e:
    PYTHON_SMBUS2_LIB_PRESENT = False

if PYTHON_SMBUS2_LIB_PRESENT:
    from .ina226 import INA226
    
log = logging.getLogger(__name__)

# load environment variables for package config
load_dotenv()

devicename_default = 'vmppt_0000'
serial_port_default = '/dev/serial/by-id/usb-FTDI_FT232EX-if00-port0'


class INA226Monitor:

    def __init__(self, port=serial_port_default, emulate=False, mqttbrokeraddress='localhost', mqttbrokerport=1883,
                 id=None, sph=360, shuntresistance=0.0015, maxcurrent=65.54):
        log.info(f"INA226 Monitor")
        self.id = id
        self.emulate = emulate
        self.sph = sph
        self.mqttbrokeraddress = mqttbrokeraddress
        if emulate:
            self.measurement = "ina226_emulate"
        else:
            self.measurement = "ina226"
        if not emulate:
            self.ina = INA226(busnum=1, address=0x40, max_expected_amps=maxcurrent, 
                              shunt_ohms=shuntresistance)
            self.ina.configure()
            self.ina.set_low_battery(5)
            time.sleep(2)
        if self.mqttbrokeraddress:
            log.info(f"Instantiating MQTT Device Data Publisher")
            self.ddp = MQTTDataPublisher(self.measurement, id=id, 
                                         mqttbrokeraddress=mqttbrokeraddress, 
                                         mqttbrokerport=mqttbrokerport)
        self.topic = "emcnet/" + self.measurement
        if id:
            if isinstance(id, str):
                self.topic = self.topic + "/" + id.strip()
            else:
                log.error("id is not a string")
                raise Exception("id must be a string")
        else:
            # could look for ID in the payload but not sure this is the best design
            pass
        
    def publish_record(self, datarecord: dict):
        # fieldday.rename_keys(datarecord, vedirect_types.keyName)
        newrecord = dict()
        newrecord["time"] = time.time_ns()
        newrecord["measurement"] = self.measurement
        newrecord["fields"] = datarecord
        if self.id:
            if not "tags" in newrecord:
                newrecord["tags"] = dict()
            newrecord["tags"]["id"] = self.id                
        log.debug(f"Storing: {newrecord}")
        # publish the record
        if self.mqttbrokeraddress:
            # publish record to MQTT broker
            self.ddp.publish(newrecord)
        else:
            # print the data to stdout
            print(json.dumps(newrecord))
            sys.stdout.flush()  # important - otherwise when piping, Python may buffer this output for some reason

    def read_ina226(self) -> dict:
        if not self.emulate:
            record = {}
            record['V'] = ina.voltage()
            record['I'] = ina.current()
            record['P'] = ina.power()
        else:
            record = {}
            record['V'] = 13.0
            record['I'] = -2.0
            record['P'] = -26.0
        # print("Bus Voltage    : %.3f V" % ina.voltage())
        # print("Bus Current    : %.3f mA" % ina.current())
        # print("Supply Voltage : %.3f V" % ina.supply_voltage())
        # print("Shunt voltage  : %.3f mV" % ina.shunt_voltage())
        # print("Power          : %.3f mW" % ina.power())
        return (record)

    def run(self):
        seconds_per_sample = 3600/self.sph
        while True:
            time.sleep(seconds_per_sample - math.fmod(time.time(), seconds_per_sample))
            self.publish_record(self.read_ina226())

def main():
    # set the default path to the EMCNET directory - from the environment if set
    emcnetdir = os.getenv("EMCNET_DIR", '/etc/emcnet').rstrip('/')
    load_dotenv(emcnetdir + '/config.env', override=True)
    # read command-line arguments and override environment variables if given
    parser = argparse.ArgumentParser(description=(
        'INA226 Publisher - Reads INA226 continuously and publishes to MQTT or stdout'))
    parser.add_argument('--port', default=serial_port_default, help='Serial port to listen for VEDirect MPPT messages')
    parser.add_argument('--mqttbrokeraddress', help='MQTT broker address', type=str,
                        default=os.getenv("MQTT_BROKER_ADDRESS", 'localhost'))
    parser.add_argument('--mqttbrokerport', help='MQTT broker port', type=int,
                        default=os.getenv("MQTT_BROKER_PORT", 1883))
    parser.add_argument('--loglevel', help='logging level one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]',
                        default=os.getenv("EMCNET_LOG_LEVEL", 'INFO'))
    parser.add_argument('--emulate', action='store_true', help='emulate measurements (default=False)')
    parser.add_argument('--id', help='Override id in the payload (e.g. "12345", "vanbattery", etc...)', 
                        type=str)
    parser.add_argument('-s', '--sph', help='Samples per hour (default = 360)', type=int, default=360)
    parser.add_argument('-m', '--maxcurrent', help='Maximum current in Amps (default = 65.54)', 
                        type=float, default=65.54)
    parser.add_argument('-r', '--shuntresistance', help='Shunt resistance (Ohms) (default = 0.0015)', 
                        type=float, default=0.0015)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel.upper())
    log.info("INA226 Publisher - Reads INA226 continuously and publishes to MQTT or stdout")
    emulate = False
    if args.emulate:
        emulate = True
        log.info("Emulation mode selected")
    else:
        if not PYTHON_SMBUS2_LIB_PRESENT:
            emulate = True
            log.info("SMBUS2 package not installed - switching to emuluation mode")
    log.info(f"VMPPT port: {args.port}")        
    log.info(f"EMCNet directory: {emcnetdir}")
    log.info(f"MQTT Broker: {args.mqttbrokeraddress}")
    log.info(f"Device/Measurement: vmppt")
    if args.id:
        log.info(f"ID: {args.id}")
    vm = INA226Monitor(args.port, emulate=emulate, mqttbrokeraddress=args.mqttbrokeraddress,
                      mqttbrokerport=args.mqttbrokerport, id=args.id, sph=args.sph,
                      shuntresistance=args.shuntresistance, maxcurrent=args.maxcurrent)
    vm.run()


if __name__ == '__main__':
    main()



    ina = INA226(busnum=1, max_expected_amps=25, log_level=logging.DEBUG)
    ina.configure()
    ina.set_low_battery(5)
    sleep(3)
    print("===================================================Begin to read")
    read()