import socket
import threading
import ssl
import requests

class secure_proxy:
     def _init_(self, host='102.0.11.108',port=8080):
             self.host = host
             self.port = port


     def start(self):
             server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             server_socket.bind((self.host, self.port))
             server_socket.listen(5)
             print(f'Secure_Proxy Server running on {self.host}:{self.port}')

             while True:
              client_socket, addr = server_socket.accept()
              print(f' Connection fromm {addr}')
              threading.Thread(target=self.handle_client, args=(client_socket,)).start()

     def handle_client(self, client_socket):
              request = client_socket.recv(4096)
              url = self.extract_url(request)
              if url:
                 response = self.fetch_url(url)
                 client_socket.sendall(response)
              client_socket.close()

     def extract_url(self, request):
         try:
              request_line = request.decode().splitlines()[0]
              url = request_line.split('')[1]
              return url
         except IndexError:
              return None

     def fetch_url(self, url):
         try:
              reponse = request.get(url, verify=False)
              return reponse.content
         except requests.RequestException as e:
              print(f'Error fetching URL: {e}')
              return b'HTTP/1.1 500 Internal Sidaaaaa'

if __name__=='__main__':
         proxy = secure_proxy()
         proxy.start()
