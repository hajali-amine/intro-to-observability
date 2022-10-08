FROM python

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./ /app/

EXPOSE 5000

ENV PYTHONPATH=$(PWD)

ENV FLASK_APP=app

RUN ls

CMD flask run --host=0.0.0.0
