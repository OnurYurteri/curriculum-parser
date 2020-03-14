from bs4 import BeautifulSoup
import requests
from googlesearch import search
import csv
from tldextract import extract as extractTLD

query="endüstri mühendisliği müfredat"

urls = []

print("Retrieving urls from google..")
for url in search(query, tld="com.tr", num=10, stop=10, pause=2): # num: how many urls will be get from each iteration, stop: number of urls to get, pause: time between requests, 2 second is ok, if it's lower google may block 
    urls.append(url)
print("Retrieved " + str(len(urls)) + " urls.")

print("Starting to iterate through urls..")
for url in urls:
    rowsToPrint = [] # To CSV
    try:
        html = requests.get(url).text
    except requests.exceptions.RequestException: # In case of commucation failure we want our script to continue
        pass
    soup = BeautifulSoup(html, "lxml")
    fileName = extractTLD(url).domain # just domain name for short file name
    tables = soup.find_all('table')
    print(str(fileName)+": "+ str(url)) # short name: url 
    for table in tables:
        for row in table.find_all('tr'):
            course = []
            for cell in row.find_all('td'):
                course.append(cell.get_text().replace('\xa0', ''))
            rowsToPrint.append(course)
    with open('curriculums/'+str(fileName)+'.csv', 'w', newline='') as file: # Create files under /curriculums folder
        writer = csv.writer(file)
        writer.writerows(rowsToPrint)


