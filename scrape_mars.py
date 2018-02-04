


# ## Red Rovr
# #### A Mars Data Scraping App 


import requests as req
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
from selenium import webdriver


# ### NASA Mars News
def scrape():

    url = 'https://mars.nasa.gov/news/'
    response = req.get(url)


    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.find("div", class_="content_title").text
    description = soup.find("div", class_="rollover_description_inner").text


    browser = Browser('chrome', headless=False)
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    browser.click_link_by_id('full_image')

    browser.click_link_by_partial_text('more info')

    image_html = browser.html
    soup2 = BeautifulSoup(image_html, 'html.parser')
    main_img_url = soup2.find('img', class_='main_image')
    split_img_url = main_img_url.get('src')

    featured_image_url = "https://www.jpl.nasa.gov" + split_img_url

    mars_twitter = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_twitter)

    html = browser.html
    twitter_soup = BeautifulSoup(html, 'html.parser')


    mars_tweet = twitter_soup.find('div', class_="js-tweet-text-container")

    mars_weather = mars_tweet.find('p', 'tweet-text').get_text()
    #mars_weather

    facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(facts_url)
    #tables

    mars_df = tables[0]
    mars_df.columns = ['Mars Facts', 'Mars Data']
    #mars_df

    mars_df.set_index('Mars Facts', inplace=True)
    #mars_df


    html_table = mars_df.to_html()

    mars_df.to_html('table.html')


    # Visit the USGS Astrogeology site to obtain for obtain high resolution images for each of Mar's hemispheres
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    usgs_req = req.get(usgs_url)

    # You will need to click each of the links to the hemispheres in order to find full res image
    soup = BeautifulSoup(usgs_req.text, "html.parser")
    hemi_attributes_list = soup.find_all('a', class_="itemLink product-item")

    # Save both the image url string using the keys img_url and title.
    # Append the dictionary with the image url string and the hemisphere title to a list.

    hemisphere_image_urls = []
    for hemi_img in hemi_attributes_list:
        img_title = hemi_img.find('h3').text
        link_to_img = "https://astrogeology.usgs.gov/" + hemi_img['href']
        img_request = req.get(link_to_img)
        soup = BeautifulSoup(img_request.text, 'lxml')
        img_tag = soup.find('div', class_='downloads')
        img_url = img_tag.find('a')['href']
        hemisphere_image_urls.append({"Title": img_title, "Image_Url": img_url})

    mars_data = {
        "News_Title": title,
        "Paragraph_Text": description,
        "Most_Recent_Mars_Image": featured_image_url,
        "Mars_Weather": mars_weather,
        "mars_h": hemisphere_image_urls
     }
    return mars_data

