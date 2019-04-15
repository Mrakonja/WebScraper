#.send_keys('c')
# germnay eoncoding
#  headless chrome
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'chromedriver.exe')

url = "http://www.bfv.de/cms/bfv-startseite.html?navi=1"

driver.get(url)
def clickElement(elementPath):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, elementPath)))
        element = driver.find_element_by_xpath(elementPath)
        element.click()

f = open("germany_clubs_00.csv", "w")    

   
ifile = open('KeysREserve.csv')
read = csv.reader(ifile)
l = list(read)
ifile.close()


for row in l:
        url = "http://www.bfv.de/cms/bfv-startseite.html?navi=1"
        name = str(row).replace("['", "").replace("']", "")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='textVerein']")))
            formElement = driver.find_element_by_xpath("//input[@id='textVerein']")
            formElement.send_keys(name)
            clickElement("//a[@id='ui-id-2']")
            clickElement("//input[@id='btn_verein']")  
            clubUrl = driver.current_url
            print(type(clubUrl))
            print(clubUrl)
            f.write(clubUrl + "\n")  
            driver.get(url)
            formElement = driver.find_element_by_xpath("//input[@id='textVerein']")
            formElement.clear()
        except:
            clubUrl = " not found "
            f.write(str(name) + "," + clubUrl + "\n")
            driver.get(url)
            formElement = driver.find_element_by_xpath("//input[@id='textVerein']")
            formElement.clear()


        

        

