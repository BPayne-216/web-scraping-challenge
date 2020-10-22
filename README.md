# web-scraping-challenge
Web Scraping Homework - Mission to Mars
![image of HW](https://github.com/BPayne-216/web-scraping-challenge/blob/master/Missions_to_Mars/templates/cover_mars.png)
Intro to this project

This project utilitizes python, beautiful soup, splinter, Flask, pymongo to scrape various space-related websites.  HTML and bootstrap were used to create and index of the scraped items: text, data table, pictures.

The motivation of this project is to utilize various web scraping applications, store the scraped information, and then review it on a separate web (HTML) document.

Build status: The first part of the project utilized Beautiful Soup within python to review the data to be pulled from the (4) websites below: 
https://mars.nasa.gov/news,
https://www.jpl.nasa.gov,
http://space-facts.com/mars,
https://astrogeology.usgs.gov

Technology/Framework (In order):  
Python (pandas), chromedriver, Beautiful Soup, splinter, pymongo, Flask.  HTML, bootstrap.

Features/Files:
mission_to_mars.ipynb is the initial python document that connects to the individual websites listed and aggregates the reviewed data (text, table, pictures) to be stored.  Lists and dictionaries were used.
scrape_mars.py this file performs the scrape based on the initial jupyter notebook format and is linked to the app.py file.
app.py this file uses Flask and pymongo to store the data and transform the /scrape function to be used in HTML format.
index.html reviewed the information scraped in HTML format.
