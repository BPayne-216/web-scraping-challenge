from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Create Flask
app = Flask(__name__)

#flask_pymongo set mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Route to render index.html template  using data from Mongo
@app.route("/")
def index():

    #Find one record of data from the mongo database
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars=mars_dict)

@app.route("/scrape")
def scrape():
    
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__=="__main__":
    app.run(debug=True)

