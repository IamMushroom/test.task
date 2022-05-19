import http.server
import socketserver
import time
import vars
from http import HTTPStatus
from prometheus_client import start_http_server
from prometheus_client import Counter, Summary

REQUESTS = Counter('server_requests_total', 'Количество запросов к приложению')
LATENCY = Summary('server_latency_seconds', 'Время обработки страницы')

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        time_request = time.time()
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(vars.http_message)
        time_responce = time.time()
        REQUESTS.inc()
        LATENCY.observe(time_responce - time_request)


start_http_server(vars.prometheus_port)
httpd = socketserver.TCPServer(('', vars.external_port), Handler)
httpd.serve_forever()
