#banner grabber by iTryZz
import socket
from optparse import OptionParser
import sys

def creds():
    print("""
    +> Banner grabber by iTryZz<+
    (Type exit to exit)
    """)

creds()

def loop():
    target = input("<+ Target IP +>> ")
    if target == "exit":
        sys.exit("Exiting:\nBanner Grabber by iTryZz\nThank you.")
    try:
        port = int(input("<+ Target Port +>> "))
        if port == "exit":
            sys.exit("Exiting:\nBanner Grabber by iTryZz\nThank you.")
    except ValueError:
        sys.exit("Error!\nOnly enter one port at a time!\nIm too lazy to make better code!!!")
    else:
        print(f"Grabbing banners for {target} on port {port}")
        try:
            s = socket.socket()
            s.connect((target, port))
            s.send("+> Banner grabber by V01D <+".encode())
            result = s.recv(1024).decode()
            print(result)
            print("") # Newline
            loop()
        except socket.error as err:
            print(f"Target ?__({target})__? on ?__{port}__? does not respond to my requests.\nIt is either closed, or configured correctly...\n")
            loop()

loop()

