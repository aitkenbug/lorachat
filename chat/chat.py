import serial
import time
import codecs
import threading


serial_port = ""
baud_rate = 115200

#Radio set up
freq = 915
mod = "SF9"
band_width = 125
tx_pr = 8
rx_pr = 8
power = 22
DELAY = 0.5
#RF configuration string
rf_conf_str = "AT+TEST=RFCFG,{},{},{},{},{},{},OFF,OFF,OFF\n".format(freq, mod, band_width, tx_pr, rx_pr, power)
TESTING_MODE = "AT+MODE=TEST\n"
RECV_MODE = "AT+TEST=RXLRPKT"
TX_MODE = "AT+TEST=TXLRPKT"
#Serial Objet
ser = None  
send = False
usr = ""
def init():
    global usr, ser
    usr = input('Set Username: ')
    serial_port = input("Choose your Serial Port: ")
    ser = serial.Serial(serial_port, baud_rate)
    initialize_radio()
    print("Radio Initialized")
    print('Your username is: {}'.format(usr))
    print('Begining LoRa Radio Chat ...')

    

def initialize_radio(): #Test PASSED
    write2ser(TESTING_MODE)
    print(ser.readline().decode())
    write2ser(rf_conf_str)
    print(ser.readline().decode())

def send_msg(message):
    write2ser(f"{TX_MODE},\"{message}\"\n")

def receive_msg():
    write2ser(RECV_MODE, delay=0)
    while True:
        while not send:
            if ser.inWaiting():
                rx_msg = ser.readline().decode()
                if '+TEST: RX ' in rx_msg:
                    msg_data = rx_msg.split('\"')[-2]
                    print(hex_to_chr(msg_data)+f"\n{usr}: ")

def chr_to_hex(string):
    return codecs.encode(string.encode(),'hex').decode()

def hex_to_chr(string):
    return codecs.decode(string, 'hex').decode()

def write2ser(mesg2write: str, serial=ser, delay=DELAY):
    serial.write(mesg2write.encode())
    time.sleep(delay)

listeting = threading.Thread(target=receive_msg, daemon=True)

if __name__ == "__main__":
    init()
    listeting.start()
    while True:
        msg = input(f"{usr}: ")
        msg = f"{usr} --> {msg}"

        send = True  #--- this set the send flag to True and ceases to send
        send_msg(chr_to_hex(msg))
        write2ser(RECV_MODE)
        send = False #--- ^^ restart listening of data
