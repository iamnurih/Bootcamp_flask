from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template("hello.html", name = "리버")

if __name__ == '__main__':
    app.run(debug=True)

