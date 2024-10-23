from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib

class myRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        page = "<html>"
        page += "<body>"
        page += "<form method='POST'>"
        page += "Nome: <input name='nome'>"
        page += "<button>Invia Dati</button>"
        page += "</form>"
        page += "</body>"
        page += "</html>"
        
        self.wfile.write( bytes(page, "utf8") )
        return
    
    def do_POST(self):
        datalen = int(self.headers['Content-Length'])
        print("bytes ricevuti: ", datalen)
        (_, value) = self.rfile.read(datalen).decode('utf-8').split('=')
        value = urllib.parse.unquote_plus(value)
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        page = "<html>"
        page += "<body>"
        page += "<h1>"
        page += value
        page += "</h1>"
        page += "<a href='/'>Back</a>"
        page += "</body>"
        page += "</html>"
        
        self.wfile.write( bytes(page, "utf8") )
        return                                        

def main():
    print("http://127.0.0.1:8081")
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
