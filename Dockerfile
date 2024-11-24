FROM python:3.9-alpine3.13
LABEL maintaner="linkedin.com/in/caiolouro"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app

# Informs Docker that the container will listen on a port (doesn't actually publish the port)
EXPOSE 8000

# Runs several commands without creating a new image layer ("&& \"" suffix)
# Note the " \" suffix is to split one command into multiple lines
# Also pip self upgrades and creates non-root user for security reasons
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        my-django-user

ENV PATH="/py/bin:$PATH"

USER my-django-user