from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World")

server = HTTPServer(("localhost", 8000), HelloHandler)
print("Server running at http://localhost:8000")
server.serve_forever()
