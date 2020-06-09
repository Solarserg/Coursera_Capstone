#!/usr/bin/env python
# coding: utf-8

# In[2]:


conda install -c anaconda beautifulsoup4


# In[84]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[6]:


pip install lxml


# In[2]:


wiki_url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# In[72]:


#make the soup
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)


# In[67]:


#find table from soup
canada_zip = soup.find('table', attrs={'class' : "wikitable sortable"})
canada_zip


# In[87]:


#read soup table into pandas DataFrame
df = pd.read_html(str(canada_zip))[0]
df


# In[104]:


#make new df that excludes all rows with value of 'Not assigned' in column Borough, reset index
df = df[df.Borough != 'Not assigned']
df = df.reset_index(drop=True)
df.head()


# In[106]:


df.shape

