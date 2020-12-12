import socket, sys, subprocess

def main(args):
    print("Host: " + args[1])
    host = args[1]
    print("Port: "+ str(args[2]))
    port = int(args[2])

    print( args[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 

    #name = input("What is your name?")

    while 1:
        #command = ("JOIN")
        #p1 = subprocess.Popen("command")
        #p2= subprocess.Popen("name|0")
        # message to be sent
        #msg = input('Chritopher|0|"\n"')
        # command = input("Hello, would you like to Join, Move, Shoot, Help, Quit", "\n")
        # if command == "MOVE" or command == "SHOOT":
        #     move = input("What room")
        # elif command == "HELP":
        #     move = 0
        # elif command == "QUIT":
        #     move = 0
        # elif command == "JOIN":
        #     move = 0
        # else:
        #     print("Please choice a choice from the list", "\n")
        # byte = 0
        # if command == "JOIN":
        #     commandline = command|name|byte
        # else:
        #     commanline = command|move|byte
        msg = input('Input command: ')  # "JOIN|Christopher|0"
        msg = msg + "\n"

        # Create socket and send message to host
       # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((host, port)) 
        s.send(msg.encode())

        # Print response
        resp = s.recv(1024).decode()  # "201|1,2,3|87\nWelcome to ... good luck
        parts = resp.split("\n")[0].split("|")
        print(parts) # [ "201", "1,2,3", "302" ]
        print("Response: %s" % str(resp))
        print(resp[-302:])
    # Close socket
    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    # pass host, port
    if len(sys.argv) >= 3:
        main(sys.argv)
    elif len(sys.argv) == 2:
        main([sys.argv[0], sys.argv[1], 9876])
    else:
        main([' ', 'localhost', 9876])
