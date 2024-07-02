import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Kapcsolat megszakadt.")
            client_socket.close()
            break


def send_messages(client_socket, client_id):
    while True:
        message = input()
        full_message = f"[{client_id}]: {message}"
        client_socket.send(full_message.encode())


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5555))

    client_id = input("Add meg az azonosítódat: ")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(
        target=send_messages, args=(client_socket, client_id)
    )
    send_thread.start()


if __name__ == "__main__":
    start_client()
