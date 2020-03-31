import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
import scrape_images
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import db_name, db_pw


# FLASK APP INITIALIZED
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_name}:{db_pw}@localhost/cricket'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

DATABASE_URI = 'postgresql://postgres:postgres@localhost/cricket'

engine = create_engine(DATABASE_URI)

Base = automap_base()

Base.prepare(engine, reflect=True)

batters = Base.classes.batters

session = Session(bind=engine)


@app.route("/")
def batters_func():

    results = session.query(batters.player, batters.country, batters.careerlength, batters.matches, batters.inn, batters.notout, batters.runs, batters.hs, batters.avgscore, batters.hundreds, batters.fifties, batters.zero, batters.playerprofile).all()

    batter_list = []
    for player, country, careerlength, matches, inn, notout, runs, hs, avgscore, hundreds, fifties, zero, playerprofile in results:
        batter_dict = {}
        batter_dict["playername"] = player
        batter_dict["country"] = country
        batter_dict["careerlength"] =  careerlength
        batter_dict["matches"] = matches
        batter_dict["innings"] = inn
        batter_dict["no"] = notout
        batter_dict["runs"] = runs
        batter_dict["hs"] = hs
        batter_dict["avg"] = avgscore
        batter_dict["hundreds"] = hundreds
        batter_dict["fifties"] = fifties
        batter_dict["zeroes"] = zero
        batter_dict["PlayerProfile"] = playerprofile 
        batter_list.append(batter_dict)

    return jsonify(batter_list) 


@app.route("/images")
def images():

    image_urls = scrape_images.scrape()

    return jsonify(image_urls)


if __name__ == "__main__":
    app.run(debug=True)