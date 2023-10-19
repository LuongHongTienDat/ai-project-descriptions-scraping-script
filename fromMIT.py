import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.keys import Keys

# Set up driver instance
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
path = 'https://news.mit.edu/topic/'
topics = ['computer-vision','computer-science-and-artificial-intelligence-laboratory-csail',
          'natural-language-processing','cloud-computing','software','machine-learning','data','big-data']
df = pd.DataFrame(columns=['url','description'])

# Get the list of jobs descriptions from the website
for topic in topics:
    url = path + topic 
    driver.get(url)
    elements = driver.find_elements(By.CLASS_NAME, 'term-page--news-article--item--title--link')
    links = [e.get_attribute('href') for e in elements]
    for l in links:
        driver.get(l)
        pars = driver.find_elements(By.CSS_SELECTOR, '#block-mit-content > div > article > div > div.news-article--content > div.news-article--content--body > div > div > p')
        for p in pars:
            df.loc[len(df.index)] = [l,p.text]


df.to_excel('data/from_MIT.xlsx')
    
driver.quit()



