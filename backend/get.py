from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
	{"id": 1, "name": "Alice", "age": 30},
]

class BaseAPI(BaseHTTPRequestHandler):
	def send_data(self, response_data, status=200):
		self.send_response(status)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps(response_data).encode())
	
	def do_GET(self):
		self.send_data(data)

def run():
	HTTPServer(('localhost', 3030), BaseAPI).serve_forever()

print('Starting server on http://localhost:3030')
run()