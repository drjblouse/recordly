FROM python:3.5.1

MAINTAINER Jared Blouse
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/recordly
WORKDIR /opt/recordly
ADD . /opt/recordly/

RUN apt-get update; apt-get -y install vim
RUN pip install -r /opt/recordly/requirements.pip

ENTRYPOINT ["python","manage.py"]
CMD ["runserver","0.0.0.0:8000"]
