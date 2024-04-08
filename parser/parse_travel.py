import requests
from bs4 import BeautifulSoup
import json
HOST = "https://tengritravel.kz/"
URL = "https://tengritravel.kz/"
HEADERS = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}
JSON = "articles.json"

def get_html(url, params = ""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("article", class_="grid-item")
    articles = []
    for item in items:
        try:
            articles.append(
                {
                    "title" : item.find("div", class_="entry-content").find("header", class_="entry-header").find('h2').find('a').get_text(strip = True),
                    "link" : HOST + item.find("div", class_="post-formats-wrapper").find("a").get("href"),
                    "image" : HOST + item.find("div", class_="post-formats-wrapper").find("a").find("img").get("src")
                }
            )
        except:
            pass
    return articles


def parser():
    html = get_html(url=URL)
    articles = get_content(html.text)
    with open("./api/json/travel-articles.json", "w") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser()
