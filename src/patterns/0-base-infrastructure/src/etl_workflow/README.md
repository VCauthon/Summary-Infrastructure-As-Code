# ETL Workflow

Code that scrapes news from the internet and loads it into DynamoDB.

This code will be zipped and wrapped as a Lambda. Because of that all the libraries used by the services must be downloaded beforehand.

If you need to update any package from the requirements.txt execute the following command:
```bash
pip install -r ./requirements.txt -t ./src
```

> TODO: A better approach from this it would be to make that the requirements are been downloaded on the terraform processes
> TODO: This webapp does not follow best practices as it does not even have a test.