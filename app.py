#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A program that takes a list of recipes and gives you a random one.
This is in Python3
"""

__author__ = "mhoelzer"


from flask import Flask
from flask import render_template
from tinydb import TinyDB
import random

app = Flask(__name__)
db = TinyDB("db.json")
recipes = db.all()


@app.route("/")
def retrieve_recipe():
    """getting random recipes because spontaneity is fun"""
    rand_rec = random.choice(recipes)
    # return f"{rand_rec}"
    return render_template("recipe.html", recipe=rand_rec)
