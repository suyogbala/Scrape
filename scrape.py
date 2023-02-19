#importing the libraries
import requests
from bs4 import BeautifulSoup
import csv

#assigning the main url to scrape to find sub-urls which starts with #StopRansomware
url = 'https://www.cisa.gov/uscert/ncas/alerts?page=0'

#sending the get request to the url
response = requests.get(url)

#parsing the html content with BeautifulSoup Library
soup  = BeautifulSoup(response.content, 'html.parser')

#Creating two empty lists to append the data
technical_title = []
Use = []
urls = []

#finding the links using the html parser which has a class of 'views-field views-field-title'
alerts = soup.findAll('div', {'class': 'views-field views-field-title'})

#Opened the csv file
with open('research.csv', 'w', newline = '') as file:
    #creating the csv writer object
    writer = csv.writer(file)
    #writitng the header row to the csv file
    writer.writerow(['Techniqual_title', 'Use'])