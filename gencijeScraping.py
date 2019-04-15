# vknjigovodstvene agencije 
# http://knjigovodje.paragraf.rs/

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
url = "http://knjigovodje.paragraf.rs/?ime=&grad=&oblasti=&page="
#chrome_options.add_argument("--headless")  
chrome_options.add_argument("--start-maximised")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

def NumberOfPages():
    for page_num in range(500):
        try:
            driver.get(url + page_num)
            return page_page_num
        except:
            print("Done")

def agency_link():
    list_of_em = []
    elements = driver.find_elements_by_xpath(   )
    for element in elements:
        elemt_text = element.text
        list_of_em = list_of_em.append(elemt_text)
        return list_of_em


#pages = NumberOfPages()
#print(pages)
href_list = []
for page_num in range(500):
    print(url + str(page_num))
    driver.get(url + str(page_num))
    agency_links = driver.find_elements_by_xpath("//h4//a")
    print(len(agency_links))
    for agency_link in agency_links:
        agency_link_text = angecy_link.text
        print(agency_link_text)
        href_list.append(agency_link_text)
    print(len(href_list))

    
    

