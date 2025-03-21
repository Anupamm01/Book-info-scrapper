import requests
from bs4 import BeautifulSoup
import pandas
import json


current_page = 1

data = []

while(True):
    print(f"currently scrapping page {current_page}")
    url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.text,"html.parser")

    if(soup.title.text=="404 Not Found"):
        break
    else:
        
        all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {}
            name = book.find("img")["alt"]
            link = f"https://books.toscrape.com/catalogue/{book.find("a")["href"]}"
            price = book.find("p",class_="price_color").text[2:]
            stock = book.find("p",class_="instock availability").text.strip()
            
            item['Title'] = name
            item['Link'] = link
            item['Price'] = price
            item['Stock'] = stock

            data.append(item)

    current_page += 1

json_data = json.dumps(data, indent=4)

with open("json_data.json","w") as f:
    f.write(json_data)

df = pandas.DataFrame(data)

df.to_excel("books.xlsx")
df.to_csv("books.csv")





    
    
    

