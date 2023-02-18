#!/usr/bin/env python
# coding: utf-8

# # HTML PARSER

# ## AIM

# Web scraping is used to collect information from various websites programmatically and be an expert in web scrapping to harvest the data effectively.
# 
# use Python libraries requests and Beautiful Soup
# 
# steps-
# 
#    Using the browser’s developer tools, inspect the HTML structure of the target site
#     
#    Scrap and parse the data from the web using requests and Beautiful Soup
#     
#    Develop a web scraping pipeline from start to finish
#     
#    Build a script that fetches data from the Web and displays relevant information in your console
# 

# ## Web scraping
A process of gathering information from the Internet.
"web scraping" for a process that involves automation
ensure that you are not violating any Terms of Service, while using the web-scrapping techniques
Automated web scraping process helps speed up the data collection process
# Challenges of Web Scrapping
# - Variety: Every website is different and unique
# - Durability: Websites constantly change
# 

# ### Worldometers Website

# build a web scraper that fetches the real-time Covid-19 data from worldometer website.
# 
# web scraper will parse the HTML on the site to pick out the relevant information
# 
# we can scrape any site on the Internet that you can look at, but the difficulty of doing so depends on the site.

# ### Inspect Data Source 

# first step is to get to know the website that you want to scrape.we should understand the site structure to extract the information that’s relevant for us.

# ### Inspect using Developer Tool

# understand the page structure to pick what you want from the HTML response
# 
# use developer tools to understand the structure of a website.
# 
# On Windows and Linux, you can access them by clicking the top-right menu button (⋮) and selecting More Tools → Developer Tools.
# 
# Windows/Linux: Ctrl+Shift+I
# 
# Developer tools allow us to interactively explore the site’s document object model (DOM) to better understand your source.

# ### Install Libraries

# You need the following Python Libraries
# 
#     BeautifulSoup4
#     Requests
#     pandas
#     lxml
# 

# In[1]:


pip install BeautifulSoup4


# In[2]:


pip install Requests


# In[3]:


pip install pandas


# In[4]:


pip install lxml


# ### Import libraries 

# In[5]:


from bs4 import BeautifulSoup


# In[6]:


import requests


# ### Request Permissions

# In[7]:


url = 'https://www.worldometers.info/coronavirus/'
html = requests.get(url)


# In[8]:


print(html.text)


# In[9]:


soup = BeautifulSoup(html.text,'lxml')


# In[10]:


print(soup.prettify())


# ## Inspect H1 Elements

# In[11]:


soup.h1


# In[12]:


soup.title


# In[13]:


soup.title.text


# In[14]:


header_h1 = soup.find_all(id="maincounter-wrap")
for head_h1 in header_h1:
    print(head_h1.h1.text)
    print(head_h1.div.span.text, end="\n"*2)


# In[15]:


scrp_table = soup.find('table', id='main_table_countries_today')
scrp_table


# ### Create Column List

# In[16]:


headers = []
for i in scrp_table.find_all('th'):
    title = i.text
    headers.append(title)


# In[17]:


headers


# In[18]:


headers

headers[10]
headers[10] = 'Tot Cases/1M pop'

headers[13]
headers[13] = 'Tests/1M pop'


# In[19]:


headers


# ### Create Dataframe and Fill 

# In[20]:


import pandas as pd


# In[21]:


scrapdata = pd.DataFrame(columns = headers)


# In[22]:


for tr in scrp_table.find_all('tr')[1:]:
    row_data = tr.find_all('td')
    row = [td.text for td in row_data]
    length = len(scrapdata)
    scrapdata.loc[length] = row


# In[23]:


scrapdata


# In[24]:


scrapdata.drop(scrapdata.index[0:8], inplace=True)
scrapdata.drop(scrapdata.index[228:236], inplace=True)
scrapdata.reset_index(inplace=True, drop=True)


# In[25]:


# Drop “#” column
scrapdata.drop('#', inplace=True, axis=1)


# In[26]:


scrapdata


# ## Export Dataframe to CSV

# In[28]:


scrapdata.to_csv('covid_data.csv', index=False)  # Export to cs

csv_data = pd.read_csv('covid_data.csv') # Try to read csv


# In[29]:


csv_data


# In[ ]:




