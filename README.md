# RedRovr
A Python, Mongo, Flask, Bootstrap web app for scraping Mars info

# Mission to Mars
Goal was to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Scraping

An initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* Scrape the (https://mars.nasa.gov/news/) and collect the latest News Title and Paragragh Text.

### JPL Mars Space Images - Featured Image

* Visit the url for JPL's Featured Space Image (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.

### Mars Weather

* Visits the Mars Weather twitter account (https://twitter.com/marswxreport?lang=en) and scrapes the latest Mars weather tweet from the page.

### Mars Facts

* Visits the Mars Facts webpage (http://space-facts.com/mars/) and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Uses Pandas to convert the data to a HTML table string.

### Mars Hemisperes

* Visits the USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

## MongoDB and Flask Application

Uses MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
