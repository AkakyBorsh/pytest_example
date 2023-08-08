FROM python:3.9-alpine
WORKDIR /app

COPY requirements.txt ./
RUN apk --no-cache add curl  \
    && apk --no-cache add zip \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY pytest.ini ./
COPY utils ./utils
COPY send_results.py ./
COPY tests ./tests
ENTRYPOINT ["/bin/sh", "-c" , "pytest tests/ --alluredir=allure-results; python send_results.py;tail -f /dev/null"]

