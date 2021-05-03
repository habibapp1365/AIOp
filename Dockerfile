FROM habibapp1365/alpine-django:latest

#RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -V
RUN pip freeze
EXPOSE 8000
RUN python3 manage.py runserver
