from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import json

# Scrape Featured Image
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    data_url = "http://localhost:5000"
    responses  = requests.get(data_url).json()

    links = []

    for i in range(3):
        
            response = responses[i]

            url = response["PlayerProfile"]

            playername = response["playername"]

            browser = init_browser()

            browser.visit(url)

            html = browser.html

            soup = bs(html, 'html.parser')

            img_url = soup.find("img")['src']

            links.append({
                "playername": playername,
                "img_url": 'http://www.espncricinfo.com' + img_url
            }) 

    return links
