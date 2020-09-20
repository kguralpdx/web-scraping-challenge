from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "../../../../chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    # Create an empty dictionary to store scraped data
    mars_scraped_dict = {}

    # NASA Mars News Scrape
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    # Get all the information for anything with a 'div' element and class of 'features'
    all_features = soup.find_all('div', class_='features')

    # Get everything for the first features div tag
    features = all_features[0]

    # Get the title and paragraph from the latest feature and assign them to variables
    news_title = features.find(class_="content_title").text.strip()
    news_p = features.find(class_="rollover_description_inner").text.strip() 

    # Add the variable info to mars_scraped_dict dictionary
    mars_scraped_dict["news_title"] = news_title
    mars_scraped_dict["news_p"] = news_title

    
    # JPL Mars Space Images Scrape
    # Initialize browser 
    browser = init_browser()

    # Browse to the JPL Mars Space site
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    time.sleep(2)

    # Click the button on the image to goto the underlying HTML
    divs = browser.find_by_tag("div")
    within_elements = divs.first.find_by_id("full_image").click()

    # Find the 'more info' button and click on that to get to the page that has the full size image
    browser.links.find_by_text('more info     ').first.click()

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    # Return all the img tag attributes for the img tag with a class of 'main_image'
    main_image = soup.find('img', class_='main_image')
    
    # Get the value for the 'src' tag
    featured_image = main_image.attrs['src']

    # Concatenate the main JPL website URL with the partial URL from the 'src' tag to get the full URL for the full size image
    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image

    # Add the variable info to mars_scraped_dict dictionary
    mars_scraped_dict["featured_image_url"] = featured_image_url

    # Close the browser window
    browser.quit()


    # Mars Facts Scrape
    # Set the URL to a variable
    facts_url = "https://space-facts.com/mars/"

    # Scrape any tabular data from the site
    tables = pd.read_html(facts_url)

    time.sleep(2)

    # Get the first table and add column headers
    mars_facts_df = tables[0]
    mars_facts_df.columns = ["Description", "Mars"]

    # Change the index to be the Description column
    mars_facts_df.set_index(["Description"], inplace=True)

    # Save the dataframe as an html table file
    mars_table = mars_facts_df.to_html()

    # Add the variable info to mars_scraped_dict dictionary
    mars_scraped_dict["mars_table"] = mars_table


    # Mars Hemispheres
    # Initialize browser 
    browser = init_browser()

    # Browse to the USGS Astrogeology site
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(6)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    # find all the itemLink product-item class elements
    results = soup.find_all("a", class_="itemLink product-item")

    # Get the URLs to be searched
    full_urls = []
    base_url = "https://astrogeology.usgs.gov"
    for item in results:
        if item['href'] not in full_urls:
            full_urls.append(item['href'])

    # Create a list of full URLs by oncatenating the main URL with the relative URLs
    search_urls = [base_url + item for item in full_urls]

    # Create list of dicitionaries
    hemisphere_list = []
    for link in search_urls:
        mars_dict = {}
        browser.visit(link)
        html = browser.html
        soup = bs(html, "html.parser")
        img_url = soup.find("img", class_ = "wide-image")["src"]
        title = soup.find("h2", class_="title").text
        mars_dict["title"] = title
        mars_dict["img_url"] = base_url + img_url
        hemisphere_list.append(mars_dict)
        browser.back()

    # Close the browser
    browser.quit()
    
    # Add the hemispheres_list to the to mars_scraped_dict dictionary
    mars_scraped_dict["hemispheres"] = hemisphere_list

    # Return results
    return mars_scraped_dict