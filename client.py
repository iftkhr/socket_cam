import socket, cv2, pickle, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.169.0.161", 2222)) #change ip accordingly

data = b""
size = struct.calcsize("Q")

while True:

    while len(data) < size:
        msg = s.recv(1024)
        if not msg: break
        data += msg

    pckd_msg = data[:size]
    data = data[size:]
    msg_size = struct.unpack("Q", pckd_msg)[0]

    while len(data) < msg_size:
        data += s.recv(1024)

    frm_data = data[:msg_size]
    data = data[msg_size:]
    frm = pickle.loads(frm_data)
    cv2.imshow("Receiving... (Press 'z' to end)", frm)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('z'): break

s.close()

    

