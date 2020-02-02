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
    for response in responses:
        
        url = x.PlayerProfile

        browser = init_browser()

        browser.visit(url)

        browser.click_link_by_partial_text('FULL IMAGE')

        html = browser.html

        soup = bs(html_2, 'html.parser')

        src_url = soup.find(id='full_image').get('data-fancybox-href')

        featured_image_url = 'https://www.jpl.nasa.gov' + src_url


        content = {
            'featured_image_url':featured_image_url,
        }

        browser.quit()
        
        return content