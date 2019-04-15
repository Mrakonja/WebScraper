from selenium import webdriver
from selenium.webdriver.chrome.options import Options
base_url = "http://www.11811.rs"

def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("user-data-dir=selenium")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

def dobijanjeDelatnosti(url):
    driver.get(url)
    hrefs = []
    list_of_p_elements = driver.find_elements_by_xpaht("//a[@class='makrodelatnosNaslovna']")
    for element in list_of_p_elements:
        driver.get(element)
        linkovi = driver.find_elements_by_xpath("//a[@class='siviLink']")
        for link in linkovi:
            href_atribut = link.get_attribute("href")
            hrefs.append(href_atribut)
    return hrefs

