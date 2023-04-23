#!/usr/bin/python3

import http.server
import ssl
import sys


class HelloHandler(http.server.BaseHTTPRequestHandler):
  hello = 'hello!'

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain; charset=utf-8')
    self.end_headers()
    self.wfile.write(f'{self.hello}'.encode('utf-8'))


def serve(prefix, hello):
  HelloHandler.hello = hello
  server = http.server.HTTPServer(('0.0.0.0', 4443), HelloHandler)
  sslcontext = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  sslcontext.load_cert_chain(certfile=f'{prefix}.pem', keyfile=f'{prefix}.key')
  server.socket = sslcontext.wrap_socket(server.socket, server_side=True)
  server.serve_forever()


def main(args):
  nargs = len(args)
  serve(args[1] if nargs > 1 else "default",
        args[2] if nargs > 2 else "hello!")


if "__main__" == __name__:
    main(sys.argv)
