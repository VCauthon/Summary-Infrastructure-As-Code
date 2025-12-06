from datetime import datetime

from services.news_extractor import get_news_from


def lambda_handler(event, context):
    news_retrieved = get_news_from(datetime.now())
    return {
        "news_retrieved": len(news_retrieved)
    }
