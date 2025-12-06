from typing import List
from datetime import date


from adapter.dynamodb import DynamoDB
from services.news_extractor._base import News
from services.news_extractor.hacker_news import HackerNews


NEWS_EXTRACTED = [HackerNews()]
DYNAMODB_ACCESS = DynamoDB("RelatedNews")


FORCED_NUMBER_NEWS_EXTRACTED_BY_SOURCE = 5


def get_news_from(date: date):
    extracted_news: List[News] = []
    
    # Going throw all existing news sources
    for func_news in NEWS_EXTRACTED:
        extracted_news.extend(func_news.extract_news(FORCED_NUMBER_NEWS_EXTRACTED_BY_SOURCE))

    extracted_news = filter_news_by_date(date, extracted_news)

    # Loads everything into the DATABASE
    DYNAMODB_ACCESS.set_items([val.to_dict() for val in extracted_news])
    return extracted_news


def filter_news_by_date(date: date, extracted_news: List[News]):
    return [val for val in extracted_news if val.date.day == date.day]
