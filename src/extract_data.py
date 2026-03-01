import requests
import json
from pathlib import Path 


import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_weather_data(url:str) -> list :
    response = requests.get(url)
    data =  response.json()

    if response != 200:
        logging.error("Erro na requisição")
        return []

    if not data :
        logging.warn("Nenhum dado retornado")
        return []

    output_path = 'data/weather_data.json'
    output.dir = PATH(output_path).parent
    output.dir.mkdir(parents=True, exist_ok= True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Arquivo salvo em {output_path}")
    return data
