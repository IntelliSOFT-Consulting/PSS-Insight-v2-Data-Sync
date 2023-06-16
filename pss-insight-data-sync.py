import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Variables
source_username = os.getenv("SOURCE_USERNAME")
source_password = os.getenv("SOURCE_PASSWORD")
target_username = os.getenv("TARGET_USERNAME")
target_password = os.getenv("TARGET_PASSWORD")
source_url = os.getenv("SOURCE_URL")
target_url = os.getenv("TARGET_URL")
data_elements_url = os.getenv("SOURCE_DATA_ELEMENTS_URL")

# Check if any of the environment variables are missing
if not (source_username and source_password and source_url and target_url):
    raise ValueError("Please set the SOURCE_USERNAME, SOURCE_PASSWORD, SOURCE_URL, and TARGET_URL environment variables.")

# Fetch data elements from source DHIS2 instance
response = requests.get(data_elements_url, auth=(source_username, source_password))
data_elements = response.json()["dataElements"]

# Extract data element IDs
data_element_ids = [data_element["id"] for data_element in data_elements]

# Fetch data from source DHIS2 instance
response = requests.get(source_url, auth=(source_username, source_password), params={"paging": "false"})
data = response.json()

# Preprocess data to include specific data element values
processed_data = []
for event in data["events"]:
    new_event = {
        "program": event["program"],
        "event": event["event"],
        "orgUnit": event["orgUnit"],
        "eventDate": event["eventDate"],
        "dataValues": []
    }
    for data_value in event["dataValues"]:
        if data_value["dataElement"] in data_element_ids:
            new_event["dataValues"].append(data_value)
    processed_data.append(new_event)

print('processed_data', processed_data)

# Push processed data to target DHIS2 instance
for event in processed_data:
    response = requests.post(target_url, auth=(target_username, target_password), json=event)
    if response.status_code == 200:
        print("Event successfully pushed:", event["event"])
    else:
        print("Failed to push event:", event["event"])