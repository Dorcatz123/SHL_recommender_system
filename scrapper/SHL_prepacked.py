import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pickle

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://www.shl.com/products/product-catalog/')


click = 0
next_button_count = 0
if os.path.exists("SHL_individual.pkl"):
    with open("SHL_individual.pkl", "rb") as f:
        d_old = pickle.load(f)
else:
    d_old = []

while click!= None:

        assessment_text = 0
        i=2

        while assessment_text!= None:
            assessment_text = driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]/a').text.split('\n')
            href = driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]/a').get_attribute('href')
            try:
                RT = driver.find_element(By.XPATH, value=f"/html/body/main/div[3]/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/span").get_attribute('class')
                adaptive = driver.find_element(By.XPATH, value=f"/html/body/main/div[3]/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/span").get_attribute('class')
            except:
                RT = 'No'
                adaptive = 'No'
            test_type = driver.find_element(By.XPATH, value=f"/html/body/main/div[3]/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[4]").text.split('\n')
            print(assessment_text, href, RT, adaptive, test_type)
            d_old.append({'test': assessment_text, 'href': href, 'RT': RT, 'adaptive': adaptive, 'test_type': test_type})
            i += 1
            try :
                assessment_text = driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]/a')
            except:
                assessment_text = None


        try:

            with open("SHL_prepackjob.pkl", "wb") as f:
                pickle.dump(d_old, f)
            pagination_links = driver.find_elements(By.XPATH, "//ul[contains(@class, 'pagination')]/li/a")

            next_button = None
            for link in pagination_links:
                if link.text.strip().lower() == "next":
                    next_button = link
                    break
            if next_button:

                next_button_count += 1
                if next_button_count > 12:
                    click  = None
                else:
                    next_button.click()



             # No more next button
                # driver.find_element(By.XPATH, value='/html/body/main/div[3]/div/div/div/div[2]/ul/li[7]/a').click()
        except:
                click = None

