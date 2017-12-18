""" Sample Script to Scrap Flipkart.com"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

my_url = "https://www.flipkart.com/search?q=iphone"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"col _2-gKeQ"})

#print(len(containers))

#print(soup.prettify(containers[0]))

container =containers[0]
#print(container.div.img["alt"])

price = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#price = container.findAll("div", {"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)

rating = container.findAll("div", {"class":"hGSR34 _2beYZw"})
#print(rating[0].text)

filename="products.csv"
try :
    f=open(filename,"w")
except IOError as err:
    print("Error reading the file " + filename)
    sys.exit(1)

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class":"col col-5-12 _2o7WAb"})
    #price_container = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class":"hGSR34 _2beYZw"})
    rating = rating_container[0].text

    #print("product_name :" + product_name)
    #print("price :" + price)
    #print("rating :" + rating)

    #string parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs. " + rm_rupee[1]
    split_price = add_rs_price.split('E')
    rem_upto = split_price[0].split("Up")
    final_price = rem_upto[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    lineItem = product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n"
    print(lineItem)
    f.write(lineItem)
f.close()
print("Reached the end")
