# alpine is the lightweight version of the Linux image
FROM python:3.9-alpine3.13
LABEL maintaner="linkedin.com/in/caiolouro"

# Prevents Python from buffering stdout and stderr, making feedback from the container more immediate
ENV PYTHONUNBUFFERED=1

# Copy files from local directory to the container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app

# Informs Docker that the container will listen on a port (doesn't actually publish the port!)
EXPOSE 8000

# Let it be overridden at build time by Docker Compose
ARG DEV=false

# Runs several commands without creating a new image layer ("&& \"" suffix)
# Note the " \" suffix is to split one command into multiple lines
# Also pip self upgrades and creates non-root user for security reasons
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = true ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        my-django-user

# Adds virtual env binaries to the PATH
ENV PATH="/py/bin:$PATH"

USER my-django-user