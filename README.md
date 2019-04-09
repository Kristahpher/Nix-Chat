# Nix-Chat (v1.10 is out. Read bottom for details)
Nix Chat is a Python Chatroom application that allows users to have encrypted chats on a local or hosted server. Nix Chat uses a modified verison of the Affine cipher that I developed(check Nix Encoder on my page for more details) to have encrypted messaging between users. Nix Chat also offers options for users to make a username once connected to a server.  


# Running Nix Chat Server on the VPS
First, create a cheap vps from any reputable site (I used the cheapest Ubuntu 18.01 server on Digital Ocean but any vps should be fine).

Next, install python3 and pip to the server. I used this link for my vps. 
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-18-04-server

Once that is complete, clone the repo to the vps. 
''git clone https://github.com/Kristahpher/Nix-Chat''

cd into the directory and run python3 Nix-Chat_Server.py

# Running Nix Chat Client(On Linux)
Run the given python-to-exe Nix-Chat_Linux file in the repo

Or

Open the code in the Python Idle and run the code.

Or

Compile the source code with your own python converter

*NOTE: You will need to change the IP of the 'HOST' at the bottom of the code to the server IP you have

# Running Nix Chat Client(On Windows)
Run the given python-to-exe Nix-Chat_Windows file in the repo 

Or

Open the code in the Python Idle and run the code

Or

Compile the source code with py to exe or anyother option

*NOTE: You will need to change the IP of the 'HOST' at the bottom of the code to the server IP you have

# Nix-Chat Version 1.10 is now released!
Nix-Chat Version 1.10 is out with lots of optimization to the code, removing almost half the codebase. Nix Chat now uses a modified Fletcher32 checksum algorithm to take the keywords given, and generates very long prime number. Both of the keywords are passed through the Fletcher32 algorithm to generate the prime numbers needed for the Affine Cipher algorithm. Using this method, it will now generates prime numbers 25 to 50 times the size of the previous methods used and it takes virtually the same time to generate. This in returns makes Nix Chat that much more secure to use!!! You can see the image folder to see the comparsion.


IMPORTANT- The server code used in Nix Chat is a clone/remake of sachans's Chat App on Github. I changed around all of the UI, some of the server connection setting, and added the option for encrypted chatting for users. If you want the original source code for the server, visit sachan's github page
