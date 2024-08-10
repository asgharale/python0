import requests
from bs4 import BeautifulSoup as bs
import re
import mysql.connector

# web data collecting
r = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = bs(r.text, 'html.parser')
content = soup.find_all('div', attrs={'class':'col-md-4 country'})

# database setup
db_user = input("Enter your db user: ")
db_user_pass = input("Enter your db user's password: ")
db_name = input("Enter your db name: ")
cnx = mysql.connector.connect(
    host="localhost",
    user=db_user,
    password=db_user_pass,
    database=db_name
)
cursor = cnx.cursor()
cursor.execute("create table country_data (name varchar(200), capital varchar(200), population varchar(200), area varchar(200));")

for i in range(20):
    country = content[i]
    name = country.find('h3', attrs={'class':'country-name'}).getText()
    name = re.sub(r'\s*', '', name)
    capital = country.find('span', attrs={'class':'country-capital'}).getText()
    capital = re.sub(r'\s*', '', capital)
    population = country.find('span', attrs={'class':'country-population'}).getText()
    population = int(re.sub(r'\s*', '', population))
    area = country.find('span', attrs={'class':'country-area'}).getText()
    area = re.sub(r'\s*', '', area)
    cursor.execute(f"insert into country_data values (\"{name}\", \"{capital}\", \"{population}\", \"{area}\");")

cnx.commit()
cursor.close()
cnx.close()