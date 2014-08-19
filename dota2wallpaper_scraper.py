from bs4 import BeautifulSoup
import os
import sys
import urllib2
import requests

dirname = "/home/surajsau/pstuff/dota2"

for i in range(1,33):
	url =  "http://www.dota2wallpapers.com/page/" + str(i)

	data = urllib2.urlopen(url).read()
	soup = BeautifulSoup(data)
	div_tags = soup.find_all("div", class_="lightboxLink")

	for div in div_tags:
		img_a_tag = div.find('a')
		img_url = img_a_tag['href']
		img_title = img_a_tag['title']
		try:
			pic = urllib2.urlopen(img_url).read()
			pic_path = os.path.join(dirname, img_title)
			print("Saving file: " + pic_path)
			out = open(pic_path, "wb")
			out.write(pic)
			out.close()
		except:
			print("Could not save file : " + img_title)

