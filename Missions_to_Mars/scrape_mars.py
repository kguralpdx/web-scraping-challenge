from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "../../../../chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    # Create an empty dictionary to store scraped data
    mars_scraped_dict = {}

    # NASA Mars News Scrape
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/"

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