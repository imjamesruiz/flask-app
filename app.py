from flask import Flask

app = Flask(__name__)

@app.route("/") # main route to home page ; empty path
def hello_world():
    return "<h1>Hello, world!</h1>"


