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

def post_to_api(user_data):
    # Extract date_joined and format it, if it's a valid datetime object
    date_joined = user_data.get("date_joined")
    formatted_date_joined = date_joined.strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the payload data
    payload_data = {
        "index": user_data.get("ind"),
        "first_name": user_data.get("first_name"),
        "last_name": user_data.get("last_name"),
        "age": user_data.get("age"),
        "date_joined": formatted_date_joined
    }
    
    # Wrap it in the structure you've provided
    payload = json.dumps({
        "records": [
            {
                "value": payload_data
            }
        ]
    })
    
    # Assuming you've got a URL for user data
    invoke_url = "https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/topics/0a5afda0229f.user"
    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    response = requests.request("POST", invoke_url, headers=headers, data=payload)
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
            
            #... [similar blocks for geo_result and user_result with different SQL query]
            
            print(user_result)
            post_to_api(user_result)

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')