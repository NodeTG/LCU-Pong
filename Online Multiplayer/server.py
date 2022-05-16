# Stolen from https://github.com/techwithtim/Network-Game-Tutorial/blob/master/server.py - Thanks Tim ;)

import socket
from _thread import *
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = [(0,0), (310,0)]
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(4096)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                #print("Recieved: " + reply)
                arr = json.loads(reply)
                id = int(arr["id"])

                if arr["type"] == "POS_UPDATE":
                    pos[id] = (arr["pos"][0], arr["pos"][1])
                else:
                    print("Unknown message received!")

                if id == 0: nid = 1
                if id == 1: nid = 0

                data = {
                    "id": nid,
                    "type": "POS_UPDATE",
                    "pos": pos[nid],
                    }

                reply = json.dumps(data)
                #print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))