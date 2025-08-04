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
    # Fetch all characters from the database
    Characters = cur.fetchall()
    conn.close()
    return render_template('all_characters.html', Characters=Characters)



@app.errorhandler(404)
def page_not_found(Error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def special_exeption_handler(Error):
    # This is a special exception handler for 500 errors
    # You can log the error or perform other actions here
    print(f"An error occurred: {Error}")
    return render_template("500.html"), 500


@app.route("/Characters/<int:id>")
def characters(id):
    conn = sqlite3.connect("Dk.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Character WHERE id=?", (id,))
    conn.commit()
    Character = cur.fetchone()
    return render_template('character.html', Character=Character)


@app.route("/tech")
def tech():
    return render_template("tech.html")


if __name__ == "__main__":
    app.run(debug=True)
