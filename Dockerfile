FROM python:2-alpine
EXPOSE 5000
COPY app microservice
WORKDIR /microservice
RUN pip install -r requirements.txt
CMD python server.py
