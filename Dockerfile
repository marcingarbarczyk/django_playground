# syntax=docker/dockerfile:1
FROM python:3.10

RUN useradd -d /home/app -m -s /bin/bash app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/app/django
COPY entrypoint.sh /home/app
COPY . /home/app/django/
RUN pip install -r requirements.txt

# Node install
ENV NVM_DIR /home/app/nvm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
ENV NODE_VERSION v16.5.0
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"

ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH

#
RUN chown -R app:app /home/app
RUN chmod 700 /home/app/entrypoint.sh
USER app