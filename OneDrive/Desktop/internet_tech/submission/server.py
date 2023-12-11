import socket
import hashlib
import sys

def main():
    listen_port = 7894
    key_file_path = "med/key.txt"
    #listen_port = int(sys.argv[1])
    #key_file_path = sys.argv[2]
    keys = []

    # Read in all the keys from the key file
    with open(key_file_path, "r") as key_file:
        for line in key_file:
            keys.append(line.strip())

    # Create a TCP socket and bind to the given port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("", listen_port))
        server_socket.listen(1)

        print(f"Server listening on port {listen_port}")

        client_socket, client_addr = server_socket.accept()
        client_socket.settimeout(10)  # Set a 10-second timeout
        print(f"Connection from {client_addr}")

        request = client_socket.recv(1024).decode("ascii").strip()
        if request == "HELLO":
            client_socket.sendall(b"260 OK\n")
        else:
            print("Error: Invalid request.")
            client_socket.close()
            return
        
        key_counter = 0  # Add a counter for the keys

        while True:
            command = client_socket.recv(1024).decode("ascii").strip()

            if command == "DATA":
                sha256_hash = hashlib.sha256()
                
                while True:
                    # Receive the length of the message
                    message_length_line = client_socket.recv(1024).decode('ascii').strip()
                    #print(f"Received message length: {message_length_line}")  # Diagnostic print

                    if message_length_line == ".":
                        break

                    # Receive the actual message based on the length provided
                    message_length = int(message_length_line)
                    message = client_socket.recv(message_length).decode('ascii').strip()
                    #print(f"Received message: {message}")  # Diagnostic print
                    
                    sha256_hash.update(message.encode())

                # Add the appropriate key from the list to the hash
                sha256_hash.update(keys[key_counter].encode())  # Use the key corresponding to the current message
                key_counter += 1  # Increment the key counter for the next message

                signature = sha256_hash.hexdigest()

                client_socket.send(b"270 SIG\n")
                client_socket.send(signature.encode() + b"\n")

                response = client_socket.recv(1024).decode().strip()
                print(f"Client Validation: {response}")

                if response not in ["PASS", "FAIL"]:
                    print("Error: Invalid response from client.")
                    client_socket.close()
                    return

                client_socket.send(b"260 OK\n")

            elif command == "QUIT":
                client_socket.close()
                print("Connection closed.")
                return

            else:
                print("Error: Invalid command received.")
                client_socket.close()
                return

if __name__ == "__main__":
    main()