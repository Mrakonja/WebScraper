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

file = open('germany_clubs_00.csv')
read = csv.reader(file)
linklist = list(read)
file.close()
f  = open("resultsGErmany1.csv", "w", )
for link in linklist:
       
            
            name = str(link).replace("['", "").replace("']", "").replace("'", "").replace(",", "")
            print(name)
            try:
                driver.get(name)
            except:
                f.write(str(name) + "not found" + "\n")

            elementPath = "//div[@class='clubLinkInfos']//div[@class='centerBlock']//a"
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, elementPath)))
                element = driver.find_element_by_xpath(elementPath)
                element.click()
            except:
                f.write(str(name) + "not found" + "\n")
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='egmClubInfoClubName']")))
                club_name = driver.find_element_by_xpath("//td[@class='egmClubInfoClubName']")
                club_name = club_name.text
                print(club_name)
                print("club_name " + club_name)
            except:
                club_name = "not found"
                print("club_namen " + club_name)
                


            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='egmClubInfo egmClubInfoHomepageLink']")))
                webAdress = driver.find_element_by_xpath("//a[@class='egmClubInfo egmClubInfoHomepageLink']")
                webAdress = webAdress.get_attribute("href")
                print("webadress " + webAdress)
            except:
                webAdress = "not found"
                print("webadress " + webAdress)

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html//div[@class='wrapperContainer club']//tr[5]/td[2]")))
                contact_person = driver.find_element_by_xpath("//html//div[@class='wrapperContainer club']//tr[5]/td[2]")
                contact_person = contact_person.text
                print("contact person " + contact_person)
            except:
                contact_person = "not found"
                print("contact person " + contact_person)

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html//div[@class='wrapperContainer club']//tr[5]/td[2]/a")))
                email = driver.find_element_by_xpath("//html//div[@class='wrapperContainer club']//tr[5]/td[2]/a")
                email = email.get_attribute("href")
                print("email " + email)
            except:
                email = "not found"
                print("email " + email)

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='egmClubInfo egmClubInfoAddressLink']")))
                adress = driver.find_element_by_xpath("//a[@class='egmClubInfo egmClubInfoAddressLink']")
                adress = adress.text
                print("adress " + adress)
            except:
                adress = "not found"
                print("adress " + adress)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html//div[@class='wrapperContainer club']//tr[6]")))
                TELEFON = driver.find_element_by_xpath("//html//div[@class='wrapperContainer club']//tr[6]")
                TELEFON = TELEFON.text
                print("TELEFON " + TELEFON)
            except:
                TELEFON = "not found"
                print("TELEFON " + TELEFON)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//html//div[@class='detailInfoWrapper']//tr[2]")))
                VEREINSNUMMER = driver.find_element_by_xpath("//html//div[@class='detailInfoWrapper']//tr[2]")
                VEREINSNUMMER = VEREINSNUMMER.text
                print("VEREINSNUMMER " + VEREINSNUMMER)
            except:
                VEREINSNUMMER = "not found"
                print("VEREINSNUMMER " + VEREINSNUMMER)

            f.write( club_name + "," + adress.replace("\n", "").replace("VEREINSADRESSE:", "") + "," + contact_person.replace("| E-Mail senden", "").replace("\n", "").replace("VEREINSADRESSE:", " ") + "," +  email.replace("mailto:", "").replace("\n", "").replace("VEREINSADRESSE:", "") + "," +  str(webAdress) +  "," +  VEREINSNUMMER.replace("\n", "").replace("VEREINSADRESSE:", "") + "," + TELEFON.replace("TELEFON:", "").replace("\n", "").replace("VEREINSADRESSE:", "") +"\n")

f.close()    
            