
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World, this is a Heroku Test!</p>"


@app.route("/home")
def hello_world():
    return "<p>Hello, World, this is home!</p>"


if __name__ == '__main__':
    app.run()
