from bs4 import BeautifulSoup
import  requests
url= 'https://www.goodreads.com/en/book/show/36624102-immortal-talks'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
for s in soup("h1","gr-h1 gr-h1--serif"):
  s.decompose()

print(str(s))    
