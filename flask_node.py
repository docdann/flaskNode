from flask import Flask
import socket
import threading
import time

app = Flask(__name__)

def broadcast_presence():
    port = 37020  # UDP port for broadcasting
    server_address = ('<broadcast>', port)
    message = b'I am a Flask server'
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        try:
            # Send data
            print(f"Broadcasting: {message}")
            sock.sendto(message, server_address)
        except Exception as e:
            print(f"Broadcasting failed: {e}")
        time.sleep(10)  # Pause for 10 seconds before next broadcast

def listen_for_servers():
    port = 37020  # Same port as the broadcaster

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', port)
    sock.bind(server_address)

    while True:
        print('\nWaiting to receive message...')
        data, address = sock.recvfrom(4096)

        print(f"Received {len(data)} bytes from {address}")
        print(data)

        if data:
            print(f"Received message from another Flask server: {data}")

@app.route('/')
def home():
    return "Hello, I'm a Flask server!"

if __name__ == '__main__':
    # Run the listener in a separate thread
    threading.Thread(target=listen_for_servers, daemon=True).start()
    # Run the broadcaster in a separate thread
    threading.Thread(target=broadcast_presence, daemon=True).start()
    # Start Flask app
    app.run(host='0.0.0.0', port=5000)
