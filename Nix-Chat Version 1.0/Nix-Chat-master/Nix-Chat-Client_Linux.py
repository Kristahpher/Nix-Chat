#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import messagebox


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
######


alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','0','"','#','$','%','&','\',','()','.','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\','] 

def primeNumbers(a,m):
    for i in range(2,m+1):
        if m % i == 0 and a % i == 0:
            return False
    return True

#This function will convert the first given keyword and convert it to a number 
def firstConvert(text):
    textList = []
    total = 0
    index = 0
    for i in range(len(text)):
    #Changes each letter in the given keyword to a number and combines them
        a = (ord(text[i]))
        textList.append(a)

    while index < len(textList):
        total = total + textList[index]
        index = index + 1
        total1 = total * total
    return total1

#This function will convert the second given keyword and convert it to a number       
def secondConvert(text):
    textList = []
    total = 0
    index = 0
    for i in range(len(text)):
    #Changes each letter in the given keyword to a number and combines them
        a = (ord(text[i]))
        textList.append(a)

    while index < len(textList):
        total = total + textList[index]
        index = index + 1
        total1 = total * total
    return total1

#This function will taken the number given from the conversion above
#This also calculates all of the prime numbers with the range of the Given Number to Given Number - 100, Example: Range between 10238 and 10138.
def calcPrime(givenNumber):
    lower = givenNumber - 100
    upper = givenNumber
    primeList = []
    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
                primeList.append(num)
    return primeList

#This fucntion takes all of the prime number produces in the function above and returns the highest prime number found 
def highestPrime(primeList):
    max = 0
    for i in primeList:
        if i > max:
            max=i
            max1 = max
    return max1

#Affine Cipher Encryption Code
def affine(a,b,m,plaintext):
    prime = primeNumbers(a,m)
    if prime == False:
        print("")
    else:
        ciphertext = ""
        for i in range(len(plaintext)):
            letter = plaintext[i]
            p = alphabet.index(letter)
            cipherNum = (a * p + b)% m 
            cipherLetter = alphabet[cipherNum]
            ciphertext = ciphertext + cipherLetter
        
        return ciphertext

#This is used for decrypting the cipher text
def inverse(a,m):
    x = 0
    for x in range(m):
        b = (a*x)%m
        if b == 1:
            return x
#Affine Cipher Decryption code
def decryptMessage(a,b,m,ciphertext):
    x = inverse(a,m)
    if inverse == '':
        print("")
    else:
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

#Function that is set to the button to encrypt the message
def clickedEncryption():
    m=26
    text = num1.get()
    text2 = num2.get()
    s1 = firstConvert(text)
    s2 = secondConvert(text2)
    c1 = calcPrime(s1)
    c2 = calcPrime(s2)
    a = highestPrime(c1)
    a2 = highestPrime(c2)
    prime = primeNumbers(a,m)
    prime2 = primeNumbers(a2,m)
    plaintext = entry_field.get()
    encryption = affine(a,a2,m,plaintext)
    msg = encryption
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
   


#Function that is set to the button to decrypt the message
def clickedDecryption():
    m=26
    tabs = 0
    text = num1.get()
    text2 = num2.get()
    s1 = firstConvert(text)
    s2 = secondConvert(text2)
    c1 = calcPrime(s1)
    c2 = calcPrime(s2)
    a = highestPrime(c1)
    a2 = highestPrime(c2)
    prime = primeNumbers(a,m)
    prime2 = primeNumbers(a2,m)
    ciphertext = entry_field.get()
    decryption = decryptMessage(a,a2,m,ciphertext)
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Information",decryption)




#########
top = tkinter.Tk()
top.title("Nix-Chat")
top.configure(bg='navy')
top.geometry('475x420')

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

entry_field.place(x=30, y=297)
num1.place(x=30, y=342)
num2.place(x=30, y=387)


send_button = tkinter.Button(top,bg='black', fg='gold',text="  Send Message  ", command=send)
encryption = tkinter.Button(top,bg='black', fg='firebrick1',text="Encrypt Message", command=clickedEncryption)
decryption = tkinter.Button(top,bg='black',fg='green3', text="Decrypt Message", command=clickedDecryption)
send_button.place(x=309, y=290)
encryption.place(x=309, y=335)
decryption.place(x=309, y=380)


messageLabel = tkinter.Label(top,bg='black',fg='white',height = 1, width = 10, text="Type Here!")
keyword1Label = tkinter.Label(top,bg='black',fg='white',height = 1, width = 10, text="Keyword 1")
keyword2Label = tkinter.Label(top,bg='black',fg='white',height = 1, width = 10, text="Keyword 2")

messageLabel.place(x=70,y=275)
keyword1Label.place(x=70,y=320)
keyword2Label.place(x=70,y=365)

top.protocol("WM_DELETE_WINDOW", on_closing)

#Socket part
HOST = '127.0.0.1'#'142.93.191.161' # Enter host of the server without inverted commas 
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # for start of GUI  Interface
