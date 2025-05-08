from flask import Flask,render_template
import sqlite3
#pip install flask
app = Flask(__name__)




@app.route('/')
def home():
    return render_template("home.html")


@app.route("/me")
def me():
    return render_template("me.html")


@app.route("/petrocks/<int:id>")
def petrocks(id):
    return render_template("petrocks.html",id=id)



if __name__ == "__main__":
    app.run(debug=True)