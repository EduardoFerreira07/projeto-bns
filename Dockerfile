FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install 'setuptools==58.0.0'
RUN pip install -r requirements.txt
ENV REDIS_PORT_6379_TCP_ADDR=redis