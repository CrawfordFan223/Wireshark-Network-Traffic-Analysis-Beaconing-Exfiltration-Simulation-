#A Simple listener that I did 
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

HOST = '0.0.0.0'
PORT = 8000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET", self.path, "from", self.client_address)
        print("Headers:", self.headers)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type', ''))
        if ctype == 'multipart/form-data':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST'})
            if 'file' in form:
                fileitem = form['file']
                filename = fileitem.filename or 'uploaded'
                data = fileitem.file.read()
                print("Received file:", filename, "size:", len(data))
                with open('received_' + filename, 'wb') as f:
                    f.write(data)
        else:
            length = int(self.headers.get('content-length', 0))
            data = self.rfile.read(length)
            print("POST data:", data[:200])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

if __name__ == '__main__':
    print("Starting listener on port", PORT)
    server = HTTPServer((HOST, PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping")
        server.server_close()
