#!/usr/bin/env python3
"""One-shot controlled HTTPS server used only for browser-runner validation."""

import argparse
import http.server
import os
import ssl


parser = argparse.ArgumentParser()
parser.add_argument("--directory", required=True)
parser.add_argument("--cert", required=True)
parser.add_argument("--key", required=True)
parser.add_argument("--port", type=int, default=8443)
args = parser.parse_args()
os.chdir(args.directory)
server = http.server.ThreadingHTTPServer(("0.0.0.0", args.port), http.server.SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(args.cert, args.key)
server.socket = context.wrap_socket(server.socket, server_side=True)
server.serve_forever()
