FROM python:latest

COPY ./ app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python","app.py"]

#ENTRYPOINT["python"]

#CMD["app.py"]