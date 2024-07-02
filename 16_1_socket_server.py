import socket
import threading

clients = {}
client_id_counter = 0


def broadcast(message, sender_client_socket):
    for client_socket, client_id in clients.items():
        if client_socket != sender_client_socket:
            try:
                client_socket.send(message.encode())
            except:
                client_socket.close()
                del clients[client_socket]


def handle_client(client_socket, client_id):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            broadcast(f"[{client_id}]: {message}", client_socket)
        except:
            client_socket.close()
            del clients[client_socket]
            break


def start_server():
    global client_id_counter
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5555))
    server_socket.listen()

    print("Szerver elindult és figyel a 5555 porton...")

    while True:
        client_socket, addr = server_socket.accept()
        client_id_counter += 1
        client_id = f"Client{client_id_counter}"
        clients[client_socket] = client_id
        print(f"Kapcsolódott: {addr} azonosítóval {client_id}")
        thread = threading.Thread(target=handle_client, args=(client_socket, client_id))
        thread.start()


if __name__ == "__main__":
    start_server()
