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
url = 'https://www.techtarget.com/whatis/feature/Artificial-intelligence-glossary-60-terms-to-know'
df = pd.DataFrame(columns=['url','description'])
# # Get the list of jobs descriptions from the website
# driver.get(url)
# jobLs = driver.find_elements(By.CLASS_NAME, 'jcs-JobTitle')

# lsLinks = [l.get_attribute('href') for l in jobLs]
# print(len(lsLinks))

driver.get(url)
rows = driver.find_elements(By.CSS_SELECTOR,'#content-body p')
for r in rows: 
    print(r.text)
    df.loc[len(df.index)] = [url,r.text]

df.to_excel('data/from_others.xlsx')
    
driver.quit()



