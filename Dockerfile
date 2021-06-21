FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Aiden-Kwak/oconnect2021_ver4.git

WORKDIR /home/oconnect2021_ver4/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-pibvgb5)3(ja*!2m4(2j$ak(hx^osv!_z5kns$c_^e+kmc9n#^" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "oconnect.wsgi", "--bind", "0.0.0.0:8000"]