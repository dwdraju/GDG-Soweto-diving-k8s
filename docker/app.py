from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! This is from v2"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
