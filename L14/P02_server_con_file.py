from http.server import HTTPServer, BaseHTTPRequestHandler

class myRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        with open('index.html') as f:
            lines = f.readlines()
            for l in lines:
                self.wfile.write( bytes(l, "utf8") )
        return
                                        

def main():
    print("http://127.0.0.1:8081")
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
