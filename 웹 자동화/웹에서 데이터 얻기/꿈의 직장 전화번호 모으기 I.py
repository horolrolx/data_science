import requests
from bs4 import BeautifulSoup

# 여기에 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/orangebottle/index")
phone_numbers = response.text

soup = BeautifulSoup(phone_numbers, 'html.parser')
program_title_tags = soup.select('span.phoneNum')

phone_numbers = []
for tag in program_title_tags:
    phone_numbers.append(tag.get_text())

# 테스트 코드
print(phone_numbers)