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

# Define your stream names
geo_stream_name = "streaming-0a5afda0229f-geo"
pin_stream_name = "streaming-0a5afda0229f-pin"
user_stream_name = "ystreaming-0a5afda0229f-user"

# Construct the invoke URLs for each stream based on your API structure
geo_invoke_url = f"https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/{geo_stream_name}/record"
pin_invoke_url = f"https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/{pin_stream_name}/record"
user_invoke_url = f"https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/{user_stream_name}/record"

# Function to send data to the API
def send_data_to_api(data_payload, api_url):
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(data_payload)

    response = requests.post(api_url, headers=headers, data=payload)
    return response

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 1000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:
            # Fetch data from Pinterest tables and create dictionaries
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)

            # Initialize variables for data
            pin_result = None
            geo_result = None
            user_result = None

            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            for row in user_selected_row:
                user_result = dict(row._mapping)
            # Extract date_joined and format it, if it's a valid datetime object
            date_joined = user_result.get("date_joined")
            date_joined = date_joined.strftime("%Y-%m-%d %H:%M:%S")
            # Format the data as needed for Kinesis
            geo_payload = {
                "index": geo_result["ind"],
                "timestamp": geo_result["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                "latitude": geo_result["latitude"],
                "longitude": geo_result["longitude"],
                "country": geo_result["country"]
            }

            pin_payload = {
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
                # ... (Other fields from pin_result)
            }

            user_payload = {
                "index": user_result.get("ind"),
                "first_name": user_result.get("first_name"),
                "last_name": user_result.get("last_name"),
                "age": user_result.get("age"),
                "date_joined": user_result.get("date_joined")
                # ... (Other fields from user_result)
            }

            # Send data to Kinesis streams via the API
            geo_response = send_data_to_api(geo_payload, geo_invoke_url)
            pin_response = send_data_to_api(pin_payload, pin_invoke_url)
            user_response = send_data_to_api(user_payload, user_invoke_url)

            # Check the responses
            if geo_response.status_code == 200:
                print("Geo data sent successfully.")
            else:
                print(f"Failed to send Geo data. Status code: {geo_response.status_code}")

            if pin_response.status_code == 200:
                print("Pin data sent successfully.")
            else:
                print(f"Failed to send Pin data. Status code: {pin_response.status_code}")

            if user_response.status_code == 200:
                print("User data sent successfully.")
            else:
                print(f"Failed to send User data. Status code: {user_response.status_code}")

if __name__ == "__main__":
    run_infinite_post_data_loop()
