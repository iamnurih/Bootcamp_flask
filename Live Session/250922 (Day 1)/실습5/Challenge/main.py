from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greet')
def greet():
   username = request.args.get('username', "Flask")
   if username:
       return render_template("greet.html", username=username)
   else:
       return "사용자 이름이 입력되지 않았습니다"

if __name__ == '__main__':
    app.run(debug=True)