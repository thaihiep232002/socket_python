import socket
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
SERVER_PORT = 5455
SERVER_HOST = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_HOST,SERVER_PORT))
if client.recv(1024).decode("utf-8") == "accepted":
    print(f"connected with {SERVER_HOST}")

while True:
    is_success = False
    print("1. Login: ")
    print("2. Regis: ")
    check = input("Select: ")
    if check == "1":#select login
        # login
        while True:
            # clear() # clear screen
            client.sendall("login".encode("utf-8"))
            username = input("Username: ")
            client.sendall(username.encode("utf-8"))
            password = input("Password: ")
            client.sendall(password.encode("utf-8"))
            if client.recv(1024).decode("utf-8") == "login_success":
                print("logged success!")
                is_success = True
                break
            else:
                print("fail success!")
    elif check == "2":#select registered
        # regis
        while True:
            clear()
            client.sendall("regis".encode("utf-8"))
            username = input("Username: ")
            client.sendall(username.encode("utf-8"))
            password = input("Password: ")
            client.sendall(password.encode("utf-8"))
            if client.recv(1024).decode("utf-8") == "regis_success":
                print("registered success!")
                break
    if is_success == True:
        break

while True:
    data_client = input("Client: ")
    client.sendall(data_client.encode("utf-8"))
    if data_client == "quit":
        client.close()
        break
    data_server = client.recv(1024).decode("utf-8")
    print(f"Server: {data_server}")
    if data_server == "quit":
        client.close()
        break

    
    


