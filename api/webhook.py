from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('content-length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            print("Webhook Received:", data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Webhook received"}).encode())

        except Exception as e:
            print("Error:", e)
            self.send_response(500)
            self.end_headers()
