import requests
from bs4 import BeautifulSoup


response = requests.get("https://workey.codeit.kr/orangebottle/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

# 지점 이름, 주소, 전화번호를 리스트 형식으로 branch_infos에 넣어 주세요. 리스트도 보통 값과 다를 것 없이 append()해 주면 됩니다.

branch_infos = []
branch_info = soup.select('div.branch')

for tag in branch_info:
    branch_name = tag.select_one('p.city').get_text()
    address = tag.select_one('p.address').get_text()
    phone_number = tag.select_one('span.phoneNum').get_text()
    branch_infos.append([branch_name, address, phone_number])

print(branch_infos)