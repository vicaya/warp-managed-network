#!/usr/bin/python3

import http.server
import logging
import ssl
import sys


class HelloHandler(http.server.BaseHTTPRequestHandler):
  hello = 'hello!'

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain; charset=utf-8')
    self.end_headers()
    self.wfile.write(f'{self.hello}'.encode('utf-8'))
    self.log_message("%s", self.headers.get("user-agent", "unknown ua"))


def serve(port, prefix, hello):
  HelloHandler.hello = hello
  server = http.server.ThreadingHTTPServer(('0.0.0.0', port), HelloHandler)
  sslcontext = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  sslcontext.load_cert_chain(certfile=f'{prefix}.pem', keyfile=f'{prefix}.key')
  server.socket = sslcontext.wrap_socket(server.socket, server_side=True)
  server.serve_forever()


def main(args):
  nargs = len(args)
  serve(int(args[1]) if nargs > 1 else 4443,
        args[2] if nargs > 2 else "default",
        args[3] if nargs > 3 else "hello!\n")


if "__main__" == __name__:
    main(sys.argv)
