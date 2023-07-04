import serial 
import time 
import codecs

baudrate = 9600
mod = "SF9"
band_width = 125
tx_pr = 8
rx_pr = 8
power = 22

def main():
    print('Welcome to Echo.py script for lora echo communication...\n\n')
    port = input('Set your Serial comm port: ')
    freq = input('Set your center frequency: ')
    initialize_radio(port,freq)
    listening_ping()

def listening_ping()
    ser.write("AT+TEST=RXLRPKT".encode())
    while True:
        if ser.inWaiting():
            rx_msg = ser.readline().decode()
            if '+TEST: RX ' in rx_msg:
                msg_data = rx_msg.split('\"')[-2]
                if hex_to_chr(msg_data) == 'ping'
                    print('Ping received\nSending Echo')
                    time.sleep(1)
                    send_msg(chr_to_hex('ping'))
                    break
    listening_ping()

def initialize_radio(serial_port, freq):
    ser = serial.Serial(serial_port, baudrate)
    ser.write("AT+MODE=TEST")
    ser.write("AT""AT+TEST=RFCFG,{},{},{},{},{},{},OFF,OFF,OFF\n".format(freq, mod, band_width, tx_pr, rx_pr, power))
    print('Radio Initialized ...')

def send_msg(message):
    ser.write("AT+TEST=TXLRPKT,\"{}\"\n".format(message).encode())
    print(ser.readline().decode())

def chr_to_hex(string):
    return codecs.encode(string.encode(),'hex').decode()

def hex_to_chr(string):
    return codecs.decode(string, 'hex').decode()

