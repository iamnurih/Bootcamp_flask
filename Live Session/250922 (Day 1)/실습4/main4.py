from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("hello.html", name = '홈')

@app.route('/user/<username>')
def hello():
    return render_template("user.html", username='username')


if __name__ == '__main__':
    app.run(debug=True)
