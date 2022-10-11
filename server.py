from ast import Str
from pathlib import Path
from cgitb import handler
from fileinput import filename
import os
import socket
import  threading
from xmlrpc.client import SERVER_ERROR 

IP = socket.gethostbyname(socket.gethostname())
PORT = 6645
FORMAT = "utf-8"
ADDR = (IP,PORT)
SIZE = 1024
SERVER_DATA_PATH = "server_dir"

def helperThread(conn,addr):
    print(f"{addr} Connected.")
    conn.send("OK@Welcome to the File Server. Smit".encode(FORMAT))
    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == 'upload':
            name = data[1]
            text = data[2]
            filepath = os.path.join(SERVER_DATA_PATH,name)
            with open(filepath,"w") as f:
                f.write(text)
            send_data = "OK@File Uploaded."
            conn.send(send_data.encode(FORMAT))

        elif cmd == 'rename':
            send_data = "OK@"
            filename = data[1]
            newfilename = data[2]

            files = os.listdir(SERVER_DATA_PATH)
            if len(files) == 0:
                send_data += "The server directory is empty." 
            else:
                if filename in files:
                    os.rename(f"{SERVER_DATA_PATH}/{filename}",f"{SERVER_DATA_PATH}/{newfilename}")
                    send_data+="File Renamed."
                else:
                    send_data+="File Not Found."
            conn.send(send_data.encode(FORMAT))

        elif cmd == 'download':
            filename = data[1]
            file = Path(f"{SERVER_DATA_PATH}/{filename}")
            if file.is_file():
                conn.send(file.read_bytes())
                print(f"Downloaded '{filename}'")

        elif cmd == 'delete':
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"
            filename = data[1]

            if len(files) == 0:
                send_data += "The server directory is empty." 
            else:
                if filename in files:
                    os.remove(f"{SERVER_DATA_PATH}/{filename}")
                    print(f"{SERVER_DATA_PATH}/{filename}")
                    send_data+="File Deleted."
                else:
                    send_data+="File Not Found."
            conn.send(send_data.encode(FORMAT))

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server Active")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=helperThread,args = (conn,addr))
        thread.start()

if __name__ == "__main__":
    main()