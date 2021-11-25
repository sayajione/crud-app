FROM python:3.9.7 as python_base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /code

COPY *.toml *.lock /code/

ENV PATH="${PATH}:/root/.poetry/bin"

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

  
COPY ./src /code/src





