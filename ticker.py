import requests

while(1):
	page = requests.get("https://coinranking.com/coin/a91GCGd_u96cF+dogecoin-doge")

	from bs4 import BeautifulSoup

	soup = BeautifulSoup( page.content , 'html.parser')

	dogePriceAnnouncement = "Doge current: "
	dogeChangeAnnouncement = "24hr % change: " 

	dogeDataPrice = []
	for paragraph in soup.find(class_ = "coin-overview__price"):
		dogeDataPrice.append(paragraph.string)

	dogeDataPrice[0].strip()

	dogeDataChange = []
	for paragraph in soup.find(class_ = "coin-overview__change"):
		dogeDataChange.append(paragraph.string)

	dogeDataChange[0].strip()

	disp = [0]*8

	disp[0] = dogePriceAnnouncement
	disp[1] = " ".join(dogeDataPrice[0].split())
	disp[2] = dogeChangeAnnouncement
	disp[3] = " ".join(dogeDataChange[0].split())

	page = requests.get("https://coinranking.com/coin/ZlZpzOJo43mIo+bitcoincash-bch")

	soup = BeautifulSoup( page.content, 'html.parser')

	bchPriceAnnouncement = "BCH current: " 
	bchChangeAnnouncement = "24hr % change: "

	bchDataPrice = []
	for paragraph in soup.find(class_ = "coin-overview__price"):
		bchDataPrice.append(paragraph.string)

	bchDataPrice[0].strip()

	bchDataChange = []
	for paragraph in soup.find(class_ = "coin-overview__change"):
		bchDataChange.append(paragraph.string)

	bchDataChange[0].strip()

	disp[4] = bchPriceAnnouncement
	disp[5] = " ".join(bchDataPrice[0].split())
	disp[6] = bchChangeAnnouncement
	disp[7] = " ".join(bchDataChange[0].split())

	for i in disp:
		print(i)

	print("")