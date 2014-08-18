#!/usr/bin/env python

import os
import requests
import sys
import urllib
from bs4 import BeautifulSoup
import hashlib

def get_pic(number_imgs, timespan):
    """Returns a list of the specified number of top images over the specified
    timeframe from wallbase.cc
    """
    url = "http://wallbase.cc/search?q=dota"
    opts = {
        'section':'wallpapers', 'q':'dota', 'res_opt':'eqeq', 
        'res':'1366x768', 'order_mode':'desc', 'order':'favs',
        'aspect':'1.77', 'purity':'100','board':'21', 'thpp':number_imgs,
        'ts':timespan
    }
    htmltext = requests.get(url, params = opts)
    page_urls = []
    img_urls = []
    soup = BeautifulSoup(htmltext.content)
    results = soup.findAll("a")

    for r in results:
        if "http://wallbase.cc/wallpaper/" in r['href']:
            page_urls.append(r['href'])

    for p in page_urls:
        wp_page = requests.get(p)
        wp_soup = BeautifulSoup(wp_page.content)
        wp_results = wp_soup.findAll("img")
        for res in wp_results:
            if "http://wallpapers.wallbase.cc/" in res['src']:
                img_urls.append(res['src'])

    return img_urls

image_count = 0
dirname = "/dirpath/"

def save_pic(url, count):
    """Saves a file to disk when given a URL"""
    file_ext = url.split(".")[-1]
    to_save = (dirname + str(count) + "." + file_ext)
    if to_save != "":
        if os.path.isfile(to_save):
            print(dirname + str(count) + "." + str(file_ext) + "\texists, skipping...")
        else:
            print(dirname + str(count) + "." + str(file_ext) + "\tdownloading...")
            urllib.urlretrieve(url, to_save)

if __name__ == "__main__":
    for img in get_pic(60, "3d"):
    	image_count += 1
        save_pic(img, image_count)

