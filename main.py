from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer



def run( server_class = HTTPServer, handler_class = BaseHTTPRequestHandler):
    _port: int = 8000
    server_address = ("", _port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except:
        httpd.server_close()

class HttpGetHandler(BaseHTTPRequestHandler):
    _httpCodes: int = 200
    def do_GET(self):
        self.send_response(self._httpCodes)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><meta charset='utf-8'>".encode())
        self.wfile.write("<title>Just HTTP-server.</title></head>".encode())
        self.wfile.write("<body>A GET request was received</body></html>".encode())


run(handler_class = HttpGetHandler)