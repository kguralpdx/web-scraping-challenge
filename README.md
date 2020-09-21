## web-scraping-challenge
# Mission to Mars

## Overview

The purpose of thie challenge is to, by the click of a button on a webpage, scrape various pieces of information about Mars from several websites and then display the results in that original webpage. This was done using several tools and technologies including *Pandas, Jupyter Notebook, BeautifulSoup, Splinter, MongoDB, and Flask* to name a few. Time to get scraping!


### Files and Folders

* [Landing Page](Missions_to_Mars/templates/index.html) - this *index.html* file is the landing page for the website and where the results of the scraping will be displayed
* **Jupyter Notebook** (Missions_to_Mars/mission_to_mars.jpynb) - the Jupyter Notebook file that was used to create the PyMongo script for the scraping; this is not used in the actual scraping process
* [Missions_to_Mars](Missions_to_Mars/) - main folder that holds all the files used and created for this project
    * [static](Missions_to_Mars/static/) - this folder holds two subfolders--css and images
        * [css](Missions_to_Mars/static/css/) - this folder holds the *style.css* file that helps format the webpage
        * [images](Missions_to_Mars/static/images/) - this folder holds the image file used as the background of the jumbotron on the webpage (*pia22594.jpg*) as well as the screenshots of the webpage
    * [templates](Missions_to_Mars/templates/) - this folder contains the *index.html* file, or the *Landing Page* file
    * [app.py](Missions_to_Mars/) - this is the *Flask* API
    * [scrape_mars.py](Missions_to_Mars/) - this is the *PyMongo* script that does the scraping

    * [mars_facts_table](Missions_to_Mars/mars_facts_table.html) - this file is the Mars Facts table created in *Jupyter Notebook* and saved as an HTML file. This is not needed to run this project. It's more of a troubleshooting file when I had issues trying to get the Mars Facts table to display on the website. This information is also saved to a variable and that's how it's used when running this project.


## Requirements

1. *MongoDB* **must** be running. If it's installed locally, you need to run `mongod` from a terminal and leave that up and running in the background. Then open another terminal and run `mongo`. If you have *MongoDB* running as a service, you just need to open a terminal and run `mongo`.

2. For *Splinter* to work, you need to have the correct version of the *Chromedriver* downloaded and accessible. This must be the version that matches your current version of Chrome. Instructions on how to find your current version of *Chrome* as well as how/where to install the *Chromedriver* can be found at the end of this file in the **How-To Install Chromedriver** section, or [here](#how-to).

3. After the *Chromedriveer* has been installed, you will need to modify the `executable-path` in the *scrape_mars.py* file to point to where you put the *chromedriver.exe* file.
    ![Images/executable_path.png](Images/executable_path.PNG)

4. If you run the *Jupyter Notebook*, you will also need to modify the `executable-path` in there as well. There are 2 cells that will need to be updated (one in the *JPL Mars Space Images - Feature Image* section and one in the *Mars Hemispheres* section).

Once the requirements are set, run `python app.py` from a Python terminal in the same folder as that file, click the URL to launch the webpage, and then click the *Scrape New Data* button to start scraping.


## Development and Analysis

I started with the *Jupyter Notebook* so I could begin scripting my scrapes and to figure out how to navigate to the information I was looking for. The first data I needed was from [NASA Mars News Site](https://mars.nasa.gov/news/). I used *BeautifulSoup* to 

Next I created the *Data* page. I knew that was going to require something outside the HTML/CSS whelm so wanted to get that taken care of. I used *Pandas* to generate an HTML table from a dataframe. That worked pretty well. I then created the page with some help from the [Layoutit!](https://layoutit.com/build) website to get the table structure. It took a little bit of tweaking but was pretty helpful.

After the *Data* page was created, I did the *Comparisons* page. Once again, I turned to the [Layoutit!](https://layoutit.com/build) website for structure assistance for the grid.

The *Visualization* pages came next and were pretty straightforward. 

Now I had all the pages created, time to tackle navigation and the sidebar. I decided to go with navigation first. This posed several challenges for me. Trying to get the layout correct and then the background colors to work depending on the screen size. Used media queries to help with the background color change. Ran into an issue when using the `navbar-light` with `bg-light`class attributes of the `nav` element. When the navigation bar background color was supposed to switch because the screen size got smaller, the *hamburger* icon would disappear. I tried setting the background color in the *styles.css* file using a media query and just trying to set it directly, but neither would work. Finally found that removing the `bg-light` attribute was all that was needed. Used the `navbar-brand` class of the `nav` element since that was always in the left side of the navigation bar and I could make it a link. Once I got the navigation bar working correctly, I added the code for that to each of the HTML pages.

The sidebar was the last challenge to overcome. Had issues getting it positioned correctly. Then I had trouble with the images, or thumbnails, and not having the correct layout based on the size of the screen; they kept stacking on top of each other instead of one row of 4 images for small screens. Finally got that working through media queries, column classes and sizing of the images. Have a better understanding of the meaning behind the 12-column structure in *Bootstrap*. Once all those issues were resolved, added the sidebar code to the 4 *Visualization* pages and the *Home* page.


## Notes

I used weather data for this project but I decided to use the data I had gathered from the earlier project instead of using the files provided. I had already done the analysis on the dataset I had created so it just made more sense to use that again. I had also put a lot of work into creating those files originally so to get the opportunity to put that to good use was appealing.

In the *Plots* dropdown, I disabled the plot if it was the current page being viewed. Seemed like you shouldn't have a link to choose it if you're already on that page. Same for the *Comparisons* and *Data* links.

The navigation bar was quite the challenge. Learned a lot about those various attributes, though, so it was more satisying when I actually got everything to work. The different screen sizes and the navbar background color change dependency what one of the more challenging parts of it.

The sidebar with the thumbnails gave me a run for my money. But the Bootstrap column grid settings finally started to make more sense along the way.

I had such grand ideas for this website but time was not my friend so I didn't get a chance to build it out more. Between the navigation bar and the sidebar, where a good portion of my time was spent, it's amazing my hair hasn't all turned gray!


## How-To

To install the *Chromedriver*, first you need to find which version of *Chrome* you're using. 

1. In Chrome, click the Menu icon, 3-dot icon, in the upper right corner of the screen.
2. Click **Help** from the dropdown menu.
3. Click **About Google Chrome** from the next dropdown menu.
4. You should now be on the *Settings* window. Your version of *Chrome* should be listed under *Google Chrome*

### macOS

* The easiest way to install ChromeDriver on a Mac is through Homebrew. You can verify your installation by running `brew -v` in terminal. If you get an error instead of a version number, visit the Homebrew website [https://brew.sh/](https://brew.sh/) to install Homebrew, and then run the command.

* If Homebrew is installed, simply run `brew cask install chromedriver` from the terminal.

* Verify your installation by running `chromedriver --version`.

* If you run into permission issues after installing chromedriver, you can grant permission by going to: `System Preferences → Security and Privacy → General → Allow Anyway`.

### Windows

* Visit the ChromeDriver [webpage](https://sites.google.com/a/chromium.org/chromedriver/downloads). Note that ChromeDriver updates really often, so the exact version you are using might be slightly different than the screenshots in these instructions. The screenshots below are for users running Chrome version 79 (your version will likely be later). Make sure match your download to the version of Chrome you’re currently using. Otherwise, you’ll likely run into an error. Follow these steps:

1. Click on the file that matches your version of Chrome.

   ![Images/01.png](Images/01.png)

2. Click `chromedriver_win32.zip` to download ChromeDriver for Windows.

   ![Images/02.png](Images/02.png)

3. Extract the executable program file.

   ![Images/03.png](Images/03.png)

4. Place the file in the same folder as your Python web scraping script.

   ![Images/04.png](Images/04.png)