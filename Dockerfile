FROM python:3

ADD test.py /

COPY ./requirements.txt /app/requirements.txt


WORKDIR /app

RUN pip install -r requirements.txt 

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "test.py" ]


