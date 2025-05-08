path = r'C:\Users\aksha\PycharmProject\Selenium\individual_SHL_assessment.pkl'

import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pickle, os


with open(path, 'rb') as file:
    individual = pickle.load(file)


for i in range(len(individual)):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(individual[i]['href'])
    elements = driver.find_elements(By.CSS_SELECTOR, "div.product-catalogue-training-calendar__row.typ")
    individual[i]['info'] = ''
    for el in elements:
        individual[i]['info'] += el.text + '\n'
    print(individual[i])
    driver.quit()
    if i% 10 == 0:
        with open("individual_SHL_assessment_with_description.pkl", 'wb') as file:
            pickle.dump(individual, file)

with open("individual_SHL_assessment_with_description.pkl", 'wb') as file:
            pickle.dump(individual, file)