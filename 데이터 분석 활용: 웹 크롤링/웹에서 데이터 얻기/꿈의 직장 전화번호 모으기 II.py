import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['지점 이름', '주소', '전화번호'])

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

# BeautifulSoup 사용해서 HTML 코드 정리
soup = BeautifulSoup(response.text, 'html.parser')

branch_infos = []

# 모든 지점에 대한 태그 가져오기
branch_tags = soup.select('div.branch')

for branch_tag in branch_tags:
    # 각 태그에서 지점 이름, 전화번호 가져오기
    row = [
        branch_tag.select_one('p.city').get_text(),
        branch_tag.select_one('p.address').get_text(),
        branch_tag.select_one('span.phoneNum').get_text(),
    ]
    ws.append(row)

wb.save('오렌지_보틀.xlsx')