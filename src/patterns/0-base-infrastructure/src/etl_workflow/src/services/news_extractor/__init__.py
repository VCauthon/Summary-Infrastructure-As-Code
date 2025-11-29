from typing import List
from datetime import date


from services.news_extractor._base import News
from services.news_extractor.hacker_news import HackerNews


NEWS_EXTRACTED = [HackerNews()]



def get_news_from(date: date):
    extr_news: List[News] = []
    for func_news in NEWS_EXTRACTED:
        extr_news.extend(func_news.extract_news(5))

    return [val for val in extr_news if val.date.day == date.day]
