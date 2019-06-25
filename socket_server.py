import socket
import requests

HOST = input("Enter IP of your device: ")  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            dataAsStr = str(data).replace("'", "")
            dataAsStr = str(dataAsStr).replace("b", "")
            print(dataAsStr)
            response = requests.get('http://adil210.beget.tech/get.php?sum=' + dataAsStr, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
