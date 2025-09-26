import requests
import time
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template("btc.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        result = requests.get(url).json()
        price = float(result["price"])
        ws.send(f"비트코인 현재가격🤑: {price:,.2f}")
        time.sleep(3)

        if price is None:
            break

if __name__ == '__main__':
    app.run(debug=True)
