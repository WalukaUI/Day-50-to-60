import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

google_sheet = "https://docs.google.com/forms/d/e/"
URL = "https://appbrewery.github.io/Zillow-Clone/"

res = requests.get(URL)
web_page = res.text

soup = BeautifulSoup(web_page, "html.parser")
posts = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

# Keep browser open so you can manually log out
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

for post in posts:
    data = []
    address = post.find(name="address").text
    correct_address = address.strip()
    data.append(correct_address)

    price = post.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
    correct_price = "".join([num for num in price.split(" ")[0] if num.isdigit()])
    data.append(correct_price)

    correct_href = post.find(name="a", class_="StyledPropertyCardDataArea-anchor", href=True)['href']
    data.append(correct_href)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(google_sheet)

    btn = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    inputs = driver.find_elements(by=By.CLASS_NAME, value="whsOnd")
    time.sleep(0.1)
    inputs[0].send_keys(correct_address)
    inputs[1].send_keys(f"${correct_price}")
    inputs[2].send_keys(correct_href)
    btn.click()





