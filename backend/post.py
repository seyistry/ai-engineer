from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = []

class BaseAPI(BaseHTTPRequestHandler):
	def send_data(self, response_data, status=201):
		self.send_response(status)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps(response_data).encode())
	
	def do_POST(self):
		content_size = int(self.headers['Content-Length'], 0)
		parsed_data = self.rfile.read(content_size)

		post_data = json.loads(parsed_data)
		data.append(post_data)

		self.send_data({"message": "Data received", "data": post_data})

def run():
	HTTPServer(('localhost', 3030), BaseAPI).serve_forever()

print('Starting server on http://localhost:3030')
run()

		