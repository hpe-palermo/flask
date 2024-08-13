from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

app.run('localhost', 2000)