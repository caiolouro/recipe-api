FROM python:3.9-alpine3.13
LABEL maintainer="caiolouro"

ENV PYTHONUNBUFFERED=1

# COPY copies from local machine to Docker image
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# Default value is false, should be overridden by docker-compose.yml
ARG DEV=false
# Uses a "long" RUN command (that's the "&& \" suffix plus identation for) to avoid creating a new layer for each command
# Note also the if syntax for shell commands, starting with "if" and ending with "fi"
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"

USER django-user