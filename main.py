from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
# db file name
db_name = 'SQLite_Python.db'
# use said db with sqlALCH and set up path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
# track changes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# used for all SQLAlchemy commands
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/')
def testdb():
    try:
        # sample query to test if connection works, otherwise
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>Database Connection Successful.</h1>'
    except Exception as e:
        # e holds description of the error
        # return error
        error_text = "<p>The error is :<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/login')
def login():
    if request.method == 'POST':
        return render_template('userManage.html')
    else:
        return render_template('index.html')

@app.route('/register')
def register():
    return render_template("userManage.html")

if __name__ == "__main__":
    app.run(debug=True)