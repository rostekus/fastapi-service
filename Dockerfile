FROM python:3.11

RUN addgroup --system myappgroup && adduser --system --group myappuser

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

USER myappuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
