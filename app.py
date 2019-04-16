from flask import Flask, render_template
from tinydb import TinyDB, Query
import random

app = Flask(__name__)
db = TinyDB("db.json")
recipes = db.all()


@app.route("/")
def index():
    rand_rec = random.choice(recipes)
    # return f"{rand_rec}"
    return render_template("recipe.html", recipe=rand_rec)
