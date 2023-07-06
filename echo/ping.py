
#Code for ping client

import serial 
import time 
import codecs

#Radio setup
freq = 915
baud_rate = 115200
mod = "SF9"
band_width = 125
tx_pr = 8
rx_pr = 8
power = 30


#ICMP data 
icmp_id = 0 

def main():
    print('Welcome to Ping.py script for lora echo communication...\n\n') 
    global ser
    serial_port = input("Choose your Serial Port: ")
    ser = serial.Serial(serial_port, baud_rate)
    initialize_radio()
    time.sleep(0.5)
    send_ping()

def send_ping():
    global icmp_id
    time_stamp = time.time()
    message="ping,{},{}".format(icmp_id,time_stamp)
    send_msg(chr_to_hex(message))
    icmp_id += 1
    time.sleep(0.5)
    t_end = time.time() + 4
    ser.write("AT+TEST=RXLRPKT\n".encode())
    while time.time() < t_end:
        if ser.inWaiting():
            rx_msg = ser.readline().decode()
            if '+TEST: RX ' in rx_msg:
                msg_data = rx_msg.split('\"')[-2]
                ping_data = hex_to_chr(msg_data).split(',')
                if ping_data[0] == 'ping':
                    time_delta = time.time()-float(ping_data[2])
                    print('Echo received, icmp_id={}, time={}s'.format(ping_data[1], time_delta))
                    time.sleep(0.5)
                    break
    if time.time()>t_end:
        print('No echo received')
    send_ping()

def initialize_radio():
    ser.write("AT+MODE=TEST\n".encode())
    time.sleep(0.5)
    ser.write("AT+TEST=RFCFG,{},{},{},{},{},{},OFF,OFF,OFF\n".format(freq, mod, band_width, tx_pr, rx_pr, power).encode())
    print('Radio Initialized ...')

def send_msg(message):
    ser.write("AT+TEST=TXLRPKT,\"{}\"\n".format(message).encode())

def chr_to_hex(string):
    return codecs.encode(string.encode(),'hex').decode()

def hex_to_chr(string):
    return codecs.decode(string, 'hex').decode()

main()
