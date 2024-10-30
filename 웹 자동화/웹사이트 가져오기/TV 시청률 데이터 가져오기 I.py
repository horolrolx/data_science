import requests


response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

print(rating_page)