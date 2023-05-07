import socket
# means create a phone 
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# means dial the phone 
my_socket.connect("data.pr4e.org" , 80)
#encode means that send the data in UTF-8 format because python uses in unicode
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
# sending the request means that the browser wants to talk first in a phone call
my_socket.send(cmd)
# this loop means 
while True:
    # continiue reciving data up to 512 charachter, if the server or the connection is slow, it's gonna  wait to get all the 512 charachters 
    data = my_socket.recv(512)
    # if no data is recieved 
    if len(data) < 1:
        # stop reciving it, by breaking the loop
        break
    # print the recieved data in uni code so it's visible in python
    print(data.decode(), end='')
