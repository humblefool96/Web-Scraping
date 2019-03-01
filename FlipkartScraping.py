from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

#opening up theconnection, grabing the page
u_client = ureq(my_url)
page_html = u_client.read()
u_client.close()

#html parsing
page_soup = soup(page_html,"html.parser")
#grab each product
containers  = page_soup.findAll("div",{"class": "_1-2Iqu row"})

filename = "Mobiles.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Brand, Rating, Number_of_Rating, Price\n"
f.write(headers)
count = 0
for container in containers:
    brand_name = container.div.div.text

    ratings = container.findAll("div", {"class": "hGSR34 _2beYZw"})
    rating = ratings[0].text

    noofrating = container.findAll("span", {"class": "_38sUEc"})
    number_of_rating = noofrating[0].text

    price_list = container.findAll("div", {"class": "_3auQ3N _2GcJzG"})
    price = price_list[0].text
    count = count + 1
    f.write(brand_name + "," + rating + "," + number_of_rating.replace("," , "|") + "," + price.replace("," , "|") + "\n")
    #print("brand: "+ brand_name)
    #print("rating: "+ rating)
    #print("number_of_rating: "+ number_of_rating)
    #print("price: "+ price)
    print(count)
f.close()
