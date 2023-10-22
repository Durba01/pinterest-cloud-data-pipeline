import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
import datetime 

random.seed(100)

class AWSDBConnector:

    def __init__(self):
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

new_connector = AWSDBConnector()

def put_user_to_api(user_result):
    geo_invoke_url = "https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0a5afda0229f-user/record"  # Replace with your actual API URL for geo data

    # Extract date_joined and format it, if it's a valid datetime object
    date_joined = user_result.get("date_joined")
    formatted_date_joined = date_joined.strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the payload data
    payload_data = {
        "index": user_result.get("ind"),
        "first_name": user_result.get("first_name"),
        "last_name": user_result.get("last_name"),
        "age": user_result.get("age"),
        "date_joined": formatted_date_joined
    }

    # Define the payload structure for streaming
    payload = json.dumps({
        "StreamName": "{stream-name}",  # Replace with your actual stream name
        "Data": payload_data,
        "PartitionKey": "age"  # Replace with a suitable partition key
    })

    headers = {'Content-Type': 'application/json'}
    response = requests.request("PUT", geo_invoke_url, headers=headers, data=payload)
    print(f'Response Status: {response.status_code}')


def run_infinite_post_data_loop():
    engine = new_connector.create_db_connector()  # Move the engine creation outside the loop
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 1000)

        with engine.connect() as connection:
            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
                # Process and post each record individually
                print(user_result)
                put_user_to_api(user_result)
            
            #... [similar blocks for other result types with different SQL queries]

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')