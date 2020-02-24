from bs4 import BeautifulSoup
import requests

metuCirrUrl = "https://ie.metu.edu.tr/tr/endustri-muhendisligi-lisans-ogretim-programi"
bounCirrUrl = "http://www.ie.boun.edu.tr/?q=tr/icerik/akademik-program"


metuHtml = requests.get(metuCirrUrl).text # Replace 'metuCirrUrl' with any url, eg: bounCirrUrl
soup = BeautifulSoup(metuHtml, "lxml")
tables = soup.find_all('table')
for table in tables:
    for row in table.find_all('tr'):
        course = []
        for cell in row.find_all('td'):
            course.append(cell.get_text().replace('\xa0', ''))
        print(course)
        print()