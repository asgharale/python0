import re

email = input()

res = re.search(r'[A-Za-z-_.0-9]+\@[A-Za-z]+\.[a-zA-Z]+', email)

if(res):
    print("OK")
else:
    print("WRONG")
