import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
#...............................
import socket
import threading

#>>>>>>>>>>>>>>
ACCESS_TOKEN=['CjLFB6kSr7o5rFW28NlN', 'jRCkLiRMdMEq7WzE8b2M']
                #Token of your device
broker="demo.thingsboard.io"   			    #host name
port=12348					    #data listening port
def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client1= paho.Client("control1")             #create client object
client1.on_publish = on_publish
                     #assign function to callback
             #access token from thingsboard device
#client1.connect(broker,port,keepalive=60)           #establish connection
#>>>>>>>>>>>>>>

port = 1883
curr= list()
def handle_client(c,addr):
    print(f"\n[NEW CONNECTION] {addr} connected")
    connected= True
    while connected:
        msg=c.recv(1024).decode()
        num = int( msg.split(".")[0] )
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
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        client1.username_pw_set(ACCESS_TOKEN[num-1] )
        client1.connect(broker,1883)
        
     
        if "Temperature" in msg:
         payload = "{" + "Temperature: " + msg.split(":")[1] + "}"

        elif "Humidity" in msg:
         payload = "{" + "Humidity: " + msg.split(":")[1] + "}"
        while not client1.is_connected():
         client1.loop() 
        ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
        print("Please check LATEST TELEMETRY field of your device")
        print(payload);
        time.sleep(5)
    
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
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
    s.bind(("192.168.0.44",port))
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





# import paho.mqtt.client as paho  		    #mqtt library
# import os
# import json
# import time
# from datetime import datetime
# #...............................
# import socket
# import threading

# #>>>>>>>>>>>>>>
# ACCESS_TOKEN='CjLFB6kSr7o5rFW28NlN'                 #Token of your device
# broker="demo.thingsboard.io"   			    #host name
# port=12348					    #data listening port
# def on_publish(client,userdata,result):             #create function for callback
#     print("data published to thingsboard \n")
#     pass
# client1= paho.Client("control1")             #create client object
# client1.on_publish = on_publish                     #assign function to callback
# client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
# #client1.connect(broker,port,keepalive=60)           #establish connection
# #>>>>>>>>>>>>>>

# port = 1883
# curr= list()
# def handle_client(c,addr):
#     print(f"\n[NEW CONNECTION] {addr} connected")
#     connected= True
#     while connected:
#         msg=c.recv(1024).decode()
#         print(f"\n[{addr}] {msg}")
#         if msg == 'CLOSE SOCKET':
#             connected=False
#             print(f"\nconnection with client with address {addr} terminated ")
#             print(f"\ncurrent number of client = {threading.activeCount()-1-1} .")
#             curr.remove(addr)
#             print(f"\n[current clients info]{curr}")

#         print(f"[{addr}]{msg}")
#         Capital_Sentence = msg.upper()
#         #print(Capital_Sentence)
#         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#         client1.connect(broker,1883)
#         if "Temperature" in msg:
#          payload = "{" + "Temperature: " + msg.split(":")[1] + "}"

#         elif "Humidity" in msg:
#          payload = "{" + "Humidity: " + msg.split(":")[1] + "}"
#         while not client1.is_connected():
#          client1.loop() 
#         ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
#         print("Please check LATEST TELEMETRY field of your device")
#         print(payload);
#         time.sleep(5)
#         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
#         c.send(Capital_Sentence.encode())
#     c.close()
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #def on_publish(client,userdata,result):             #create function for callback
#  #   print("data published to thingsboard \n")
# #    pass
# #client1= paho.Client("control1")                    #create client object
# #client1.on_publish = on_publish                     #assign function to callback
# #client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
# #client1.connect(broker,port,keepalive=60)           #establish connection


# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def main():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket successfully created")

#     # reserve a port on your computer in our
#     # case it is 12345 but it can be anything


#     # Next bind to the port
#     # we have not typed any ip in the ip field
#     # instead we have inputted an empty string
#     # this makes the server listen to requests
#     # coming from other computers on the network
#     s.bind(("192.168.0.44",port))
#     print("socket binded to %s" % (port))

#     # put the socket into listening mode
#     s.listen(5)
#     print("Server is listening on port ",(port))

#     # a forever loop until we interrupt it or
#     # an error occurs
#     while True:

#         # Establish connection with client.
#         c, addr = s.accept()
#         curr.append(addr)
#         thread=threading.Thread(target=handle_client , args=(c,addr))
#         #print(f"[Got connection from]", addr)
#         thread.start()
#         print(f"\n[CURRENT NUMBER OF CLIENTS ] {len(curr)} . ")
#         print(f"[current clients info]{curr}")

# #print('Got connection from', addr)

# if __name__=="__main__":
#     main()