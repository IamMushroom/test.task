import http.server
import socketserver
from http import HTTPStatus
import vars

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(vars.http_message)

httpd = socketserver.TCPServer(('', vars.external_port), Handler)
httpd.serve_forever()