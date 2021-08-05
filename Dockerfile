FROM python:3.7-slim-buster
LABEL maintainer="RIT SSE <tech@sse.rit.edu>"

RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo 'America/New_York' > /etc/timezone

RUN pip install pipenv

WORKDIR /opt/api/

ADD Pipfile Pipfile.lock /opt/api/

RUN pipenv install

ADD . /opt/api/

ENTRYPOINT [ "pipenv", "run", "gunicorn", "api:app" ]
CMD [ "--bind=0.0.0.0:8080", "--access-logfile=-" ]
