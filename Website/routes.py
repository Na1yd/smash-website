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


@app.route("/all_characters")
def all_characters():
    conn = sqlite3.connect("")
    cur = conn.cursor()
    cur.execute('SELECT * FROM character')
    characters = cur.fetchall()
    conn.close()
    return render_template('all_characters.html', characters = characters)


if __name__ == "__main__":
    app.run(debug=True)