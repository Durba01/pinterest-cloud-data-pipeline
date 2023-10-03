import requests
import json

example_df = {"index": 1, "name": "Maya", "age": 25, "role": "engineer"}

# Replace 'stream-name' with the actual name of the stream you want to use
stream_name = "streaming-0a5afda0229f-geo"

# Construct the invoke URL based on your API structure
invoke_url = "https://uodinybje6.execute-api.us-east-1.amazonaws.com/dev/streams/{stream_name}/record"

# To send JSON messages, follow this structure
payload = json.dumps({
    "Data": {
        # Data should be sent as pairs of column_name:value, with different columns separated by commas
        "index": example_df["index"],
        "name": example_df["name"],
        "age": example_df["age"],
        "role": example_df["role"]
    },
    "PartitionKey": "desired-name"
})

headers = {'Content-Type': 'application/json'}

response = requests.request("PUT", invoke_url, headers=headers, data=payload)
print(response.status_code)