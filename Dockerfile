FROM python:3.12.3

# Atualizar pacotes e instalar dependências necessárias
RUN apt-get -q update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV USERNAME=admin_damiani
ENV WORKING_DIR=/home/damiani/Defense1

WORKDIR ${WORKING_DIR}

COPY app app
COPY requirements.txt .
COPY service_entrypoint.sh .

RUN groupadd ${USERNAME} && \
    useradd -g ${USERNAME} ${USERNAME}

RUN chown -R ${USERNAME}:${USERNAME} ${WORKING_DIR}
RUN chmod -R u=rwx,g=rwx ${WORKING_DIR}

# Atualizar pip e instalar dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Configurações adicionais
ENV FLASK_APP=app
RUN chmod +x service_entrypoint.sh

EXPOSE 5000
RUN flask db init

ENTRYPOINT ["./service_entrypoint.sh"]