import requests
import random
import json
import sqlalchemy
from sqlalchemy import text
from time import sleep
import datetime

random.seed(100)

class AWSDBConnector:
    """
    This class handles the connection to the AWS database.
    """
    def __init__(self):
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306

    def create_db_connector(self):
        """
        Creates a database engine connection.
        """
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

def get_data_from_db(engine, data_type):
    """
    Retrieves a random row of data from the specified table in the database.
    """
    table_name = f"{data_type}_data"
    random_row = random.randint(0, 1000)
    query = text(f"SELECT * FROM {table_name} LIMIT {random_row}, 1")
    with engine.connect() as connection:
        result = connection.execute(query).first()
        return dict(result._mapping) if result else None

def post_data_to_api(data, data_type):
    """
    Posts data to the corresponding API endpoint.
    """
    invoke_url = f"https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/topics/0a5afda0229f.{data_type}"
    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    payload = json.dumps({"records": [{"value": data}]})
    response = requests.post(invoke_url, headers=headers, data=payload)
    return response.status_code

def stream_data(data, data_type):
    """
    Streams data to the corresponding streaming endpoint.
    """
    invoke_url = f"https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0a5afda0229f-{data_type}/record"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"StreamName": "{stream-name}", "Data": data, "PartitionKey": "category"})
    response = requests.put(invoke_url, headers=headers, data=payload)
    return response.status_code

def run_infinite_post_data_loop():
    """
    Runs an infinite loop that continuously fetches and posts data for different types.
    """
    connector = AWSDBConnector().create_db_connector()
    data_types = ['geo', 'pin', 'user']

    while True:
        for data_type in data_types:
            sleep(random.randrange(0, 2))
            data = get_data_from_db(connector, data_type)
            if data:
                print(f"Posting {data_type} data: {data}")
                post_data_to_api(data, data_type)
                stream_data(data, data_type)

if __name__ == "__main__":
    run_infinite_post_data_loop()
