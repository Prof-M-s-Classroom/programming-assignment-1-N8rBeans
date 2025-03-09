import serial
import time

from distance import Distance
from stack import CircularStack

# Replace 'COM3' with the correct port for your system
arduino_port = 'COM6'
baud_rate = 9600

try:
    # Establish connection with Arduino
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Allow time for connection to establish
    print("Connected to Arduino. Reading Ultrasonic Sensor data...")
    initial = Distance(1.0)         # temporary distance object (for initializing stack)
    stack = CircularStack(initial)  # initialize circular stack
    stack.pop()                     # remove temporary distance object

    while True:
        if arduino.in_waiting > 0: # check if data is available
            distance = arduino.readline().decode('utf-8').strip()   # get data from arduino
            if distance:                        # check that data is valid
                reading = Distance(distance)    # create distance object with data
                stack.push(reading)             # add distance object to circular stack
                stack.print_stack()             # print stack of data
        time.sleep(2)  # Read every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()

except serial.SerialException:
    print("Error: Could not connect to Arduino. Check your port and connection.")
