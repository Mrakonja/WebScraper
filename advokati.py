import selenium
from urllib.request import urlopen
import csv
import datetime
from selenium import webdriver
import time

def click_next():
    try:
        clickelement = driver.find_element_by_xpath("//a[@class='paginate_button next']")
    except:
        clickelement = "not found"
    if clickelement == "not found":
        print('scraping done')
    else:
        clickelement.click()
def get_advokat()
    lista_advokata = driver.find_elements_by_xpath("//tbody//tr")
    for advokat in lista_advokata:
        print(advokat.get_attribute('innerHTML'))
    
    return listamo 
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
#executable_path="./chromedriver"
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://akb.org.rs/imenik/")



