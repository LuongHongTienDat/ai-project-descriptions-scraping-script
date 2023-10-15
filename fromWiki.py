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
url = 'https://en.wikipedia.org/wiki/List_of_artificial_intelligence_projects'
df = pd.DataFrame(columns=['url','description'])


driver.get(url)
rows = driver.find_elements(By.CSS_SELECTOR,'#bodyContent li')
for row in rows: 
    df.loc[len(df.index)] = [url,row.text]

df.to_excel('data/from_wiki.xlsx')
    
driver.quit()



