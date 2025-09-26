from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/<name>")
def index(name):
    # return {"message": f"{name}님, 환영합니다!"}
    return jsonify(message=f"{name}님, 환영합니다!") # 권장

if __name__ == "__main__":
    app.run(debug=True)
