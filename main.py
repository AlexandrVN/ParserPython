import requests
import json


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


# читання та запис *.html сторінки
def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("index.html", "w") as file:
        file.write(response.text)


# читання та запис *.json файлу
def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("result_page.json", "w", encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def get_collect(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    data = response.json()
    last_page = data.get("last_page")
    print(last_page)


def main():
    # get_page(url="https://mybeauty.ua/ru/search?\
    # latitude=50.448125\
    # &longitude=30.522332\
    # &address=%D0%9A%D0%B8%D0%B5%D0%B2\
    # &direction=fe347320-9080-40ec-9b66-4a6cf4994299")

    # get_json(url="https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=2\
    # &latitude=50.448125\
    # &longitude=30.522332\
    # &direction=fe347320-9080-40ec-9b66-4a6cf4994299\
    # &address=%D0%9A%D0%B8%D0%B5%D0%B2")

    # get_json(url="https://app.mybeauty.ua/api/v1/salon/nearest?\
    # page=2\
    # &perPage=10\
    # &city=kiev\
    # &direction=barbershopi\
    # &isMaster=0")

    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=2\
    # &latitude=50.448125\
    # &longitude=30.522332\
    # &searchText=%D0%91%D0%B0%D1%80%D0%B1%D0%B5%D1%80%D1%88%D0%BE%D0%BF%D0%B8\
    # &address=%D0%9A%D0%B8%D1%97%D0%B2"

    url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    page=1\
    &perPage=10\
    &city=dnipro\
    &direction=barbershopi\
    &isMaster=0"

    "https://app.mybeauty.ua/api/v1/salon/nearest?page=1&perPage=10&city=dnipro&direction=barbershopi&isMaster=0"
    "https://app.mybeauty.ua/api/v1/salon/nearest?page=1&perPage=10&city=kiev&direction=makiyazh&isMaster=0"

    get_json(url)
    get_collect(url)




if __name__ == '__main__':
    main()


