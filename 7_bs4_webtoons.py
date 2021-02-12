import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# 네이버 웹툰 전체 목록 가져오기
soup = BeautifulSoup(res.text, "lxml")
# class속성이 title인 모든 "a" element를 반환
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())

    