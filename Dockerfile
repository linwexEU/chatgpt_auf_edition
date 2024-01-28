FROM python:3.11.7 

RUN mkdir /chatgpt 

WORKDIR /chatgpt 

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

RUN chmod a+x /chatgpt/docker/*.sh

CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]













