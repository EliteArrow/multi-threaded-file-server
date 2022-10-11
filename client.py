from cgitb import handler
from http import client
import os
import select
from pathlib import Path
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 6645
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_dir"
CLIENT_DATA_PATH = "client_dir"

 
def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split('@')

        if cmd == "OK":
            print(f"{msg}")
        elif cmd == "DISCONNECTED":
            print(f"{msg}")
            break
        
        data = input("> ")
        data = data.split(" ")
        cmd = data[0]
        if(cmd == "upload"):
            path = CLIENT_DATA_PATH +"/" + data[1]
            with open(f"{path}","r") as f:
                text = f.read()
                filename = path.split("/")[-1]
                send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))
        elif cmd == 'download':
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            ready = select.select([client], [], [], 1)[0]
            if ready:
                recdata = client.recv(SIZE)
                p = Path(f'client_dir/{data[1]}')
                p.write_bytes(recdata)
                continue;
            else:
                print("Time Limit Excedded")
        elif cmd == 'rename':
            send_data = f"{cmd}@{data[1]}@{data[2]}"
            client.send(send_data.encode(FORMAT))
        elif cmd == 'delete': 
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
    
    print("Disconnected from Server.")
    client.close()
if __name__ == "__main__":
    main()