# web-scraping-challenge
Web Scraping Homework - Mission to Mars
![image of HW](https://github.com/BPayne-216/web-scraping-challenge/blob/tree/master/Missions_to_Mars/templates/cover_mars.png)
Intro to this project

This project utilitizes python and 

The motivation of this project is to utilize database tables from SQLite format and in Python to analyze temperature and Weather Stations.  Queries were made to review smaller samples of the database tables and build smaller time series graphs. 

Build status: The first part saved the sqlite files and using SQLalchemy creating.  SqlAlchemy was used to bring and query the database within the python application.  Many of the queries were transferred to pandas dataframes.  Matplotlib was also used to create graphs.

Technology/Framework (In order):  
Python, Pandas, 

Features/Files:
climate_starter.ipynb contains Step 1 and Step 2 of the Climate and Station analysis.
Precipitation_Analysis_png and Station_Histogram.png are files that have the output for steps 1 and 2.
QuickDBD.sql: this is the sql file used to create the SQL tables with appropriate primary and foreign key structure.
app.py is the python file that contains the Flask code that accesses the hawaii.sqlite tables, used to create Routes for the Climate App.  This file contains JSON (jsonify) and ORM processes.
