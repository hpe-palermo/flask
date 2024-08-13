FROM python:3.8

WORKDIR /app

RUN	/bin/sh -c pip3 install -r requirements.txt 

EXPOSE 2000

CMD ["flask", "run", "--host=0.0.0.0"]
