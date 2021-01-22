import socket, cv2, pickle, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname() + '.local'), 2222))
s.listen(5)
print("Server IP:", socket.gethostbyname(socket.gethostname() + '.local'))

while True:
    clnt, adr = s.accept()
    print (f"Connection to {adr} established")

    if clnt:
        vid = cv2.VideoCapture(0)

        while(vid.isOpened()):
            img, frm = vid.read()
            a = pickle.dumps(frm)
            msg = struct.pack("Q", len(a)) + a
            clnt.sendall(msg)

    clnt.close()
