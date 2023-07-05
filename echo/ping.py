import serial 
import time 
import codecs
import colorama
from colorama import Fore

freq = 915
serial_port = 'COM24'
baudrate = 9600
mod = "SF9"
band_width = 125
tx_pr = 8
rx_pr = 8
power = 22

time.monotonic()

ser = serial.Serial(serial_port, baudrate) 

def main():
    print('Welcome to Ping.py script for lora echo communication...\n\n')
    initialize_radio()
    time.sleep(0.5)
    print('Timeout in 10 seconds')
    send_ping()

def send_ping():
    send_msg(chr_to_hex('ping'))
    time.sleep(0.5)
    print('Ping Sent')
    t_end = time.time() + 9
    ser.write("AT+TEST=RXLRPKT\n".encode())
    while time.time() < t_end:
        if ser.inWaiting():
            rx_msg = ser.readline().decode()
            if '+TEST: RX ' in rx_msg:
                msg_data = rx_msg.split('\"')[-2]
                if hex_to_chr(msg_data) == 'ping':
                    print('Echo received')
                    time.sleep(0.5)
                    break
    if time.time()>t_end:
        print('timeout, echo not received\nSending ping again...')
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
