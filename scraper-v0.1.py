import requests
from bs4 import BeautifulSoup

base_url="https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,30,10):
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    print(soup.prettify())
    all=soup.find_all("div",{"class":"propertyRow"})
    print(all)