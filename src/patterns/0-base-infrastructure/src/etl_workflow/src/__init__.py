import boto3
import botocore
from datetime import datetime



from services.news_extractor import get_news_from


def lambda_handler(event, context):
    print("")

if __name__ == "__main__":
    # TODO: Pending to load the news into DynamoDB
    news_to_be_load = get_news_from(datetime.now())
