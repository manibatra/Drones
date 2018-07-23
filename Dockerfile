FROM python:3.6.5

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

ADD . /code/

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 6379

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
