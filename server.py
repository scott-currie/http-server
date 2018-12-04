from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from cowpy import cow


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    """
    def do_GET(self):
        """
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

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
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            parsed_message = parsed_qs['msg'][0]
            cheese = cow.Moose(eyes='dead')
            msg = cheese.milk(parsed_message)
            self.wfile.write(msg.encode())
            return

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Cow not found. Moo.')

    def do_HEAD(self):
        """
        """
        pass

    def do_POST(self):
        """
        """
        pass


def create_server():
    """
    """
    return HTTPServer(
        ('127.0.0.1', 5000),  # TODO: Make these ENV Vars
        SimpleHTTPRequestHandler
    )


def run_forever():
    """Create the server instance."""
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
