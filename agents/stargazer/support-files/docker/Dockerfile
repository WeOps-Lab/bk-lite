FROM python:3.10

RUN apt-get update && \
    apt-get install -y vim  unzip curl pkg-config libssl-dev  supervisor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD . .

ADD support-files/supervisor/service.conf /etc/supervisor/conf.d/service.conf

RUN pip install -r ./requirements/requirements-core.txt 
RUN pip install -r ./requirements/requirements-extra.txt 

CMD ["supervisord", "-n"]