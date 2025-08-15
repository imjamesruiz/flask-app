from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # main route to home page ; empty path
def hello_jovian():
    return render_template("index.html")


