from cowpy import cow
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    """

    def do_GET(self):
        """Handle GET request. Will serve both the root of the site as well
        as allow the user to request a message that will be returned using the
        cowpy package.
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        print(parsed_qs)
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''<!DOCTYPE html>
            <html>
              <head>
                <title> cowsay </title>
              </head>
              <body>
               <header>
                 <nav>
                   <ul>
                     <li><a href="/cowsay">cowsay</a></li>
                   </ul>
                 </nav>
               <header>
               <main>
                 <p>This project is designed to test specific routes and return status messages accordingly</p>
               </main>
              </body>
            </html>''')
            return

        elif parsed_path.path == '/cow':
            try:
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                parsed_message = parsed_qs['msg'][0]
                cheese = cow.Moose(eyes='dead')
                msg = cheese.milk(parsed_message)
                self.wfile.write(msg.encode())
                return

            except KeyError:
                self.send_response(400)
                self.end_headers()
                cheese = cow.Moose()
                msg = cheese.milk('400 Bad Request')
                self.wfile.write(msg.encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Cow not found. Moo.')

        self.send_response(404)
        self.end_headers()

    def do_HEAD(self):
        """
        """
        pass

    def do_POST(self):
        """Handle POST request. Parse the query looking for
        a msg. If msg exists, send the cowpy formattted  msg
        as a json string.

        input: none
        return: none
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        if parsed_path.path == '/cow':
            print('parsed_qs=', parsed_qs)
            # msg in query (200)
            if 'msg' in parsed_qs:
                cowpied = cowpyify(parsed_qs['msg'][0])
                json_string = json.dumps({'content': cowpied})
                self.send_response(201)
                self.end_headers()
                self.wfile.write(json_string.encode())
                return
            # No msg in query (400)
            else:
                self.send_response(400)
                self.end_headers()
                return
        # Post methods not allowed on / (400)
        if parsed_path.path == '/':
            self.send_response(400)
            self.end_headers()
            return
        # Route doesn't exist (404)
        self.send_response(404)
        self.end_headers()


def cowpyify(msg):
    """Pass a string through cowpy.

    input: msg (str): string to modify
    return: (str) new string wrapped in cowpy text
    """
    cheese = cow.Moose()
    return cheese.milk(msg)


def create_server():
    """Creates a method for the creation of a basic HTTP server."""
    return HTTPServer(
        ('127.0.0.1', 5000),  # TODO: Make these ENV Vars
        SimpleHTTPRequestHandler
    )


def run_forever():
    """Create the server instance using the above create_server method."""
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
