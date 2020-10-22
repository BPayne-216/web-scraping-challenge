# web-scraping-challenge
Web Scraping Homework - Mission to Mars
![image of HW](https://github.com/BPayne-216/web-scraping-challenge/blob/master/Missions_to_Mars/templates/cover_mars.png)
Intro to this project

This project utilitizes python, beautiful soup, splinter, Flask, pymongo to scrape various space-related websites.  HTML and bootstrap were used to create and index of the scraped items: text, data table, pictures.

The motivation of this project is to utilize various web scraping applications, store the scraped information, and then review it on a separate web (HTML) document.

Build status: The first part of the project utilized Beautiful Soup within python to review the data to be pulled from the (4) websites below: 
https://mars.nasa.gov/news
https://www.jpl.nasa.gov
http://space-facts.com/mars
https://astrogeology.usgs.gov

Technology/Framework (In order):  
Python, Beautiful Soup

Features/Files:
climate_starter.ipynb contains Step 1 and Step 2 of the Climate and Station analysis.
Precipitation_Analysis_png and Station_Histogram.png are files that have the output for steps 1 and 2.
QuickDBD.sql: this is the sql file used to create the SQL tables with appropriate primary and foreign key structure.
app.py is the python file that contains the Flask code that accesses the hawaii.sqlite tables, used to create Routes for the Climate App.  This file contains JSON (jsonify) and ORM processes.
