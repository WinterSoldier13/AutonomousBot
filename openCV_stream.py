'''This code will rest on Pi and will receive command from the PC and will then forward the command to Arduino'''


'''This is the code on the Raspberry Pi'''

import socket
import serial


HOST = '192.168.43.22'  # Standard loopback interface address (localhost)
PORT = 1315        # Port to listen on (non-privileged ports are > 1023)


ser = serial.Serial('/dev/ttyACM0')
ser.flush()





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('Listening')
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        while True:
            data = conn.recv(1024)
            conn2, addr = s.accept()
            data = conn2.recv(1024)
            if(len(repr(data))) > 4:
                data = repr(data)[2:len(repr(data))-1]
                data = str(data)         # convering the received data to String
                print(data)
                ser.write(data.encode())
                
               





