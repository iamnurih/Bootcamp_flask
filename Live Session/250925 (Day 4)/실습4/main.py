from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template("sentiment.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        data = ws.receive()

        if data is None:
            break

        pos = ["love", "happy", "excited", "great"]
        neg = ["sad", "gloomy", "angry", "upset"]

        if any(word in data for word in pos):
            sentiment = "🤩"
        elif any(word in data for word in neg):
            sentiment = "🥲"
        else:
            sentiment = "🙃"

        ws.send(sentiment)

if __name__ == '__main__':
    app.run(debug = True)