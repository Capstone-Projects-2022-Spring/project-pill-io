from flask import Flask, render_template, url_for,redirect,request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/login')
def login():
    if request.method == 'POST':
        return render_template('userManage.html')
    else:
        return render_template('index.html')

@app.route('/register')
def register():
    return render_template("userManage.html")

@app.route('/help')
def help():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True)