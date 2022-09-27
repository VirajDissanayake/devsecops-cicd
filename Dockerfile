FROM python:3.7
COPY rates/* ./app/
WORKDIR /app/
RUN pip install -r requirements.txt
EXPOSE 80
CMD gunicorn -b :80 wsgi
