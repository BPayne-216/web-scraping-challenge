#Import Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import os
import pandas as pd
import requests 

def init_browser():   
    #Create path to chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    #Connect to url for Nasa Mars site
    nasa_url = 'https://mars.nasa.gov/news'
    browser.visit(nasa_url)
    #Create Beautiful Soup Object
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    #Inspect and Retrieve News Title and Opener
    news_title = news_soup.find('div', class_="content_title").text
    news_p = news_soup.find('div', class_="rollover_description_inner").text

    #Images of Mars to scrape
    jpl_url = 'https://www.jpl.nasa.gov'
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(images_url)
    #Create Beautiful Soup Object
    html = browser.html
    images_soup = BeautifulSoup('html.parser')
    #Retrieve image
    image_path = images_soup.find('img', class_="Thumb")["src"]
    featured_image_url = jpl_url + image_path

    #Mars Detail table to scrape
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_facts_df = tables[2]
    mars_facts_df.columns = ["Description", "Value"]
    mars_html_table = mars_facts_df.to_html()
    mars_html_table.replace('\n', '')

    #Hemisphere names and images to scrape
    usgs_url = 'https://astrogeology.usgs.gov'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    #Beautiful Soup object
    hemispheres_url = browser.html
    hemispheres_soup = BeautifulSoup(hemispheres_url, 'html.parser')
    all_mars_hemispheres = hemispheres_soup.find('div', class_='collapsible results')
    mars_hemispheres = all_mars_hemispheres.find_all('div', class_='item')

    hemispheres_image_urls = []
    #Iterate through the hemisphere data
    for m in mars_hemispheres:
        #Title of Products
        hemisphere = m.find('div', class_="description")
        title = hemisphere.h3.text

        #Image from hemisphere page
        hemisphere_link = hemisphere.a["href"]
        browser.visit(usgs_url + hemisphere_link)

        image_html = browser.html
        image_soup =BeautifulSoup(image_html, 'html.parser')

        image_link = image_soup.find('div', class_="downloads")
        image_url = image_link.find('li').a['href']

        #Create dictionary to store title and url
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url
        hemispheres_image_urls.append(image_dict)
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": str(mars_html_table),
        "hemisphere_images": hemispheres_image_urls
    }

    return mars_dict








