FROM habibapp1365/alpine-django:latest

WORKDIR /app

COPY requirements.txt ./
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
