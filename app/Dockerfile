FROM python:3.10-slim
WORKDIR /usr/src/app

# not write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# intall packages
RUN pip install -U pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]