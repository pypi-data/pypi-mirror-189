import fieldday
from vedirect import VEDirect
from collections import OrderedDict

keyName = {
    'V': 'batteryVoltage',
    'V2': 'batteryVoltage2',
    'V3': 'batteryVoltage3',
    'VS': 'auxVoltage',
    'VM': 'midVoltage',
    'DM': 'midDeviation',
    'VPV': 'panelVoltage',
    'PPV': 'panelPower',
    'I': 'batteryCurrent',
    'I2': 'batteryCurrent2',
    'I3': 'batteryCurrent3',
    'IL': 'loadCurrent',
    'LOAD': 'load',
    'T': 'batteryTemperature',
    'P': 'instantaneousPower',
    'CE': 'consumedEnergy',
    'SOC': 'stateOfCharge',
    'TTG': 'timeToGo',
    'Alarm': 'alarmState',
    'Relay': 'relayState',
    'AR': 'alarmReason',
    'OR': 'offReason',
    'H1': 'depthOfDeepestDischarge',
    'H2': 'depthOfLastDischarge',
    'H3': 'depthOfAvgDischarge',
    'H4': 'numberOfChargeCycles',
    'H5': 'numberOfFullCDischarges',
    'H6': 'cumulativeEnergy',
    'H7': 'minBatteryVoltage',
    'H8': 'maxBatteryVoltage',
    'H9': 'timeSinceLastFullCharge',
    'H10': 'numberOfAutoSynchs',
    'H11': 'numberOfLowMainVoltageAlarms',
    'H12': 'numberOfHighMainVoltageAlarms',
    'H13': 'numberOfLowAuxVoltageAlarms',
    'H14': 'numberOfHighAuxVoltageAlarms',
    'H15': 'minAuxVoltage',
    'H16': 'maxAuxVoltage',
    'H17': 'dischargedEnergy',
    'H18': 'chargedEnergy',
    'H19': 'yieldTotal',
    'H20': 'yieldToday',
    'H21': 'maximumPowerToday',
    'H22': 'yieldYesterday',
    'H23': 'maximumPowerYesterday',
    'ERR': 'error',
    'CS': 'mode',
    'BMV': 'modelDescription',
    'FW': 'firmwareVersion',
    'FWE': 'firmwareVersion24Bit',
    'PID': 'productId',
    'SER#': 'serialNumber',
    'HSDS': 'daySequenceNumber',
    'MODE': 'deviceMode',
    'AC_OUT_V': 'acOutputVoltage',
    'AC_OUT_I': 'acOutputCurrent',
    'AC_OUT_S': 'acOutputApparentPower',
    'WARN': 'warningReason',
    'MPPT': 'trackerMode'
}


class FieldOffReason(fieldday.FieldInt):
    def str_value(self):
        return VEDirect.offReasonDecode.get(self.value, '{0:d}'.format(self.value))


class FieldMode(fieldday.FieldInt):
    def str_value(self):
        return VEDirect.device_state_map.get(self.value, '{0:d}'.format(self.value))


class FieldTrackerMode(fieldday.FieldInt):
    def str_value(self):
        return VEDirect.trackerModeDecode.get(self.value, '{0:d}'.format(self.value))


class FieldErrorCode(fieldday.FieldInt):
    def str_value(self):
        return VEDirect.error_codes.get(self.value, '{0:d}'.format(self.value))


fieldTypes = OrderedDict([
    ('batteryVoltage', (fieldday.FieldInt, {'desc': 'Main or channel 1 (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('batteryVoltage2', (fieldday.FieldInt, {'desc': 'Channel 2 (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('batteryVoltage3', (fieldday.FieldInt, {'desc': 'Channel 3 (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('auxVoltage', (fieldday.FieldInt, {'desc': 'Auxiliary (starter) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('midVoltage', (fieldday.FieldInt, {'desc': 'Mid-point voltage of battery bank', 'units': 'mV', 'fmt': 'd'})),
    ('midDeviation', (fieldday.FieldInt, {'desc': 'Mid-point deviation of battery bank', 'units': '%', 'fmt': 'd'})),
    ('panelVoltage', (fieldday.FieldInt, {'desc': 'Panel voltage', 'units': 'mV', 'fmt': 'd'})),
    ('panelPower', (fieldday.FieldInt, {'desc': 'Panel power', 'units': 'W', 'fmt': 'd'})),
    ('batteryCurrent', (fieldday.FieldInt, {'desc': 'Main or channel 1 battery current', 'units': 'mA', 'fmt': 'd'})),
    ('batteryCurrent2', (fieldday.FieldInt, {'desc': 'Channel 2 battery current', 'units': 'mA', 'fmt': 'd'})),
    ('batteryCurrent3', (fieldday.FieldInt, {'desc': 'Channel 3 battery current', 'units': 'mA', 'fmt': 'd'})),
    ('loadCurrent', (fieldday.FieldInt, {'desc': 'Load current', 'units': 'mA', 'fmt': 'd'})),
    ('load', (fieldday.FieldStr, {'desc': 'Load output state (ON/OFF)'})),
    ('batteryTemperature', (fieldday.FieldInt, {'desc': 'Battery temperature', 'units': 'degC', 'fmt': 'd'})),
    ('instantaneousPower', (fieldday.FieldInt, {'desc': 'Instantaneous power', 'units': 'W', 'fmt': 'd'})),
    ('consumedAH', (fieldday.FieldInt, {'desc': 'Consumed Amp Hours', 'units': 'mAh', 'fmt': 'd'})),
    ('stateOfCharge', (fieldday.FieldInt, {'desc': 'State-of-charge', 'units': '%', 'fmt': 'd'})),
    ('timeToGo', (fieldday.FieldInt, {'desc': 'Time-to-go', 'units': 'min', 'fmt': 'd'})),
    ('alarmState', (fieldday.FieldStr, {'desc': 'Alarm condition active'})),
    ('relayState', (fieldday.FieldStr, {'desc': 'Relay state'})),
    ('alarmReason', (fieldday.FieldInt, {'desc': 'Alarm reason', 'fmt': 'd'})),
    ('offReason', (FieldOffReason, {'desc': 'Off reason'})),
    ('depthOfDeepestDischarge', (fieldday.FieldInt, {'desc': 'Depth of the deepest discharge', 'units': 'mAh', 'fmt': 'd'})),
    ('depthOfLastDischarge', (fieldday.FieldInt, {'desc': 'Depth of the last discharge', 'units': 'mAh', 'fmt': 'd'})),
    ('depthOfAvgDischarge', (fieldday.FieldInt, {'desc': 'Depth of the average discharge', 'units': 'mAh', 'fmt': 'd'})),
    ('numberOfChargeCycles', (fieldday.FieldInt, {'desc': 'Number of charge cycles', 'fmt': 'd'})),
    ('numberOfFullCDischarges', (fieldday.FieldInt, {'desc': 'Number of full discharges', 'fmt': 'd'})),
    ('cumulativeEnergy', (fieldday.FieldInt, {'desc': 'Cumulative Amp Hours drawn', 'units': 'mAh', 'fmt': 'd'})),
    ('minBatteryVoltage', (fieldday.FieldInt, {'desc': 'Minimum main (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('maxBatteryVoltage', (fieldday.FieldInt, {'desc': 'Maximum main (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('timeSinceLastFullCharge', (
        fieldday.FieldInt, {'desc': 'Number of seconds since last full charge', 'units': 's', 'fmt': 'd'})),
    ('numberOfAutoSynchs', (
        fieldday.FieldInt, {'desc': 'Number of automatic synchronizations', 'fmt': 'd'})),
    ('numberOfLowMainVoltageAlarms', (
        fieldday.FieldInt, {'desc': 'Number of low main voltage alarms', 'fmt': 'd'})),
    ('numberOfHighMainVoltageAlarms', (
        fieldday.FieldInt, {'desc': 'Number of high main voltage alarms', 'fmt': 'd'})),
    ('numberOfLowAuxVoltageAlarms', (
        fieldday.FieldInt, {'desc': 'Number of low auxiliary voltage alarms', 'fmt': 'd'})),
    ('numberOfHighAuxVoltageAlarms', (
        fieldday.FieldInt, {'desc': 'Number of high auxiliary voltage alarms', 'fmt': 'd'})),
    ('minAuxVoltage', (fieldday.FieldInt, {'desc': 'Minimum auxiliary (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('maxAuxVoltage', (fieldday.FieldInt, {'desc': 'Maximum auxiliary (battery) voltage', 'units': 'mV', 'fmt': 'd'})),
    ('dischargedEnergy', (fieldday.FieldInt, {'desc': 'Amount of discharged energy', 'units': '0.01 kWh', 'fmt': 'd'})),
    ('chargedEnergy', (fieldday.FieldInt, {'desc': 'Amount of charged energy', 'units': '0.01 kWh', 'fmt': 'd'})),
    ('yieldTotal', (
        fieldday.FieldInt, {'desc': 'Yield total (user resettable counter)', 'units': '0.01 kWh', 'fmt': 'd'})),
    ('yieldToday', (fieldday.FieldInt, {'desc': 'Yield today', 'units': '0.01 kWh', 'fmt': 'd'})),
    ('maximumPowerToday', (fieldday.FieldInt, {'desc': 'Maximum power today', 'units': 'W', 'fmt': 'd'})),
    ('yieldYesterday', (fieldday.FieldInt, {'desc': 'Yield yesterday', 'units': '0.01 kWh', 'fmt': 'd'})),
    ('maximumPowerYesterday', (fieldday.FieldInt, {'desc': 'Maximum power yesterday', 'units': 'W', 'fmt': 'd'})),
    ('error', (FieldErrorCode, {'desc': 'Error code'})),
    ('mode', (FieldMode, {'desc': 'State of operation'})),
    ('modelDescription', (fieldday.FieldStr, {'desc': 'Model description (deprecated)'})),
    ('firmwareVersion', (fieldday.FieldStr, {'desc': 'Firmware version (16 bit)'})),
    ('firmwareVersion24Bit', (fieldday.FieldStr, {'desc': 'Firmware version (24 bit)'})),
    ('productId', (fieldday.FieldStr, {'desc': 'Product ID'})),
    ('serialNumber', (fieldday.FieldStr, {'desc': 'Serial number'})),
    ('daySequenceNumber', (fieldday.FieldInt, {'desc': 'Day sequence number (0..364)', 'fmt': 'd'})),
    ('deviceMode', (fieldday.FieldInt, {'desc': 'Device mode', 'fmt': 'd'})),
    ('acOutputVoltage', (fieldday.FieldInt, {'desc': 'AC output voltage', 'units': '0.01 V', 'fmt': 'd'})),
    ('acOutputCurrent', (fieldday.FieldInt, {'desc': 'AC output current', 'units': '0.1 A', 'fmt': 'd'})),
    ('acOutputApparentPower', (fieldday.FieldInt, {'desc': 'AC output apparent power', 'units': 'VA', 'fmt': 'd'})),
    ('warningReason', (fieldday.FieldInt, {'desc': 'Warning reason', 'fmt': 'd'})),
    ('trackerMode', (FieldTrackerMode, {'desc': 'Tracker operation mode'}))])


# intervalTypes = {
#     'batteryVoltage': IntervalAccumulatorAverage,
#     'batteryVoltage2': IntervalAccumulatorAverage,
#     'batteryVoltage3': IntervalAccumulatorAverage,
#     'auxVoltage': IntervalAccumulatorAverage,
#     'midVoltage': IntervalAccumulatorAverage,
#     'midDeviation': IntervalAccumulatorAverage,
#     'panelVoltage': IntervalAccumulatorAverage,
#     'panelPower': IntervalAccumulatorAverage,
#     'batteryCurrent': IntervalAccumulatorAverage,
#     'batteryCurrent2': IntervalAccumulatorAverage,
#     'batteryCurrent3': IntervalAccumulatorAverage,
#     'loadCurrent': IntervalAccumulatorAverage,
#     'batteryTemperature': IntervalAccumulatorAverage,
#     'instantaneousPower': IntervalAccumulatorAverage,
#     'alarmState': IntervalAccumulatorOn,
#     'alarmReason': IntervalAccumulatorBitmapOn,
#     'error': IntervalAccumulatorLastNonzero,
#     'acOutputVoltage': IntervalAccumulatorAverage,
#     'acOutputCurrent': IntervalAccumulatorAverage,
#     'acOutputApparentPower': IntervalAccumulatorAverage,
#     'warningReason': IntervalAccumulatorBitmapOn
# }
