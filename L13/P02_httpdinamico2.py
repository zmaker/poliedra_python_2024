from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class myRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        #print(self.path)
        data = urlparse(self.path)
        param = parse_qs(data.query)
        print(param)
        
        msg = "Stato LED: "
        state = "off"
        color = "white"
        
        page = "<html>"
        page += "<head>"
        page += "<title>Pagina dinamica</title>"
        page += "</head>"
        page += "<body>"
        
        if "/led" in self.path:
            if 'state' in param:
                state = param['state'][0]
            if 'color' in param:
                color = param['color'][0]
            
            if (state == 'on'):
                msg += "ACCESO"
            else:
                msg += "SPENTO"
        
        page += "<h1>"
        page += msg
        page += "</h1>"
        page += f"<div style='width:50; height:50; background:{color}'></div>"
        page += "</body>"
        page += "</html>"
        
        self.wfile.write( bytes(page, "utf8") )
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

