# EX01 Developing a Simple Webserver
## Date:26.10.24

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
'''
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
                <th>integrated intel UHD graphics</th>
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
httpd.serve_forever()'''

## OUTPUT:
![alt text](<Screenshot 2024-10-26 101355.png>)
![alt text](<Screenshot 2024-10-26 101446.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
