import http.server, socketserver, os
os.chdir("/Users/benjaminjbsmith/Downloads/Bens Estates Website")
PORT = int(os.environ.get("PORT", 3001))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
