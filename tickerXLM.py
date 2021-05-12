import requests

while(1):
	page = requests.get("https://coinranking.com/coin/f3iaFeCKEmkaZ+stellar-xlm")

	from bs4 import BeautifulSoup

	soup = BeautifulSoup( page.conent , 'html.parser')

	priceAnnouncement = "XML Current: "
	changeAnnouncement = "24hr % change: "

	dataPrice = []
	for paragraph in soup.find(class_ = "coin-overview__price")
		dataPrice.append(paragraph.string)

	dataPrice[0].strip()

	dataChange = []
	for paragraph in soup.find(class_ = "coin-overview__change")
		dataChange.append(paragraph.string)

	dataChange[0].strip()

	disp = [0]*4

	disp[0] = priceAnnouncement
	disp[1] = " ".join(dataPrice[0].split())
	disp[2] = changeAnnouncement
	disp[3] = " ".join(dataChange[0].split())

	for i in disp:
		print(i)
