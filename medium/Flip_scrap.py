#!/usr/bin/env python
# coding: utf-8

#importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# extracting urls of all the pages

pages_url =[] # array for storing url of all the pages
new_url = "https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=1"

# the url of the next/previous page should be compared with the url of the current page.
# This method works for this website as only the last numeral changes from current to next/previous website.
# Method may vary for different types of websites.


j=1
i=2                   # since the url ending with '1' is already stored in new_url and gets appended in pages_url.
while j<=50:          #the 51st page of this website returns an error. This means that we have 50 pages to extract urls from.
    j=j+1
    pages_url.append(new_url)
    new_url = "https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page="+ str(i)
    i=i+1

pages_url  #displaying all the url of all the pages.
products =[] # for storing product names
prices= [] #for storing corresponding product prices.

i=0
for page in pages_url:
    results = requests.get(page)
    soup = BeautifulSoup(results.text, 'html.parser')
    for x in soup2.findAll('div', attrs={'class':'_3liAhj'}):
        names = x.find('a', attrs={'class':'_2cLu-l'})
        cost =  x.find('div', attrs={'class':'_1vC4OE'})
        products.append(names.text)
        prices.append(cost.text)
        print (products[i] + ":" + prices[i])
        i = i+1

final_data = pd.DataFrame({'Name': products, 'Price': prices})
final_data.to_csv('test.csv') # 'test' name can changed to any name of choice
