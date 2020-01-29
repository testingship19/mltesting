#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


# In[3]:


url = "https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=1"
results = requests.get(url) #request to fetch the url    
soup = BeautifulSoup(results.text, 'html.parser') #parsing the url
pages_url =[]
new_url = "https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page=1"
j=1
i=2
while j<=50:
    j=j+1
    pages_url.append(new_url)
    new_url = "https://www.flipkart.com/mobile-accessories/cases-and-covers/pr?sid=tyy%2C4mr%2Cq2u&otracker=nmenu_sub_Electronics_0_Mobile+Cases&page="+ str(i)
    i=i+1


# In[4]:


products =[]
prices= []
i=0
for page in pages_url:
    results2 = requests.get(page)
    soup2 = BeautifulSoup(results2.text, 'html.parser')
    for x in soup2.findAll('div', attrs={'class':'_3liAhj'}):
        names = x.find('a', attrs={'class':'_2cLu-l'})
        cost =  x.find('div', attrs={'class':'_1vC4OE'})
        products.append(names.text)
        prices.append(cost.text)
        print (products[i] + ":" + prices[i])
        i = i+1


# In[15]:


final_data = pd.DataFrame({'Name': products, 'Price': prices})
[x[1:] for x in final_data.Price]
final_data


# In[14]:


final_data.to_csv('test.csv')


# In[ ]:





# In[ ]:




