import time
import threading
from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

# 연결된 클라이어트 보관서
connection = []

@sock.route('/ws')
def websocket(ws):
    connection.append(ws)
    while True:
        data = ws.receive()
        if data is None:
            break
    connection.remove(ws)

def background_jobs():
        while True:
            time.sleep(5)
            for ws in connection:
                try:
                    ws.send("리버야 일어나")
                except Exception:
                    pass


if threading.Thread(target=background_jobs, daemon=True).start()

if __name__ == '__main__':
      app.run(debug=True)

