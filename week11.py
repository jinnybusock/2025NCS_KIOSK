import requests

#url= f"https://wttr.in/incheon"
#url= f"https://wttr.in/incheon?&n&Q"
url= f"https://wttr.in/incheon?&0&Q"
response= requests.get(url)
#print(response)
#print(response.status_code)

if response.status_code== 200:
    print(response.text.strip())

else:
    print(f"상태 코드: {response.status_code}")
