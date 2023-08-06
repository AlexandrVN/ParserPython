import requests
import json

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


def get_response(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    return response


# читання та запис *.html сторінки
def get_html(url):
    with open("index.html", "w") as file:
        file.write(get_response(url).text)


# читання та запис *.json файлу
def get_json(url):
    with open("result_page.json", "w", encoding="utf-8") as file:
        json.dump(get_response(url).json(), file, indent=4, ensure_ascii=False)


def get_collection(url):
    data = get_response(url).json()
    last_page = data.get("last_page")
    total_items = data.get("total_items")

    return last_page, total_items


def get_category(url):
    ##### id категорії послуги (??? по ним зібрати колекцію послуг ???)
    # "0": {"masterServiceDirections": {"id": "fe347320-9080-40ec-9b66-4a6cf4994299"}}
    ##### категорії послуг конкретного салону
    # "0": {"masterServiceDirections": {"translations": {"original": {"name": "\u0411\u0430\u0440\u0431\u0435\u0440\u0448\u043e\u043f\u044b"}}}}
    ##### назва
    # "0": {"translations": {"original": {"name": "ES Beauty Bar"}}}
    ##### адреса
    # "0": {"salonLocations": {"location": {"translations": {"original": {"address": "\u043c. \u041a\u0438\u0457\u0432, \u0432\u0443\u043b. \u0411\u043e\u0440\u0438\u0441\u0430 \u0413\u0440\u0456\u043d\u0447\u0435\u043d\u043a\u0430, 4"}}}}}
    ##### країна
    # "0": {"salonLocations": {"location": {"translations": {"original": {"country": "\u0423\u043a\u0440\u0430\u0457\u043d\u0430"}}}}}
    ##### посилання
    # "0": {"translations": {"original": {"siteUrl": null}}}

    pass
