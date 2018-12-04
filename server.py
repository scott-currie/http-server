from cowpy import cow
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    """

    def do_GET(self):
        """
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            # Query the DB here - Then format your response
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Welcome to our site.')
            return

        if parsed_path.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                b'<html><body><h1>hello world!</h1></body></html>')
            return

        self.send_response(404)
        self.end_headers()

    def do_HEAD(self):
        """
        """
        pass

    def do_POST(self):
        """
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        print(parsed_qs)
        if parsed_path.path == '/cow':
            if 'msg' in parsed_qs:
                cowpied = cowpyify(parsed_qs['msg'][0])
                json_string = json.dumps({'content': cowpied})
                self.send_response(201)
                self.end_headers()
                self.wfile.write(json_string.encode())
                return
            else:
                self.send_response(400)
                self.end_headers()
                return


def cowpyify(msg):
    cheese = cow.Moose()
    return cheese.milk(msg)


def create_server():
    """
    """
    return HTTPServer(
        ('127.0.0.1', 5000),  # TODO: Make these ENV Vars
        SimpleHTTPRequestHandler
    )


def run_forever():
    """
    """
    server = create_server()

    try:
        print(f'Starting server on 127.0.0.1:5000')
        server.serve_forever()
    except KeyboardInterrupt as error:
        print('Thanks for running the server. Shutting down...')
        print(error.message)
        server.server_close()  # Politely closes active sockets
        server.shutdown()  # Politely shuts down the server instance


if __name__ == '__main__':
    run_forever()
