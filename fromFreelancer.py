from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Set up driver instance
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.freelancer.com/jobs/artificial-intelligence/?languages=en'

# Get the list of jobs descriptions from the website
driver.get(url)
descriptions = []
description_elements = driver.find_elements(By.CLASS_NAME, 'JobSearchCard-primary-description')


df = df = pd.DataFrame(columns=['url','description'])
for element in description_elements:
    df.loc[len(df.index)] = [url,element.text]

df.to_excel('ai_project_description.xlsx')
    
driver.quit()



