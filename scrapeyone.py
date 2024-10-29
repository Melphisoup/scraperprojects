import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
target_url="https://www.scrapethissite.com/pages/simple/"
driver.get(target_url)
country = driver.find_elements(By.CLASS_NAME, "country-name")
wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d : country)
filename = "data.csv"

file = open(filename, 'w', newline='')
with file:
    write = csv.writer(file)
    write.writerows(country)
