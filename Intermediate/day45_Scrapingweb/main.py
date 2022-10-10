from bs4 import BeautifulSoup
import requests

# # Avoid requesting many times, save the data to a text file
# response = requests.get("https://news.ycombinator.com/news")
# with open("web.txt", "w") as file:
#     file.write(response.text)

# yc_webpage and response.text have the same data type: <class 'str'>
# yc_webpage = response.text
with open("web.txt") as file:
    yc_webpage = file.read()

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)

article_titles = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")
for article in articles:
    text = article.get_text()
    link = article.get("href")
    article_titles.append(text)
    article_links.append(link)

article_scores = [int(info.getText().split()[0]) for info in soup.find_all(name="span", class_="score")]

temp = 0
for i in range(len(article_scores)):
    if article_scores[i] > temp:
        index = i
        temp = article_scores[i]
print(temp, index)

largest_number = max(article_scores)
largest_index = article_scores.index(largest_number)
print(largest_number, largest_index)

print(f"The article with highest score:\n"
      f"Title: {article_titles[index]}\n"
      f"Link: {article_links[index]}\n"
      f"Score: {article_scores[index]}")
