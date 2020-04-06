from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        print("Received POST body:")
        print(body)

        self.send_response(201)
        self.end_headers()


srv = HTTPServer(("0.0.0.0", 5000), Handler)
srv.serve_forever()
