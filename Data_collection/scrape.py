# Write your code here :-)
from bs4 import BeautifulSoup
import requests

url = "https://playbill.com/seasons?year=2010"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soups.findall