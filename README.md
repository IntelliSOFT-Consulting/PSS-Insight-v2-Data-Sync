# PSS-Insight-v2-Data-Sync
PSS DHIS2 data sync script between the national PSS instance and the international instance.

# set Environment Variables

export TARGET_USERNAME="your_username"

export SOURCE_USERNAME="your_username"

export SOURCE_PASSWORD="your_password"

export TARGET_PASSWORD="your_password"

export SOURCE_URL="https://source-dhis2-instance/api/events"

export TARGET_URL="https://target-dhis2-instance/api/events"

# Build a docker image and push to docker hub

docker build -t mtaps2023/pss_data_sync:latest -f Dockerfile .  
 
docker login 

`< Enter Username and Password >``

docker push  mtaps2023/pss_data_sync:latest