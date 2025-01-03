# OBTER TODAS AS DETECÇÕES DE 200 EM 200
import requests
import json
import glob
import os

class detections_import:
    def __init__(self):
        def delete_detection_files(directory):
            # Procurar por todos os arquivos que começam com "detection_ids_part" na pasta especificada
            files_to_delete = glob.glob(os.path.join(directory, "detection_ids_part*"))

            # Excluir cada arquivo encontrado
            for file_path in files_to_delete:
                try:
                    os.remove(file_path)
                    print(f"Arquivo excluído: {file_path}")
                except Exception as e:
                    print(f"Erro ao excluir o arquivo {file_path}: {e}")


        directory = "app_dev/data"  # Substitua pelo caminho da sua pasta
        delete_detection_files(directory)

        def get_token(client_id, client_secret):
            oauth2_url = "https://api.us-2.crowdstrike.com/oauth2/token"
            body = {
                "client_id": client_id,
                "client_secret": client_secret
            }
            headers = {
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            response = requests.post(oauth2_url, data=body, headers=headers)
            response_data = response.json()
            return response_data['access_token']

        def get_data(token):
            api_url = "https://api.us-2.crowdstrike.com/alerts/queries/alerts/v1?filter=(created_timestamp%3A%3E%3D%27now-30d%27%2Bcreated_timestamp%3A%3C%27now%27)%2Bproduct%3A%5B%27epp%27%5D&limit=10000&offset=0&sort=timestamp|desc"
            headers = {
                "Authorization": f"Bearer {token}",
                "accept": "application/json"
            }
            response = requests.get(api_url, headers=headers)
            return response.json()

        def save_batches_to_json(resources):
            for i in range(0, len(resources), 200):
                batch = resources[i:i+200]
                batch_filename = f'app_dev/data/detection_ids_part-{i//200 + 1}.json'
                with open(batch_filename, 'w') as json_file:
                    json.dump(batch, json_file, indent=4)
                print(f"Parte {i//200 + 1} salvo em {batch_filename}")

        client_id = ""
        client_secret = ""
        token = get_token(client_id, client_secret)
        data = get_data(token)
        resources = data['resources']

        with open('app_dev/data/detection_ids-all.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("Dados salvos em 'app_dev/data/detection_ids-all.json'")
        save_batches_to_json(resources)

