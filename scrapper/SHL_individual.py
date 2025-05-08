import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pickle, os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://www.shl.com/products/product-catalog/')

click = 0

j=3

if os.path.exists("SHL_individual.pkl"):
    with open("SHL_individual.pkl", "rb") as f:
        d_old = pickle.load(f)
else:
    d_old = []
while click!= None:

        assessment_text = 0
        i=2

        while assessment_text!= None:
            assessment_text = driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[{j}]/div/table/tbody/tr[{i}]/td[1]/a').text.split('\n')
            href = driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[{j}]/div/table/tbody/tr[{i}]/td[1]/a').get_attribute('href')
            try:
                RT = driver.find_element(By.XPATH, value=f"/html/body/main/div[3]/div/div/div/div[{j}]/div/table/tbody/tr[{i}]/td[2]/span").get_attribute('class')
                adaptive = driver.find_element(By.XPATH, value=f"/html/body/main/div[3]/div/div/div/div[{j}]/div/table/tbody/tr[{i}]/td[3]/span").get_attribute('class')
            except:
                RT = 'No'
                adaptive = 'No'
            test_type = driver.find_element(By.XPATH, value=f"/html/body/main/div[3]/div/div/div/div[{j}]/div/table/tbody/tr[{i}]/td[4]").text.split('\n')
            print(assessment_text, href, RT, adaptive, test_type)
            d_old.append({'test': assessment_text, 'href': href, 'RT': RT, 'adaptive': adaptive, 'test_type': test_type})
            i += 1
            try :
                assessment_text = driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[{j}]/div/table/tbody/tr[{i}]/td[1]/a')
            except:
                assessment_text = None

        try:
                # driver.find_element(By.XPATH, value=f'/html/body/main/div[3]/div/div/div/div[{j}]/ul/li[7]/a').click()


                # Save the full updated list
                with open("SHL_individual.pkl", "wb") as f:
                    pickle.dump(d_old, f)
                pagination_links = driver.find_elements(By.XPATH, "//ul[contains(@class, 'pagination')]/li/a")

                next_button = None
                for link in pagination_links:
                    if link.text.strip().lower() == "next":
                        next_button = link
                if next_button:
                    next_button.click()

                # WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located((By.XPATH, f"/html/body/main/div[3]/div/div/div/div[{2}]/div/table/tbody/tr[{i}]/td[1]/a"))  # Adjust this to what changes after the click
                # )
                j=2
        except:
                click = None







