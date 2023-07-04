import serial
import time
import codecs

serial_port = "COM24"
baud_rate = 9600

#Radio set up
freq = 915
mod = "SF9"
band_width = 125
tx_pr = 8
rx_pr = 8
power = 22

#RF configuration string
rf_conf_str = "AT+TEST=RFCFG,{},{},{},{},{},{},OFF,OFF,OFF\n".format(freq, mod, band_width, tx_pr, rx_pr, power)

#Serial Objet
ser = serial.Serial(serial_port,baud_rate)

def main():
    serial_port=input('Set your Radio comm Port: (win: "COMXX")(linux: "/dev/ttyXXXX") ')
    initialize_radio()
    print("Radio Initialized")
    usr = input('Set Username: ')
    print('Your username is: {}'.format(usr))
    print('Begining LoRa Radio Chat ...')
    

def initialize_radio(): #Test PASSED
    ser.write("AT+MODE=TEST\n".encode())
    time.sleep(0.5)
    print(ser.readline().decode())
    time.sleep(0.5)
    ser.write(rf_conf_str.encode())
    print(ser.readline().decode())

def send_msg(message):
    ser.write("AT+TEST=TXLRPKT,\"{}\"\n".format(message).encode())
    print(ser.readline().decode())

def receive_msg():
    ser.write("AT+TEST=RXLRPKT".encode())
    while True:
        if ser.inWaiting():
            rx_msg = ser.readline().decode()
            if '+TEST: RX ' in rx_msg:
                msg_data = rx_msg.split('\"')[-2]
                print(hex_to_chr(msg_data))

def chr_to_hex(string):
    return codecs.encode(string.encode(),'hex').decode()

def hex_to_chr(string):
    return codecs.decode(string, 'hex').decode()


initialize_radio()
time.sleep(1)
#receive_msg()
import serial
import time
import codecs

serial_port = "COM24"
baud_rate = 9600

#Radio set up
freq = 915
mod = "SF9"
band_width = 125
tx_pr = 8
rx_pr = 8
power = 22

#RF configuration string
rf_conf_str = "AT+TEST=RFCFG,{},{},{},{},{},{},OFF,OFF,OFF\n".format(freq, mod, band_width, tx_pr, rx_pr, power)

#Serial Objet
ser = serial.Serial(serial_port,baud_rate)

def main():
    serial_port=input('Set your Radio comm Port: (win: "COMXX")(linux: "/dev/ttyXXXX") ')
    initialize_radio()
    print("Radio Initialized")
    usr = input('Set Username: ')
    print('Your username is: {}'.format(usr))
    print('Begining LoRa Radio Chat ...')
    

def initialize_radio(): #Test PASSED
    ser.write("AT+MODE=TEST\n".encode())
    time.sleep(0.5)
    print(ser.readline().decode())
    time.sleep(0.5)
    ser.write(rf_conf_str.encode())
    print(ser.readline().decode())

def send_msg(message):
    ser.write("AT+TEST=TXLRPKT,\"{}\"\n".format(message).encode())
    print(ser.readline().decode())

def receive_msg():
    ser.write("AT+TEST=RXLRPKT".encode())
    while True:
        if ser.inWaiting():
            rx_msg = ser.readline().decode()
            if '+TEST: RX ' in rx_msg:
                msg_data = rx_msg.split('\"')[-2]
                print(hex_to_chr(msg_data))

def chr_to_hex(string):
    return codecs.encode(string.encode(),'hex').decode()

def hex_to_chr(string):
    return codecs.decode(string, 'hex').decode()


initialize_radio()
time.sleep(1)
#receive_msg()
send_msg("72")
