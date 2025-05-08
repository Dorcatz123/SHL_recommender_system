path = r'C:\Users\aksha\PycharmProject\Selenium\prepacked_SHL_assessment.pkl'

import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pickle, os


with open(path, 'rb') as file:
    prepacked = pickle.load(file)


for i in range(len(prepacked)):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(prepacked[i]['href'])
    elements = driver.find_elements(By.CSS_SELECTOR, "div.product-catalogue-training-calendar__row.typ")
    prepacked[i]['info'] = ''
    for el in elements:
        prepacked[i]['info'] += el.text + '\n'
    print(prepacked[i])
    driver.quit()
    if i% 10 == 0:
        with open("prepacked_SHL_assessment_with_description.pkl", 'wb') as file:
            pickle.dump(prepacked, file)

with open("prepacked_SHL_assessment_with_description.pkl", 'wb') as file:
            pickle.dump(prepacked, file)