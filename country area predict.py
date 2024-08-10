# linear regression
# برای پیش بینی این چنین مسایلی بهتر است راه حل خطی استفاده شود
import requests
from bs4 import BeautifulSoup as bs
import re
import mysql.connector
from sklearn import linear_model


# collecting data
r = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = bs(r.text, 'html.parser')
content = soup.find_all('div', attrs={'class':'col-md-4 country'})


# db setup
db_user = "root"#input("Enter your db user: ")
db_user_pass = "admin" #input("Enter your db user's password: ")
db_name = "country_data" #input("Enter your db name: ")
cnx = mysql.connector.connect(
    host="localhost",
    user=db_user,
    password=db_user_pass,
    database=db_name
)
cursor = cnx.cursor()
# cursor.execute("create table country_data (name varchar(200), capital varchar(200), population varchar(200), area varchar(200));")


# variables
x = []
y = []
i=0
for country in content:
    name = country.find('h3', attrs={'class':'country-name'}).getText()
    name = re.sub(r'\s*', '', name)
    capital = country.find('span', attrs={'class':'country-capital'}).getText()
    capital = re.sub(r'\s*', '', capital)
    population = country.find('span', attrs={'class':'country-population'}).getText()
    population = int(re.sub(r'\s*', '', population))
    area = country.find('span', attrs={'class':'country-area'}).getText()
    area = float(re.sub(r'\s*', '', area))
    cursor.execute(f"insert into country_data values (\"{name}\", \"{capital}\", \"{population}\", \"{area}\");")
    x.append([population])
    y.append(area)


cnx.commit()
cursor.close()
cnx.close()

# linear regression
reg = linear_model.LinearRegression()
reg.fit(x, y)

print(reg.predict([[80000000]])[0])