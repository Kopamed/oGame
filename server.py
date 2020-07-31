import socket as st
from _thread import *
import sys
from player import Player
import pickle


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




players = [Player(0,0,50,50,(255,0,0)), Player(450,450,50,50,(0,0,255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            #reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending: ", reply)
                
            conn.sendall(pickle.dumps(reply))
            
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