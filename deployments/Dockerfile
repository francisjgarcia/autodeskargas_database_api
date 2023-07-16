FROM python:3.10.8-bullseye

LABEL maintainer Francis J. Garcia <contacto@francisjgarcia.es>
LABEL org.opencontainers.image.source="https://github.com/francisjgarcia/autodeskargas_database_api"
LABEL org.opencontainers.image.description "Administra los accesos a base de datos del proyecto AutoDesKargaS"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN useradd -m python && usermod -aG python python

USER python:python

WORKDIR /usr/src/app

COPY --chown=python:python app .
COPY --chown=python:python deployments/entrypoint.sh /
COPY --chown=python:python deployments/start.sh /

RUN chmod +x /entrypoint.sh && \
    chmod +x /start.sh

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]

CMD [ "/start.sh", "server" ]