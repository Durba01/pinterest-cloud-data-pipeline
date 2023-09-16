import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text

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

def post_to_api(pin_result):
    invoke_url = "https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/topics/0a5afda0229f.pin"
    
    payload_data = {
        "index": pin_result["index"],
        "unique_id": pin_result["unique_id"],
        "title": pin_result["title"],
        "description": pin_result["description"],
        "poster_name": pin_result["poster_name"],
        "follower_count": pin_result["follower_count"],
        "tag_list": pin_result["tag_list"].split(","),
        "is_image_or_video": pin_result["is_image_or_video"],
        "image_src": pin_result["image_src"],
        "downloaded": pin_result["downloaded"],
        "save_location": pin_result["save_location"],
        "category": pin_result["category"]
    }
    
    payload = json.dumps({
        "records": [
            {
                "value": payload_data
            }
        ]
    })

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    response = requests.request("POST", invoke_url, headers=headers, data=payload)
    print(f'Response Status: {response.status_code}')

def run_infinite_post_data_loop():
    engine = new_connector.create_db_connector()  # Move the engine creation outside the loop
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 1000)

        with engine.connect() as connection:
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)
            
            #... [similar blocks for geo_result and user_result]
            
            print(pin_result)
            post_to_api(pin_result)

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
