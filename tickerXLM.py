import requests

# LED Matrix Prerequisites
import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

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

	for i in disp
		print(i)

	print("")

	serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)

    for i in range(len(disp)):
        show_message(device, disp[i], fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02) #Change the value of 'scroll_delay' to change the Scrolling Speed
