ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION} as requirements-dev

WORKDIR /app
 
FROM python:${PYTHON_VERSION} as base


# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--debug", "--host=0.0.0.0", "--port", "5000"]
