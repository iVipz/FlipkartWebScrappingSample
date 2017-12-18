""" Sample Script to Scrap Flipkart.com"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = "https://www.flipkart.com/search?q=iphone"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"col _2-gKeQ"})

#print(len(containers))

#print(soup.prettify(containers[0]))

container =containers[0]
print(container.div.img["alt"])

price = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#price = container.findAll("div", {"class":"col col-5-12 _2o7WAb"})
print(price[0].text)

rating = container.findAll("div", {"class":"hGSR34 _2beYZw"})
print(rating[0].text)

filename="products.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    #price_container = container.findAll("div", {"class":"col col-5-12 _2o7WAb"})
    price_container = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class":"hGSR34 _2beYZw"})
    rating = rating_container[0].text

    #print("product_name :" + product_name)
    #print("price :" + price)
    #print("rating :" + rating)


print("Reached the end")
