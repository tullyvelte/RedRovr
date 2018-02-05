from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = PyMongo.MongoClient(conn)

# Use database and create it if it does not exist
db = client.marsDB

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)