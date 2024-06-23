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

# for post in  posts:
#     address = post.find(name="address").text
#     correct_address = address.strip()
#     correct_href = post.find(name="a", class_="StyledPropertyCardDataArea-anchor", href=True)['href']
#     price = post.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
#     correct_price = "".join([num for num in price.split(" ")[0] if num.isdigit()])

# Keep browser open so you can manually log out
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(google_sheet)
time.sleep(1)
inputs = driver.find_elements(by=By.CLASS_NAME, value="whsOnd")
for data_input in inputs:
    data_input.send_keys("name")


