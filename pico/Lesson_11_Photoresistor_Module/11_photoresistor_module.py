import machine  # Hardware control library
import time  # Time control library

photoresistor = machine.ADC(26)  # Initialize ADC on pin 26

while True:
    value = photoresistor.read_u16()  # Read analog value
    print(value)  # Print the value

    time.sleep_ms(200)  # Delay of 200 ms between reads
