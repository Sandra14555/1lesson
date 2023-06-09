import urllib.request
import requests

# opener = urllib.request.build_opener()
#
# response = opener.open("https://httpbin.org/get")
#
# print(response.read())
# res = requests.post("https://httpbin.org/post", data="Test data hello world" , headers={"h1":"My title"})
# print(res.text)
#
#
# response = requests.get("https://httpbin.org/get")
# print(response.text)

response = requests.get("https://bank.gov.ua/ua/markets/exchangerate-chart?cn%5B%5D=USD")
response_text = response.text

coin_list = []

response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if parse_elem1.startswith("₴"):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2.startswith("₴") and parse_elem2[1].isdigit():
                coin_list.append(parse_elem2)

usd = coin_list[0]
print("Usd =", usd)
