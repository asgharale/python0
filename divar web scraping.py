import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://divar.ir/s/tehran")

soup = bs(r.text, 'html.parser')
content = soup.find_all('div', attrs={'class':'post-list__widget-col-a3fe3'})

for post in content:
    show = False
    not_priced = True
    post_data = post.find_all('div', attrs={'class':'kt-post-card__description'})
    for data in post_data:
        if data.contents[0]=="توافقی" or data.contents[0]=="قیمت توافقی":
            show = True
            break

        # second part (new part)
        if 'تومان' in data.contents[0]:
            not_priced = False
    if show or not_priced:
        print(post.prettify())