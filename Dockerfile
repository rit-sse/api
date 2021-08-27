FROM python:3.7-slim-buster AS requirements
WORKDIR /opt/api/

RUN pip install pipenv
ADD Pipfile Pipfile.lock /opt/api/
RUN pipenv install && pipenv run pip freeze > requirements.txt

FROM python:3.7-slim-buster
LABEL maintainer="RIT SSE <tech@sse.rit.edu>"

RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo 'America/New_York' > /etc/timezone
WORKDIR /opt/api/

COPY --from=requirements /opt/api/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . /opt/api/

ENTRYPOINT [ "gunicorn", "api:app" ]
CMD [ "--bind=0.0.0.0:8080", "--access-logfile=-" ]
