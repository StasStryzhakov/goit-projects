from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import pathlib
import urllib.parse
import mimetypes
import datetime
import json
from threading import Thread
import socket

BASE_PATH = pathlib.Path()
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000
BUFFER = 1024

def send_data_to_socket(body):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(body, (SERVER_IP, SERVER_PORT))
    client_socket.close()
    
class HTTPHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        send_data_to_socket(body)
        
        # json_file = BASE_PATH.joinpath('storage/data.json')
        # old_data = self.json_load(json_file)
        # payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
        # time = str(datetime.datetime.now())
        # old_data.update({time: payload})
         
        # self.json_save(json_file, old_data)
        
        self.send_response(302)
        self.send_header('Location', '/message')
        self.end_headers()
        
    # def json_save(self, file_name, data):
    #     with open(file_name, 'w', encoding='utf-8') as fd:
    #         json.dump(data, fd)
    
    # def json_load(self, file_name):
    #     try:
    #         with open(file_name, 'r', encoding='utf-8') as fd:
    #             data = json.load(fd)
    #         if data:
    #             return data
    #         else:
    #             return dict()
    #     except FileNotFoundError:
    #         print(f'No File {file_name}')
            
    
    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_file('index.html')
            case "/message":
                self.send_file('message.html')
            case _:
                content_file = BASE_PATH / route.path[1:]
                if content_file.exists():
                    self.send_file(content_file)
                else:
                    self.send_file('error.html', 404)
    
    
    def send_file(self, file_name, status_code=200):
        self.send_response(status_code)
        mimi_type, *res = mimetypes.guess_type(file_name)
        
        if mimi_type:
            self.send_header('Content-Type', mimi_type)
        else:
            self.send_header('Content-Type', 'text/plain')
            
        self.end_headers()
        
        with open(file_name, 'rb') as fpage:
            self.wfile.write(fpage.read())
    
    # def send_static(self, file_name, status_code=200):
    #     self.send_response(status_code)
    #     self.send_header('Content-Type', 'text/html')
    #     self.end_headers()
        
    #     with open(file_name, 'rb') as fpage:
    #         self.wfile.write(fpage.read())
  
def save_data(data):
    # json_file = BASE_PATH.joinpath('storage/data.json')
    # old_data = self.json_load(json_file)
    # payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
    # time = str(datetime.datetime.now())
    # old_data.update({time: payload})
        
    # self.json_save(json_file, old_data)
    body = urllib.parse.unquote_plus(data.decode())
    
    try:
        json_file = BASE_PATH.joinpath('storage/data.json')
        data = load_data(json_file)
        payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}
        time = str(datetime.datetime.now())
        data.update({time: payload})
        with open(json_file, 'w', encoding='utf-8') as fd:
            json.dump(data, fd, ensure_ascii=False)
    except ValueError as err:
        logging.error(f"Field parse data {body} with error {err}")
    except OSError as err:
        logging.error(f"Field write data {body} with error {err}")
        
def load_data(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as fd:
                data = json.load(fd)
                if data:
                    return data
                else:
                    return dict()
        except FileNotFoundError:
            logging.error(f"No file {file_name}")  
                              
def run(server=HTTPServer, handler=HTTPHandler):
    adress = ('', 3000)
    http_server = server(adress, handler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()

def run_socket_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    server_socket.bind(server)
    try:
        while True:
            data, address = server_socket.recvfrom(BUFFER)
            save_data(data)
    except KeyboardInterrupt:
        logging.info('Socket server stopped')
    finally:
        server_socket.close()
    
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    
    thread_server = Thread(target=run)
    thread_server.start()
    thread_socket = Thread(target=run_socket_server(SERVER_IP, SERVER_PORT))
    thread_socket.start()