from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
    <title>My Web Server</title>
    </head>
    <body>
        <h1>my laptop config</h1>
        <table border="5" cellspacing="10" cellpadding="5">
            <tr>
                <th>system config</th>
                <th> description</th>
            </tr>
            <tr>
                <td>processor</td>
                <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
            </tr>
            <tr>
                <th>primary memory</th>
                <th>ram 16gb</th>
            </tr>
            <tr>
                <th>seconday memory</th>
                <th>512 gb</th>
            </tr>
            <tr>
                <th>o.s build </th>
                <th>22631.4317</th>
            </tr>
            <tr>
                <th>graphic</th>
                <th>interated intel UHD graphics</th>
            </tr>
            </table>
            </body>
            </html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()