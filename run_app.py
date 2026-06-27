import http.server
import socketserver
import webbrowser
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Đảm bảo chúng ta đang ở đúng thư mục chứa index.html
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"Đang khởi chạy máy chủ tại http://localhost:{PORT}")
print("Nhấn Ctrl+C để dừng máy chủ.")

# Mở trình duyệt mặc định
webbrowser.open(f"http://localhost:{PORT}/index.html")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐang dừng máy chủ...")
        httpd.server_close()
