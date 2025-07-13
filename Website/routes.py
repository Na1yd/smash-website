from flask import Flask, render_template
import sqlite3
# pip install flask
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/me")
def me():
    return render_template("me.html")


@app.route("/all_characters")
def all_characters():
    conn = sqlite3.connect("Dk.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Character')
    Characters = cur.fetchall()
    conn.close()
    return render_template('all_characters.html', Characters=Characters)


@app.route("/Characters/<int:id>")
def characters(id):
    conn = sqlite3.connect("Dk.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Character WHERE id=?", (id,))
    Character = cur.fetchone()
    return render_template('character.html', Character=Character)

@app.route("/tech")
def tech():
    return render_template("tech.html")


if __name__ == "__main__":
    app.run(debug=True)
