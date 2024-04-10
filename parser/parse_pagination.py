import requests
from bs4 import BeautifulSoup
import json
HOST = "https://tengrinews.kz/"
URL = "https://tengrinews.kz/search/page/"
HEADERS = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}

hosts = ("https://tengrisport.kz/", "https://tengritravel.kz/", "https://tengriauto.kz/")

def get_html(url, params = "", page = 1):
    request = requests.get(url + str(page) + "/?field=all&text=" + params, headers=HEADERS)
    print(url + str(page) + "/?field=all&text=" + params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="content_main_item")
    articles = []
    for item in items:
        try:
            fixed =False
            for h in hosts:
                if h in item.find("a").get("href"):
                    link = item.find("a").get("href")
                    fixed = True
                    break
            if not fixed:
                link = HOST + item.find("a").get("href")
            articles.append(
                {
                    "title" : item.find("span", class_="content_main_item_title").find('a').get_text(strip = True),
                    "link" : link,
                    "image" : item.find("a").find("picture").find("img").get("src")
                }
            )
        except:
            pass
    return articles


def parser():
    html = get_html(url=URL, params="life", page=2)
    articles = get_content(html.text)
    for i in articles:
        print(i["title"])
    with open("./idk.json", "x") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser()
