FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install --no-install-recommends postgresql-client

FROM python:3.9

RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app

# Create the home directory
ENV APP_HOME=/home/app/presentation
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# install
COPY . $APP_HOME
RUN pip install .[dev]
RUN pip install -e .

RUN chown -R app:app $APP_HOME
USER app

EXPOSE 8080
CMD python3 -m uvicorn api.app:app --reload --host 0.0.0.0 --port 8080
