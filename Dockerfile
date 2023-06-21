FROM python:3.9

# Install cron
RUN apt-get update && apt-get -y install cron

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


COPY crontab /etc/cron.d/my-cron

RUN chmod 0644 /etc/cron.d/my-cron
RUN crontab /etc/cron.d/my-cron

CMD ["cron", "-f"]

# CMD ["python3", "pss-insight-data-sync.py"]

# docker build -t pssdatasync-image .

# docker run --name pssdatasync-container pssdatasync-image
