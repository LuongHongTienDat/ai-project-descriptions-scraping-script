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
url = 'https://developer.ibm.com/technologies/deep-learning/articles/'
df = pd.DataFrame(columns=['url','description'])
# # Get the list of jobs descriptions from the website
# driver.get(url)
# jobLs = driver.find_elements(By.CLASS_NAME, 'jcs-JobTitle')

# lsLinks = [l.get_attribute('href') for l in jobLs]
# print(len(lsLinks))

driver.get(url)
rows = driver.find_elements(By.CSS_SELECTOR,'.articles > a')
linkLs = [row.get_attribute('href') for row in rows]
print(linkLs)
for link in linkLs: 
    driver.get(link)
    time.sleep(4)
    pars = driver.find_elements(By.CSS_SELECTOR,'.content-data p')
    for par in pars:        
        df.loc[len(df.index)] = [linkLs,par.text]

df.to_excel('data/from_ibm.xlsx')
    
driver.quit()



