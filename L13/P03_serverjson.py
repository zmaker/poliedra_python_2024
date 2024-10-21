from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class myRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = None
        
        if '/hello' in self.path:
            data = json.dumps( { 'hello':'world', 'received':'ok', 'answer':42 } )
        else:
            data = json.dumps( { 'error':'not founded' } )
        
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        self.wfile.write( bytes(data, "utf8") )
        return
                                        

def main():
    print("http://127.0.0.1:8081")
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
