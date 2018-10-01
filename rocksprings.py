import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c, "html.parser")
all=soup.find_all("div",{"class":"propertyRow"})
#print(all[0].find("h4",{"class":"propPrice"}).text.strip())
#instead of strip you can use replace("\n","").replace(" ","")

#use try and except for unknown results / not existing results

for item in all:
    print(item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        print(item.find("span",{"class","infoBed"}).find("b").text)
    except:
        pass
    try:
        print(item.find("span",{"class","infoSqFt"}).find("b").text)
    except:
        pass
    try:
        print(item.find("span",{"class","infoValueFullBath"}).find("b").text)
    except:
        pass
    try:
        print(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
    except:
        pass
    print(" ")