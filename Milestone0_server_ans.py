import socket
import threading

port = 12345
curr= list()
def handle_client(c,addr):
    print(f"\n[NEW CONNECTION] {addr} connected")
    connected= True
    while connected:
        msg=c.recv(1024).decode()
        print(f"\n[{addr}] {msg}")
        if msg == 'CLOSE SOCKET':
            connected=False
            print(f"\nconnection with client with address {addr} terminated ")
            print(f"\ncurrent number of client = {threading.activeCount()-1-1} .")
            curr.remove(addr)
            print(f"\n[current clients info]{curr}")

        print(f"[{addr}]{msg}")
        Capital_Sentence = msg.upper()
        #print(Capital_Sentence)
        c.send(Capital_Sentence.encode())
    c.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything


    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(("172.20.10.14",port))
    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(5)
    print("Server is listening on port ",(port))

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with client.
        c, addr = s.accept()
        curr.append(addr)
        thread=threading.Thread(target=handle_client , args=(c,addr))
        #print(f"[Got connection from]", addr)
        thread.start()
        print(f"\n[CURRENT NUMBER OF CLIENTS ] {len(curr)} . ")
        print(f"[current clients info]{curr}")

#print('Got connection from', addr)

if __name__=="__main__":
    main()