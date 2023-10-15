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
url = 'https://projectwale.com/final-year-artificial-intelligence-projects/'

# Get the list of jobs descriptions from the website
driver.get(url)
description_elements = driver.find_elements(By.CLASS_NAME, 'JobSearchCard-primary-description')
table = driver.find_element(By.XPATH,'//*[@id="post-31"]/div/div/div/div/section[2]/div/div/div/div/div/div[1]/div/div/div[2]/table')

links = table.find_elements(By.TAG_NAME,'a')
lsLinks = [l.get_attribute('href') for l in links]
print(len(lsLinks))
df = pd.DataFrame(columns=['url','description'])

# for l in lsLinks[:50]: 
#     # driver.execute_script('''window.open("{l}","_blank");''')
#     driver.get(l)
#     abstract = driver.find_element(By.XPATH,'/html/body/section[1]/div/form/div/div[2]/p[1]')
#     df.loc[len(df.index)] = [l,abstract.text]

for l in lsLinks[90:200]: 
    # driver.execute_script('''window.open("{l}","_blank");''')
    driver.get(l)
    abstract = driver.find_element(By.XPATH,'/html/body/section[1]/div/form/div/div[2]/p[1]')
    df.loc[len(df.index)] = [l,abstract.text]

df.to_excel('data/ai_project_description_3.xlsx')
    
driver.quit()



