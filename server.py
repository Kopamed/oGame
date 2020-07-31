import socket as st
from _thread import *
import sys


server = "100.115.92.203"
port = 5555

print("Starting server...")
s = st.socket(st.AF_INET, st.SOCK_STREAM)

try:
    s.bind((server, port))
except st.error as e:
    str(e)
    
s.listen()
print("Server started succesfully!")
print("Waiting for a connection...")


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0])+","+str(tup[1])


pos = [(0,0), (100,100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            #reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)
                
            conn.sendall(str.encode(make_pos(reply)))
            
        except:
            break
        
    print("Lost connection") 
    conn.close()
            
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1