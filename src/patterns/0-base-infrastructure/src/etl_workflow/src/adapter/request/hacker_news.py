from typing import List, Dict


from adapter.request._base import Request


class HackerNews(Request):
    
    @property
    def source(self) -> str:
        return "hacker-news"
    
    def get_top_stories(self) -> List[str]:
        return self._get(
            "https://hacker-news.firebaseio.com/v0/topstories.json"
        )

    def get_details_story(self, item: str) -> Dict[str, str]:
        return self._get(
            f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
        )
