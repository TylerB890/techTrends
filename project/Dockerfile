FROM python:3.9

LABEL maintainer="Tab890"

COPY . /app

WORKDIR /app/techtrends

EXPOSE 3111

RUN pip install -r requirements.txt
RUN python init_db.py

CMD ["python", "app.py"]

