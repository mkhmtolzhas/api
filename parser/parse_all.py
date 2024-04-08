from fastapi import Request
from parser.parse_travel import get_content as get_travel_content, get_html as get_travel_html, URL as URL_TRAVEL
from parser.parse_edu import get_content as get_edu_content, get_html as get_edu_html, URL as URL_EDU
from parser.parse_relevant import get_content as get_relevant_content, get_html as get_relevant_html, URL as URL_RELEVANT
from parser.parse_news import get_content as get_news_content, get_html as get_news_html, URL as URL_NEWS
from parser.parse_sport import get_content as get_sport_content, get_html as get_sport_html, URL as URL_SPORT

def parse_all():
    html = get_news_html(url=URL_NEWS)
    articles = get_news_content(html.text)

    html = get_relevant_html(url=URL_RELEVANT)
    relevants = get_relevant_content(html.text)

    html = get_sport_html(url=URL_SPORT)
    sports = get_sport_content(html.text)

    html = get_travel_html(url=URL_TRAVEL)
    travels = get_travel_content(html.text)

    html = get_edu_html(url=URL_EDU)
    edus = get_edu_content(html.text)

    mains = [articles[0], relevants[0], sports[0], travels[0], edus[0]]
    return {
        "articles" : articles,
        "relevants" : relevants,
        "sports" : sports, 
        "travels" : travels, 
        "mains" :mains, 
        "edus" : edus
    }

if __name__ == "__main__":
    print(parse_all())