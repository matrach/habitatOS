FROM python:3.6.2
RUN mkdir /code
ADD requirements.txt /code
RUN pip install -r /code/requirements.txt
ADD . /code
WORKDIR /code
VOLUME /code

ENTRYPOINT bash -c "python manage.py migrate --noinput && python manage.py loaddata && python manage.py runserver 0.0.0.0:8000"