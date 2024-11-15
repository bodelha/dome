#!/bin/bash

# Verifica se o ambiente é "development"
if [ "$ENV" != "development" ]; then
    echo "Ambiente não é de desenvolvimento. Carga de dados não será realizada."
    exit 0
fi

# Endpoint da API (ajuste conforme necessário)
API_URL="$API_URL"  # A URL da API dentro do Docker Compose

# Exibe o endpoint para verificação
echo "Usando o endpoint da API: $API_URL"

echo "Aguardando a API estar pronta..."
wait-for-it api:5000 --timeout=60 --strict -- echo "API pronta para conexões!"

# Testa a conexão com a API
echo "Testando a API com curl..."
curl -v "$API_URL/" || { echo "Falha ao conectar com a API"; exit 1; }

# Gera os dados com o Python
echo "Gerando dados..."
python generate.py  # Isso vai gerar o arquivo de dados mockados

# Verifica se o arquivo JSON foi gerado
DATA_FILE="dados_mockados_estufa_franca.json"
if [[ ! -f "$DATA_FILE" ]]; then
    echo "Arquivo de dados não encontrado após a execução do script Python!"
    exit 1
fi

# Lê o arquivo JSON e faz o POST para a API
cat "$DATA_FILE" | jq -c '.[]' | while read json_data; do
    # Faz o POST para a API
    response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$API_URL/v1/measurements" -H "Content-Type: application/json" -d "$json_data")

    # Verifica se a requisição foi bem-sucedida
    if [[ "$response" -ne 201 ]]; then
        echo "Falha ao enviar dados. Código HTTP: $response"
    else
        echo "Dados enviados com sucesso"
    fi
done
