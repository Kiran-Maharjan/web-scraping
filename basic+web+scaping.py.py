import bs4
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
#html function
page_soup=soup(page_html,"html.parser")

#page_soup.h1

#page_soup.p

#page_soup.body.span

containers=page_soup.findAll("div",{"class":"item-container"})

#len(containers)

#container.div.div.a
filename= "products.csv"
f=open(filename,"w")
header="brand, product_name, shipping_name \n"
f.write(header)

# In[16]:
for container in containers:
    #got the title.. we wantted
    brand_name=container.div.div.a.img["title"]

    title_container=container.findAll("a",{"class":"item-title"})
    product_name=title_container[0].text

    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping_name=shipping_container[0].text.strip()


    # In[ ]:

    print("brand:"+brand_name)
    print("product_name:"+product_name)
    print("shipping:"+shipping_name)

    f.write(brand_name + ","+ product_name.replace(",","|") + "," + shipping_name + "\n")

f.close()
