
# Indeed Job Scraper
# First import all the packages needed

import numpy as np 	#data structure
import pandas as pd  #manipulating data
import requests 	#to pull in HTML
from bs4 import BeautifulSoup as Soup 	#for parsing
from time import sleep #need to stop the code from continuously pulling too much data from a website, resulting in a ban
from random import randint

# Next create columns with names using pandas

col = ['Name', 'Company', 'City', 'Ratings', 'Summary', 'Date']
indeed = pd.DataFrame(columns = col)

# Create a for loop for the pages

for page in range(0,100):

# Insert url, and methods to get data from url

for page in range(0,100):
    url = "https://www.indeed.com/jobs?q=analyst&start={}"
    P_url = requests.get(url.format(10*page))
    P_html = P_url.text
    P_soup = Soup(P_html, 'html.parser')
    sleep(randint(2,10))

# Define containers based on HTML and what you want to pull

	containers = P_soup.findAll('div', {"data-tn-component": "organicJob"})
    #print(len(containers))
    #print(Soup.prettify(containers[0]))
    container = containers[0]
    for container in containers:
        Name = container.findAll('a', {"class": "jobtitle turnstileLink"})
        if len(Name) !=0:
            name = Name[0].text.strip()
        else:
            name = "NaN" 

# Rest are identical just tweek it towards the data for each container

 	Company = container.findAll('span', {"class":"company"})
        if len(Company) !=0:
            comp = Company[0].text.strip()
        else:
            comp = "NaN"

        City = container.findAll('span', {"class":"location accessible-contrast-color-location"})
        if len(City) !=0:
            city = City[0].text.strip()
        else:
            city = "NaN"
        
        ratings = container.findAll('span', {"class":"ratingDisplay"})
        if len(ratings) !=0:
            rat = ratings[0].text.strip()
        else:
            rat = "NaN"
        
        Summ = container.findAll('div', {"class":"summary"})
        if len(Summ) !=0:
            summ = Summ[0].text.strip()
        else:
            summ = "NaN"
            
        date = container.findAll('span', {"class":"date"})
        if len(date) !=0:
            dat = date[0].text.strip()
        else:
            dat = "NaN"

# Set up dataframe, and move data

	data = pd.DataFrame([[name, comp, city, rat, summ, dat]])
        data.columns = col
        indeed = indeed.append(data, ignore_index = True)

# Print out data

print(indeed)
indeed.to_excel("Output.xlsx")

# Also watch your indents they all have a purpose**
