from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from urllib.parse import urlparse

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加 CORS 头，允许跨域请求
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Cookie')
        super().end_headers()

    def do_OPTIONS(self):
        # 处理预检请求
        self.send_response(200)
        self.end_headers()

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    print(f"""
掘金 Cookie 测试服务器已启动！

请在浏览器中访问:
http://localhost:{port}/test_cookie.html

按 Ctrl+C 可停止服务器
""")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.server_close()

if __name__ == '__main__':
    run_server() 