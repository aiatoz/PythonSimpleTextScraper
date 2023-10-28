# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:18:34 2023

@author: Krishna
"""

#Scraping and filtering out data

#Url lib page : https://pypi.org/project/urllib3/
#BeautifulSoup lib page : https://pypi.org/project/beautifulsoup4/

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib3


def filterTag(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def htmlToText(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.find_all(string=True)
    visible_texts = filter(filterTag, texts)
    return u" ".join(t.strip() for t in visible_texts)


req = urllib3.PoolManager()
response = req.request('GET', "https://en.wikipedia.org/wiki/Smooth_toadfish")
htmlContent = response.data
#html = BeautifulSoup(res.data, 'html.parser')

scrapedText = htmlToText(htmlContent)
print(scrapedText)