import http.server
import socketserver
import vars
from http import HTTPStatus
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('server_requests_total', 'Количество запросов к приложению')


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(vars.http_message)

start_http_server(vars.prometheus_port)
httpd = socketserver.TCPServer(('', vars.external_port), Handler)
httpd.serve_forever()