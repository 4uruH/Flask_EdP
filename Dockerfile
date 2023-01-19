FROM python:3.8.10-buster

WORKDIR /app

COPY Pipfile.lock Pipfile.lock

COPY Pipfile Pipfile

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]