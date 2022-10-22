from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>It's a good day!</p>"

if __name__ == "__main__":
    # app.debug = True
    app.run()