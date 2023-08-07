FROM python:3.9-alpine
WORKDIR /app

RUN apk --no-cache add curl
RUN apk --no-cache add zip

COPY tests ./tests
COPY utils ./utils
COPY requirements.txt ./
COPY send_results.py ./
COPY pytest.ini ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/sh", "-c" , "pytest tests/ --alluredir=allure-results; python send_results.py;tail -f /dev/null"]