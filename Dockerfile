FROM python:3.9
WORKDIR /app

COPY pss-insight-data-sync.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV SOURCE_USERNAME=admin
ENV SOURCE_PASSWORD=district
ENV SOURCE_URL=https://pssnational.intellisoftkenya.com/api/events
ENV TARGET_USERNAME=admin
ENV TARGET_PASSWORD=district
ENV TARGET_URL=https://pssinternational.intellisoftkenya.com/api/events
ENV SOURCE_DATA_ELEMENTS_URL=https://pssnational.intellisoftkenya.com/api/dataElements

CMD ["python3", "pss-insight-data-sync.py"]

# docker build -t pssdatasync-image .

# docker run --name pssdatasync-container pssdatasync-image
