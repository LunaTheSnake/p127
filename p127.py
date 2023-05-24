#BeautifulSoup  Selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
start_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser =webdriver.Chrome('chromedriver')
browser.get(start_URL)
time.sleep(10)

def scrape():
    headers=["name", "light_years_from_earth", "planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]
    for i in range(0,201):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ultag in soup.find_all("ul", attrs={"class","exoplanet"}):
            litags= ultag.find_all("li")
            temp_list=[]
            for index, litag in enumerate(litags):
                if index==0:
                    temp_list.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(litag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        #browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        #browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter .writerows(planet_data)

scrape()
        