# Отримати категорії послуг
# Отримати по м.Київ перелік всіх зареєстрованних на сайті салонів з переліком послуг по кожному (назва, адреса, посилання та послуги)
# Записати результат в *.csv

import myFunctions as mf
import pandas as pd


def main():
    # посилання сформоване з "home-categories"
    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=1\
    # &latitude=50.4501\
    # &longitude=30.5234\
    # &direction=fe347320-9080-40ec-9b66-4a6cf4994299\
    # &address=%D0%9A%D0%B8%D1%97%D0%B2,%20Ukraine"

    # посилання сформоване з "footer__main--nav"
    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # page=1\
    # &perPage=10\
    # &city=kiev\
    # &direction=makiyazh\
    # &isMaster=0"

    # "total_items": 97,
    # "last_page": 10,
    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=1\
    # &searchText=%D0%9C%D0%B0%D0%BA%D1%96%D1%8F%D0%B6\
    # &latitude=50.448125\
    # &longitude=30.522332\
    # &address=%D0%9A%D0%B8%D1%97%D0%B2"

    # "total_items": 87,
    # "last_page": 9,
    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=1\
    # &latitude=50.4501\
    # &longitude=30.5234\
    # &direction=71450fe6-1355-4b58-97d1-8b2ddb848f73\
    # &address=%D0%9A%D0%B8%D1%97%D0%B2,%20Ukraine"

    # "total_items": 18,
    # "last_page": 2,
    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=1\
    # &latitude=50.4501\
    # &longitude=30.5234\
    # &direction=71450fe6-1355-4b58-97d1-8b2ddb848f73\
    # &address=%D0%9A%D0%B8%D1%97%D0%B2,%20Ukraine\
    # &isMaster=1"

    # "total_items": 69,
    # "last_page": 7,
    # url = "https://app.mybeauty.ua/api/v1/salon/nearest?\
    # perPage=10\
    # &page=1\
    # &latitude=50.4501\
    # &longitude=30.5234\
    # &direction=71450fe6-1355-4b58-97d1-8b2ddb848f73\
    # &address=%D0%9A%D0%B8%D1%97%D0%B2,%20Ukraine\
    # &isMaster=0"

    # f.get_html(url)
    # f.get_json(url)
    # f.get_collect(url)

    url = "https://app.mybeauty.ua/api/v1/salon/nearest?perPage=10&page=1&latitude=50.4501&longitude=30.5234&searchText=%D0%91%D0%B0%D1%80%D0%B1%D0%B5%D1%80%D1%88%D0%BE%D0%BF%D0%B8&address=%D0%9A%D0%B8%D1%97%D0%B2,%20Ukraine"
    pages = mf.get_collection(url)

    # page = 1
    # perPage = 10
    # city = 'kiev'
    # direction = 'makiyazh'
    # for i in range(0, pages[0]):
    #     url_page = (f"https://app.mybeauty.ua/api/v1/salon/nearest?page={page+i}&perPage={perPage}&city={city}&direction={direction}&isMaster=0")
    #     data = f.get_response(url_page).json()
    #     # last_page = data.get("last_page")
    #     # total_items = data.get("total_items")
    #
    #     print(url_page)

    page = 1
    item_end = 10
    item_description = {'name': [],
                        'siteUrl': []}
    for i in range(7, pages[0]):
        url_page = (f"https://app.mybeauty.ua/api/v1/salon/nearest?perPage=10&page={page + i}&latitude=50.4501&longitude=30.5234&searchText=%D0%91%D0%B0%D1%80%D0%B1%D0%B5%D1%80%D1%88%D0%BE%D0%BF%D0%B8&address=%D0%9A%D0%B8%D1%97%D0%B2,%20Ukraine")
        data = mf.get_response(url_page).json()
        # last_page = data.get("last_page")
        # total_items = data.get("total_items")
        if i + 1 == pages[0]:
            item_end = pages[1] % item_end

        # item = 0
        # print(type(data[str(item)]))
        # print(data[str(item)]['name'])
        # item_description.append(data[str(item)]['name'])


        for item in range(0, item_end):
            # item_description.append(data[str(item)]['name'])
            item_description['name'].append(data[str(item)]['name'])
            item_description['siteUrl'].append(data[str(item)]['translations']['original']['siteUrl'])
            # print(type(data[str(item)]))
            # print(data[str(item)])
            # item_description.append(data[str(item)]['translations']['original']['name'])
            # print(data[str(item)]["translations"]["original"]["name"])

            # item_description.append(data.get(item))

            # print(type(data.get(item).get("translations").get("original").get("name")))



        # print(url_page)

    print(item_description)


if __name__ == '__main__':
    main()
