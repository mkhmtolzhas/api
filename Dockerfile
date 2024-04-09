FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

RUN pip install -r requirements.txt


COPY requirements.txt .


COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000



