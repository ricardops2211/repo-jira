import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8080))
ENV = os.environ.get("ENV", "cert")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"Hello from {ENV} environment! Path: {self.path}\n"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == "__main__":
    print(f"🚀 Starting server on port {PORT} in {ENV} mode...")
    server = HTTPServer(("", PORT), Handler)
    server.serve_forever()
