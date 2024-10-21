from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class myRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        dt = datetime.now()
        data = dt.strftime("%d/%m/%Y %H:%M:%S")
        
        msg = "<html>"
        msg += "<head>"
        msg += "<title>Ora Esatta</title>"
        msg += "<meta http-equiv='refresh' content='1'>"
        msg += "</head>"
        msg += "<body>"
        msg += "<h1>"
        msg += data
        msg += "</h1>"
        msg += "</body>"
        msg += "</html>"
        
        self.wfile.write( bytes(msg, "utf8") )
        return
                                        
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def main():
    ipaddr = str(get_ip())
    port = 8081
    
    print(f"http://{ipaddr}:{port}")
    
    server_address = (ipaddr, port)
    
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
