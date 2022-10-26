import requests
import pprint

API_KEY = 'xxxx'
SEARCH_POINT = 'https://api.themoviedb.org/3/search/movie'
DETAIL_POINT = 'https://api.themoviedb.org/3/movie'
movie_name = 'The Matrix'

params = {
    'api_key': API_KEY,
    'query': movie_name,
}
response = requests.get(SEARCH_POINT, params=params)
response.raise_for_status()
data = response.json()['results']
print(pprint.pp(data))

movie_id = 603
params2 = {
    'api_key': API_KEY,
}
response2 = requests.get(f'{DETAIL_POINT}/{movie_id}', params=params2)
response2.raise_for_status()
detail = response2.json()
year = detail['release_date'].split('-')[0]
print(year)
print(detail['overview'])
