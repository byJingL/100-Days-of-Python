import requests
from bs4 import BeautifulSoup


# swap the orders of the list
def reverse_list(origin_list):
    left = 0
    right = len(origin_list) - 1
    while left <= right:
        origin_list[left], origin_list[right] = origin_list[right], origin_list[left]
        left += 1
        right -= 1
    return origin_list


# Avoid requesting too frequent, save the data to a file
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(URL)
# with open("web.txt", "w") as file:
#     file.write(response.text)

with open("web.txt") as file:
    webpage = file.read()
soup = BeautifulSoup(webpage, "html.parser")
# find all movies
movies = soup.find_all(name="h3", class_="title")
# Format movies list
movie_titles = [movie.getText() for movie in movies]
movies_list = reverse_list(movie_titles)
# Simple way to revers the list:
movie_titles = [movie.getText() for movie in movies]
movies_list2 = movie_titles[::-1]
print(movies_list)
print(movies_list2)

with open("top_100_movies.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")




