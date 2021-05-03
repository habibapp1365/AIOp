FROM habibapp1365/alpine-django

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN python -V
RUN pip freeze
EXPOSE 8000
RUN python manage.py runserver
