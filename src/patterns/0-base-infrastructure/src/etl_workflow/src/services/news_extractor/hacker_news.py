from typing import List
from datetime import datetime


from adapter.request.hacker_news import HackerNews as E_HackerNews
from services.news_extractor._base import News, NewsExtractor


class HackerNews(NewsExtractor):

    _extractor = E_HackerNews()

    def extract_news(self, limit: str = 5) -> List[News]:
        histories = []
        for item in self._extractor.get_top_stories()[:limit]:
            context = self._extractor.get_details_story(item)
            histories.append(
                News(
                    source=self._extractor.source,
                    id=item,
                    title=context.get("title"),
                    url=context.get("url"),
                    date=datetime.fromtimestamp(context.get("time"))
                )
            )
        return histories
