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

def put_geo_to_api(geo_result):
    geo_stream_name = "streaming-0a5afda0229f-geo"
    geo_invoke_url = f"https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/geo_stream_name/record" # Replace this with your actual API URL for geo data

    payload_data = {
        "index": geo_result["ind"],
        "timestamp": geo_result["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),  # Formatting the datetime object to string
        "latitude": geo_result["latitude"],
        "longitude": geo_result["longitude"],
        "country": geo_result["country"]
    }

    payload = json.dumps({
        "records": [
            {
                "value": payload_data
            }
        ]
    })

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    response = requests.request("PUT", geo_invoke_url, headers=headers, data=payload)
    print(f'Response Status: {response.status_code}')


def run_infinite_post_data_loop():
    engine = new_connector.create_db_connector()  # Move the engine creation outside the loop
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 1000)

        with engine.connect() as connection:
            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)
            
                # Process and post each record individually
                print(geo_result)
                put_geo_to_api(geo_result)
            
            #... [similar blocks for other result types with different SQL queries]

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')