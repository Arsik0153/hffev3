import socket
import requests

HOST = '192.168.100.38'  # Standard loopback interface address (localhost)
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
            #if(dataAsStr[0] == "C"):
            #    response = requests.get('http://test.docchaika.kz/get.php?carCount=' + dataAsStr[1::], headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
            #if(dataAsStr[0] == "T"):
            #    response = requests.get('http://test.docchaika.kz/get.php?min=' + dataAsStr[1::], headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})