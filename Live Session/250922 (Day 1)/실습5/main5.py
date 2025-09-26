from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return render_template("hello.html", name="홈")

@app.route('/user/<username>')
def hello(username):
    return render_template("user.html", username=username)

@app.route("/fruits")
def fruits():
    fruits = ["apple", "banana", "cherry", "strawberry"]
    return render_template("fruits.html", fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)
