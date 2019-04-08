#!/usr/bin/env python3
import sympy
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import messagebox

alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','0','"','#','$','%','&','\',','()','.','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\',']

#Flecter32 checksum algorithm to generate a very large number
#Using the Sympy library to get the next prime number after generating the checksum 
def flecterAlgo(inString):
    aList=[]
    bList = []
    bList.append(0)

    for i in range(len(inString)):
        charNum = (ord(inString[i]))
        aList.append(charNum)
        
    for i in range(len(aList)):
        bList.append(bList[i] + aList[i])
        
    checksum = sum(bList)
    
#Performing the Bitwise algorithms to the final checksum
    finalCheckSum = checksum << 1000 | max(bList)
    prime = sympy.nextprime(finalCheckSum)
    
    return prime

#This is used for decrypting the cipher text
def inverse(a,m):
    x = 0
    for x in range(m):
        b = (a*x)%m
        if b == 1:
            return x
        
#Affine Cipher Encryption Code
def affineEncrypt(a,b,m,plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        p = alphabet.index(letter)
        cipherNum = (a * p + b)% m 
        cipherLetter = alphabet[cipherNum]
        ciphertext = ciphertext + cipherLetter
    return ciphertext

#Affine Cipher Decryption Code
def affineDecrypt(a,b,m,ciphertext):
    x = inverse(a,m)
    plaintext = ''
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        c = alphabet.index(letter)
        plainNum = (x * (c - b))% m
        plaintextLetter = alphabet[plainNum]
        if alphabet[plainNum] == 0:
            plaintext = plaintext + ' '
        else:
            plaintext = plaintext + plaintextLetter
    return plaintext

def clickedEncryption():
    m=50
    keyword = num1.get()
    keyword2 = num2.get()
    a = flecterAlgo(keyword)
    a2 = flecterAlgo(keyword2)
    plaintext = entry_field.get()
    encryption = affineEncrypt(a,a2,m,plaintext)
    msg = encryption
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))

def clickedDecryption():
    m=50
    keyword = num1.get()
    keyword2 = num2.get()
    a = flecterAlgo(keyword)
    a2 = flecterAlgo(keyword2)
    ciphertext = entry_field.get()
    decryption = affineDecrypt(a,a2,m,ciphertext)
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Information",decryption)
    
##################
#   Message code #
##################
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  
            break

def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "exit":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("exit")
    send()

##################
#Tkinter UI Stuff#
##################
top = tkinter.Tk()
top.title("Nix-Chat")
top.configure(bg='navy')
top.geometry('425x425')

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
# this will contain the messages.
msg_list = tkinter.Listbox(messages_frame,bg='lightcyan', height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
num1 = tkinter.Entry(top)
num2 = tkinter.Entry(top)

entry_field.bind("<Return>", send)
num1.bind("<Return>", send)
num2.bind("<Return>", send)

entry_field.place(x=50, y=297)
num1.place(x=50, y=342)
num2.place(x=50, y=387)

send_button = tkinter.Button(top,bg='black', fg='gold',text="  Send Message  ", command=send)
encryption = tkinter.Button(top,bg='black', fg='firebrick1',text="Encrypt Message", command=clickedEncryption)
decryption = tkinter.Button(top,bg='black',fg='green3', text="Decrypt Message", command=clickedDecryption)
send_button.place(x=275, y=290)
encryption.place(x=275, y=335)
decryption.place(x=275, y=380)

messageLabel = tkinter.Label(top,bg='black',fg='white',height = 1, width = 10, text="Type Here!")
keyword1Label = tkinter.Label(top,bg='black',fg='white',height = 1, width = 10, text="Keyword 1")
keyword2Label = tkinter.Label(top,bg='black',fg='white',height = 1, width = 10, text="Keyword 2")

messageLabel.place(x=75,y=275)
keyword1Label.place(x=75,y=320)
keyword2Label.place(x=75,y=365)

top.protocol("WM_DELETE_WINDOW", on_closing)

###################
#Socket connection#
###################

HOST = '' # Enter host of the server without inverted commas 
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # for start of GUI  Interface
