# 🌤️ Weather Data Pipeline

Pipeline ETL automatizado para coleta, transformação e carregamento de dados meteorológicos utilizando **Apache Airflow** e Python.

---

## 📌 Sobre o Projeto

Este projeto implementa um pipeline completo de Engenharia de Dados, composto por:

- **Extract**: coleta dados de clima da API OpenWeather
- **Transform**: normaliza e transforma os dados
- **Load**: grava os dados transformados em destino estruturado (arquivo Parquet e/ou banco de dados)

O pipeline é orquestrado pelo **Apache Airflow** com tasks sequenciais e modularizadas.

---

## 🧠 O que este projeto resolve

- Organiza um fluxo de dados meteorológicos repetitivo e escalável
- Utiliza boas práticas de modularização de código (`src/`)
- Separa lógica de ETL em tarefas distintas
- Evita o uso de DataFrames em XCom (padrão Airflow)
- Produz artefatos intermediários (Parquet) reutilizáveis

---

## 🗂️ Estrutura do Repositório

```text
weather-data-pipeline/
├── dags/                     # Definição das DAGs do Airflow
│   └── weather_dag.py
├── src/                      # Módulos reutilizáveis (Extract / Transform / Load)
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
├── data/                     # Armazenamento de dados brutos e transformados
├── notebooks/                # Notebooks auxiliares (análises exploratórias etc.)
├── .gitignore
├── docker-compose.yaml       # (Opcional) Configuração Docker
├── pyproject.toml
└── README.md