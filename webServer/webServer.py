from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = 'localhost'
PORT = 8000

home_page = """
<html>
    <head>
        <title> Hello! </title>
    <head>
    <body>
    <h1> Hello, world! </h1>
    <p> This is my first try to create a local server </p>
    </body>
<html>
"""


class MyHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-length", len(home_page))
            self.end_headers()

            self.wfile.write(bytes(home_page, "utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

            self.wfile.write(bytes("404: not found", "utf-8"))


my_server = HTTPServer((HOST, PORT), MyHTTP )
my_server.serve_forever()
