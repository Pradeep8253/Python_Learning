from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Chrome/81.0.4044.138" }


respons = requests.get("https://tech.target.com/blog/hardening-the-registers",headers)
your_web_page = respons.text

soup = BeautifulSoup(your_web_page, "html.parser")
print(soup.title)




# with open("Website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup)
# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)
#
# for tag in all_anchor_tag:
#     print(tag.get("href"))