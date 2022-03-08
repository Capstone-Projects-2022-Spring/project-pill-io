
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pythonanywhere.html")

@app.route("/login", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        print(user + password)
        return redirect(url_for("user", usr=user, password=password))
    else:
        return render_template("pythonanywhere.html")

@app.route("/<user> & <password>")
def user(user, password):
    return f"<h1>{user}{password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)