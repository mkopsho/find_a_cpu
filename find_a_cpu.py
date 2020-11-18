import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

# Twilio setups (make into environment vars)
account = TWILIO_ACCOUNT_SID
token = TWILIO_ACCESS_TOKEN
client = Client(account, token)

# Controls
# newegg_url = 'https://www.newegg.com/amd-ryzen-9-3900x/p/N82E16819113103' # In stock (control)
# bhphoto_url = 'https://www.bhphotovideo.com/c/product/1558667-REG/amd_ryzen_3_3100_quad_core.html' # In stock (control)

# Targets
newegg_url = 'https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666' # Out of stock (target)
bhphoto_url = 'https://www.bhphotovideo.com/c/product/1598377-REG/amd_100_100000065box_ryzen_5_5600x_3_7.html' # Out of stock (target)

# Newegg
newegg_request = requests.get(newegg_url)
newegg_html_doc = newegg_request.text
newegg_soup = BeautifulSoup(newegg_html_doc, 'html.parser')

newegg_inventory = newegg_soup.find(class_="product-inventory")
if "In stock." in newegg_inventory.strings:
  client.messages.create(
    to=YOUR_VERIFIED_NUMBER, 
    from_=TWILIO_NUMBER, 
    body=f'Ryzen 5 5600X in stock at Newegg: {newegg_url}',
  )

# B&H Photo
bhphoto_request = requests.get(bhphoto_url)
bhphoto_html_doc = bhphoto_request.text
bhphoto_soup = BeautifulSoup(bhphoto_html_doc, 'html.parser')

bhphoto_inventory = bhphoto_soup.find(string="In Stock")
if bhphoto_inventory == "In Stock":
  client.messages.create(
    to=YOUR_VERIFIED_NUMBER,
    from_=TWILIO_NUMBER,
    body=f'Ryzen 5 5600X in stock at B&H Photo: {bhphoto_url}',
  )  

