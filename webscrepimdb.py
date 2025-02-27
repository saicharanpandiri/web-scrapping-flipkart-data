from bs4 import BeautifulSoup
import requests
import pandas as pd
response=requests.get("https://www.flipkart.com/search?q=samsung%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
#below loop is for get name of mobiles
names=soup.find_all('div',class_="KzDlHZ")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
#below for loop is for get price of mobiles    
prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
#this loop is for rating of mobile   
ratings=soup.find_all('div',class_="XQDdHH")
rating=[]
for i in ratings[0:20]:
    d=i.get_text()
    rating.append(float(d))
#below is for images of mobiles
images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
#below loop is used for the links of mobiles    
links=soup.find_all('a',class_="CGtC98")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
    
    
df=pd.DataFrame()#row columns
df["Names"]=name
df["Prices"]=price
df["Ratings"]=rating
df["images"]=image
df["Links"]=link

print(df)
#command to get a csv file and get stored in data in csv
df.to_csv("mobiles.csv")



    