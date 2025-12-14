locals {
  region             = "eu-west-1"
  hash_key_news_loader = "new_id"
  hash_key = "page"
  base_webpages = {
    reddit={
      page="Reddit",
      url="https://www.reddit.com/"
    }
    ycombinator={
      page="HackerNews",
      url="https://news.ycombinator.com/"
    }
  }
}