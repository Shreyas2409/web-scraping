from bs4 import BeautifulSoup
import requests
url= 'https://www.goodreads.com/en/book/show/36624102-immortal-talks'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
soup.extract() 
print(soup.find("h1","gr-h1 gr-h1--serif"))
print (soup.find("div","readable stacked"))




