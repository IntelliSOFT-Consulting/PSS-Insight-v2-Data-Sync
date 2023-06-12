import requests
import os

# Variables
username = os.getenv("DHIS2_USERNAME")
password = os.getenv("DHIS2_PASSWORD")
source_url = os.getenv("SOURCE_URL")
target_url = os.getenv("TARGET_URL")

# Check if any of the environment variables are missing
if not (username and password and source_url and target_url):
    raise ValueError("Please set the DHIS2_USERNAME, DHIS2_PASSWORD, SOURCE_URL, and TARGET_URL environment variables.")

data_elements = ["Fz75Jo6v99X", "DAvT1ODxYKK", "HLBBj5vnCC3"]  # Specify the data elements to be included

# Fetch data from source DHIS2 instance
response = requests.get(source_url, auth=(username, password), params={"paging": "false"})
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
        if data_value["dataElement"] in data_elements:
            new_event["dataValues"].append(data_value)
    processed_data.append(new_event)

print('processed_data',processed_data)

# Push processed data to target DHIS2 instance
for event in processed_data:
    response = requests.post(target_url, auth=(username, password), json=event)
    if response.status_code == 200:
        print("Event successfully pushed:", event["event"])
    else:
        print("Failed to push event:", event["event"])