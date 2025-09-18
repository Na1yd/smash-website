from flask import Flask, render_template
import sqlite3
# pip install flask
# pepe 8 needed!
# code coments!
# testing :(!

app = Flask(__name__)


# This starting point of the website.
@app.route('/')
def home():
    return render_template("home.html")


# This is for when you go to mutch ups and it shows you all characters in game
# And you choose the one you want to see.
@app.route("/all_characters")
def all_characters():
    conn = sqlite3.connect("Dk.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Character')
    Characters = cur.fetchall()
    conn.close()
    return render_template('all_characters.html', Characters=Characters)


# This is for when you search for somthing that does not exist.
# It lets you see this nice screen instead of a messy screen.
@app.errorhandler(404)
def page_not_found(Error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def special_exeption_handler(Error):
    print(f"An error occurred: {Error}")
    return render_template("500.html"), 500


# When clicking on a character in the match ups section it takes you here.
# All the info you need is taken from the data bace and showed to you.
@app.route("/Characters/<int:id>")
def characters(id):
    conn = sqlite3.connect("Dk.db")
    cur = conn.cursor()
    cur.execute(
            "SELECT name, How_to_play_matchup,Pdko_percent_ps2,"
            "Apdko_percent_ps2 FROM Character WHERE id=?", (id,))
    Character = cur.fetchone()
    columns = [desc[0] for desc in cur.description] if cur.description else []
    CharacterFields = list(zip(columns, Character)) if Character else []
    conn.close()
    return render_template('character.html', Character=Character, CharacterFields=CharacterFields)


@app.route("/Game_Franchises/<int:id>")
def Game_Franchise(id):
    conn = sqlite3.connect("Dk.db")
    cur = conn.cursor()
    cur.execute(
            "SELECT Franchise , character1,character1,character1,"
            "character1,character1 FROM Game_Franchise WHERE id=?", (id,))
    conn.commit()
    Game_Franchise = cur.fetchone()
    return render_template('Game_Franchise.html', Game_Franchise=Game_Franchise)


@app.route("/tech")
def tech():
    return render_template("tech.html")


if __name__ == "__main__":
    app.run(debug=True)

