# pull official base image
FROM python:3.8.6-buster
RUN mkdir /app
WORKDIR /app
ADD . /app/


RUN pip install pipenv
RUN python -m pip install django-debug-toolbar
RUN pip install Pillow
COPY Pipfile* /app/
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary


COPY . .

CMD ["python", "manage.py", "runserver"]