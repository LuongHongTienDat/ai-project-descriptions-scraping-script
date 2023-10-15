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
url = 'https://ai-jobs.net/'
df = pd.DataFrame(columns=['url','description'])
# # Get the list of jobs descriptions from the website
# driver.get(url)
# jobLs = driver.find_elements(By.CLASS_NAME, 'jcs-JobTitle')

# lsLinks = [l.get_attribute('href') for l in jobLs]
# print(len(lsLinks))

driver.get(url)
rows = driver.find_elements(By.CSS_SELECTOR,'#job-list > li > div > a')
linkLs = [row.get_attribute('href') for row in rows]
print(linkLs)
for link in linkLs: 
    driver.get(link)
    content = driver.find_element(By.CLASS_NAME,'job-description-text')
    df.loc[len(df.index)] = [link,content.text]

df.to_excel('data/from_aijobs.xlsx')
    
driver.quit()



