from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from parser.parse_any_topic import get_html, get_content, URL
from parser.parse_all import parse_all

router = APIRouter(
    prefix="",
    tags=["Pages"]
)


templates = Jinja2Templates(directory="FrontEnd")

@router.get("/")
def get_home_page(request : Request):
    all_articles = parse_all()
    response = {"request" : request, "articles" : all_articles["articles"], "sports" : all_articles["sports"], "relevants" : all_articles["relevants"], "travels" : all_articles["travels"], "mains" : all_articles["mains"], "edus" : all_articles["edus"]}

    
    return templates.TemplateResponse('main.html', response)

@router.get("/{name_of_genre}")
def get_sorted_news(request: Request, name_of_genre):
    html = get_html(url=URL, params=name_of_genre)
    articles = get_content(html.text)
    return templates.TemplateResponse('topic.html', {"request" : request, "name_of_genre" : name_of_genre, "articles" : articles})


# ./json/articles.json