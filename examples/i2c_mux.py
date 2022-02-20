import smbus
import time
import sys

channel_array=[0b00000001,0b00000010,0b00000100,0b00001000,0b00010000,0b00100000,0b01000000,0b10000000]

# Address of the two mux drivers
RIGHT_MUX = 0x70
LEFT_MUX = 0x71

def set_chan(multiplexer,i2c_channel_setup):
    bus = smbus.SMBus(1)

    # turn the other mux off by setting to unused channel 0
    if multiplexer == RIGHT_MUX:
        bus.write_byte(LEFT_MUX,channel_array[0])
    else:
        bus.write_byte(RIGHT_MUX,channel_array[0])

    # turn the requested mux channel on
    bus.write_byte(multiplexer,channel_array[i2c_channel_setup])

    # Sleep a millisecond and read the mux status (comment out after testing)
    time.sleep(0.001)
    print("I2C channel status:", bin(bus.read_byte(multiplexer)))
