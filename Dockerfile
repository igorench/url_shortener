FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /url_shortener_engine
WORKDIR /url_shortener_engine
COPY requirements.txt /url_shortener_engine/
RUN pip install -r requirements.txt
COPY . /url_shortener_engine/