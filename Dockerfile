FROM python:3.9-alpine
WORKDIR /app

RUN apk --no-cache add curl
RUN apk --no-cache add zip

COPY tests ./tests
COPY utils ./utils
COPY requirements.txt ./
COPY pytest.ini ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pytest tests/ --alluredir=allure-results
RUN zip -r allure-results.zip allure-results