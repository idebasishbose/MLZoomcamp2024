FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["q6.py","q6-server-test.py","./"]

EXPOSE 9670

ENTRYPOINT [ "gunicorn","--bind=0.0.0.0:9670", "q6:app" ]