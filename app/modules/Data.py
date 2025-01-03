from flask import Blueprint, current_app, render_template
import requests
import json

# criação do blueprint
blueprint = Blueprint('dspm', __name__, url_prefix = '/dspm')

# Payload usado para capturar os dados
payload = json.dumps({
  "source": "violation",
  "queries": [
    {
      "skip_read_cache": True,
      "skip_cache": True,
      "response_config": {
        "format": 1,
        "int_64_to_str": False,
        "float_64_to_str": False
      },
      "fields": [
        {
          "name": "id",
          "type": "aggregate",
          "options": {
            "function": "count_distinct",
            "alias": "Qtd"
          }
        }
      ],
      "distinct": True,
      "group_by": [
        {
          "field": "service_type"
        },
        {
          "field": "severity"
        },
        {
          "field": "status"
        }
      ]
    },
    {
      "skip_read_cache": True,
      "skip_cache": True,
      "response_config": {
        "format": 1,
        "int_64_to_str": False,
        "float_64_to_str": False
      },
      "fields": [
        {
          "name": "id",
          "type": "aggregate",
          "options": {
            "function": "count_distinct",
            "alias": "Qtd"
          }
        }
      ],
      "distinct": True,
      "group_by": [
        {
          "field": "service_type"
        },
        {
          "field": "asset_name_keyword"
        },
        {
          "field": "severity"
        },
        {
          "field": "status"
        }
      ]
    },
    {
      "skip_read_cache": True,
      "skip_cache": True,
      "response_config": {
        "format": 1,
        "int_64_to_str": False,
        "float_64_to_str": False
      },
      "fields": [
        {
          "name": "id",
          "type": "aggregate",
          "options": {
            "function": "count_distinct",
            "alias": "Qtd"
          }
        }
      ],
      "distinct": True,
      "group_by": [
        {
          "field": "object_id"
        },
        {
          "field": "object_name_keyword"
        }
      ]
    }
  ],
  "filter": {
    "op": "and",
    "value": [
      {
        "op": "eq",
        "value": "violation",
        "field": "meta_type"
      }
    ]
  }
})

# Função para buscar os dados da API
def get_api_data():
    api_url = current_app.config.get('API_URL')
    
    # Cabeçalhos para a requisição
    headers = {
        'X-API-KEY': current_app.config.get('API_KEY'),
        'X-API-SECRET': current_app.config.get('API_SECRET'),
        'X-TIDENT': current_app.config.get('API_TIDENT'),
        'Content-Type': current_app.config.get('API_CONTENT_TYPE'),
        'Cookie': current_app.config.get('API_COOKIE'),
    }

    try:
        # print(payload)
        # print(api_url)

        # Fazendo requisição
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status() # Levanta uma exceção para status de erro

        # Logar toda a resposta em JSON
        response_data = response.json()
        current_app.logger.info(f"Resposta completa da API: {json.dumps(response_data, indent=2)}")

        if 'data' in response_data and isinstance(response_data['data'], list):
            return {'responses': response_data['data']}  # Retorne em formato de lista
        else:
            return {"error": "Resposta da API não contém 'data' corretamente."}
        
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Erro ao acessar a api {e}')

        return {"error" : "Erro ao acessar a API"}

@blueprint.route('/data',methods=["GET" , "POST"])
def get_data():

    # Busca os dados da API do securiti
    data = get_api_data()

    # Log para verificar a restutura de 'data'
    current_app.logger.info(f'Data from API:{data}')

    # Renderia os dados em uma pagina HTMl
    return render_template('index.html', data=data)