import requests

rating_pages = []

for year in range(2010, 2013):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekIndex)
            response = requests.get(url)
            rating_pages.append(response.text)

print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드