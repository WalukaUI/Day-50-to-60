import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"

res = requests.get(URL)
web_page = res.text

soup = BeautifulSoup(web_page, "html.parser")
posts = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

for post in  posts:
    address = post.find(name="address").text
    print(address.strip())
    href = post.find(name="a", class_="StyledPropertyCardDataArea-anchor", href=True)['href']
    print(href)
    price = post.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
    num_cost = "".join([num for num in price.split(" ")[0] if num.isdigit()])
    print(num_cost)


