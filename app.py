from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Oh, you GET! But, can you POST?"


@app.route("/", methods=["POST"])
def post():
    return "Oh, you POST! But, can you GET?"


@app.route("/", methods=["PUT"])
def put():
    return "Nobody PUTs baby in the corner."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')