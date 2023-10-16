FROM python:3.10.12-slim

RUN pip install pipenv
RUN pip install numpy
RUN pip install scipy

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
COPY ["model2.bin", "dv.bin", "./"]

RUN pipenv install --system --deploy

COPY ["predict2.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict2:app" ]


