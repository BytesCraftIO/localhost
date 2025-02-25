# installation required
# pip install Flask
# python main.py

from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()