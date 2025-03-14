import http.server
import socketserver

PORT = 8000
counter = 0  # アクセスカウンター

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global counter
        counter += 1

        # シンプルなHTMLページを生成
        html_content = f"""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Python Web Server</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #f4f4f4;
                }}
                .container {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                    display: inline-block;
                }}
                h1 {{ color: #333; }}
                p {{ font-size: 1.2em; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Python http.server で作るWebサイト</h1>
                <p>このページへのアクセス数: <strong>{counter}</strong></p>
                <p>Pythonの http.server を使って簡単なWebサーバーを構築しました。</p>
                <p><a href="/">更新する</a></p>
            </div>
        </body>
        </html>
        """

        # HTTPレスポンスを送信
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

# サーバーの起動
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
