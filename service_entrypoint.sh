#!/bin/bash

# Esperar pelo banco de dados
echo "Aguardando o banco de dados ficar disponível..."
for i in {1..10}; do
    if pg_isready -h db -p 5432 -U "${POSTGRES_USER}"; then
        echo "Banco de dados está pronto!"
        break
    fi
    echo "Tentando conectar ao banco de dados ($i/10)..."
    sleep 2
done

if [ $i -eq 10 ]; then
    echo "Erro: Não foi possível conectar ao banco de dados. Saindo."
    exit 1
fi

# Aplicar migrações do banco de dados
echo "Aplicando migrações do banco de dados..."
flask db migrate || { echo "Erro ao executar 'flask db migrate'."; exit 1; }
flask db upgrade || { echo "Erro ao executar 'flask db upgrade'."; exit 1; }

# Iniciar o servidor
echo "Iniciando o servidor..."
exec waitress-serve --host=0.0.0.0 --port=5000 --call 'app:create_app'
