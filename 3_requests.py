import requests
res = requests.get("http://google.com")
print("응답 코드 : ",res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status() #오류가 생기면 바로 오류를 내뱉고 프로그램을 끝내도록 한다.
print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoggle.html", "w", encoding="utf-8") as f:
    f.write(res.text)