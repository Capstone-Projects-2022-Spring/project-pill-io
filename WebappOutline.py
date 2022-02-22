from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is the main page of the soon to be Pill.io !!" \
           "<h1>Hello Everyone<h1>" \
           "<p>We are Pill.IO" \
           "<br>A pill dispenser" \
           "<br>created for people" \
           "<br>by us. <p>"

if __name__ == "__main__":
    app.run()