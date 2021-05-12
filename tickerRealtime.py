import requests

while(1):
	pages = rquests.get("https://www.coindesk.com/price/stellar")

	from bs4 import BeautifulSoup

	soup = BeautfulSoup( page.content, 'html.parser')

	priceAnnouncement = "XML Current: "
	changeAnnouncement = "24hr % Change: "

	dataPrice = []
	for paragraph in soup.find(class_ = "price-large")
		dataPrice.append(paragraph.string)

	print(dataPrice[0])