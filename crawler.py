import requests
import sys
from bs4 import BeautifulSoup

url=  'https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php'
response = requests.get(url,verify=False)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('a', href=True, class_="btn btn-success btn-lg")
for res in titles:
    print(res)