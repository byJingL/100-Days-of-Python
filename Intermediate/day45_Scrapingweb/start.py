from bs4 import BeautifulSoup

with open("website.html") as file:
    data = file.read()

# BeautifulSoup(): Class
# soup: Object
soup = BeautifulSoup(data, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(type(soup))
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText(), tag.get("href"))

# Get things by Attributes
heading = soup.find(name="h1", id="name")
print(heading)
heading2 = soup.find(name="h3",  class_="heading")
print(heading2.name, heading2.getText())

# Get things by CSS selectors
compony_url = soup.select_one(selector="p a")  # <a href="https://www.appbrewery.co/">The App Brewery</a>
# select ID
name = soup.select(selector="#name")  # [<h1 id="name">Angela Yu</h1>]
# select class
classes = soup.select(".heading")  # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]

