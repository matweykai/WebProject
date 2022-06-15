FROM python:3.9
ENV PYTHONUNBUFFERED = 1
WORKDIR website
COPY requirements.txt /website/
RUN pip install -r requirements.txt
COPY . /website/