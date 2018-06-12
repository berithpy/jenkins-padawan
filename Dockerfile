FROM python:3-alpine
EXPOSE 5000
COPY app microservice
WORKDIR /microservice
RUN pip install pipenv
RUN SHELL=/bin/ash
RUN pipenv install 
CMD pipenv run python app.py
