import requests
from bs4 import BeautifulSoup
import pandas

url = "https://books.toscrape.com/catalogue/page-51.html"

page = requests.get(url)


soup = BeautifulSoup(page.text,"html.parser")

print(soup.title.text.strip())



cureent_page = 1

while(True):
    url = f"https://books.toscrape.com/catalogue/page-{cureent_page}.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.text,"html.parser")

    if(soup.title.text=="404 Not Found"):
        break
    else:
        
        all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            name = book.find("img")["alt"]
            print(name)
    
    
    

