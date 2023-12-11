import socket
import sys
import time

def main():
    server_name = "localhost"
    server_port = 7894
    message_filename = "med/message2.txt"
    signature_filename = "med/signature2.txt"
    # server_name = sys.argv[1]
    # server_port = int(sys.argv[2])
    # message_filename = sys.argv[3]
    # signature_filename = sys.argv[4]
    # Open the message file and read data
    with open(message_filename, "r") as message_file:
        lines = message_file.readlines()
    # Filter out lines that are just numbers
        messages = [line for line in lines if not line.strip().isdigit() and line != '\n']
        #print(f"Message:\n{messages}\n")


    # Open the signature file and read data
    with open(signature_filename, "r") as signature_file:
        signatures = [line.strip() for line in signature_file]
    #print(f"Signature:\n{signatures}\n")

    # Create a TCP socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_name, server_port))

        # Send a "HELLO" message to the server
        client_socket.sendall(b"HELLO\n")
        print("HELLO")
        response = client_socket.recv(1024).decode('utf-8').strip()
        print(f"Server Response: {response}")
        if response != "260 OK":
            print("Error: Server response is not '260 OK'")
            sys.exit(1)

        for message in messages:
            # Send the "DATA" command to the server
            client_socket.send(b"DATA\n")
            print("DATA")
            time.sleep(0.1)

            # Send the message length followed by the message itself and the end character
            message_length = str(len(message.strip())+1)
            client_socket.send(message_length.encode() + b"\n")
            time.sleep(0.1)
            client_socket.send(message.encode())
            time.sleep(0.1)
            client_socket.send(b".\n")  # termination of the message
            response = client_socket.recv(1024).decode().strip()
            print(f"Raw Server Response: {response}")

            if response != "270 SIG":
                print("Error: Server response is not '270 SIG'")
                sys.exit(1)
            
            received_signature = client_socket.recv(1024).decode().strip()
            print(f"Received Signature: {received_signature}")

            if received_signature in signatures:
                client_socket.send(b"PASS\n")
            else:
                client_socket.send(b"FAIL\n")
            
            response = client_socket.recv(1024).decode().strip()
            print(f"Response = {response}\n")

        # Send a "QUIT" message to the server
        client_socket.send(b"QUIT\n")
        return

if __name__ == "__main__":
    main()