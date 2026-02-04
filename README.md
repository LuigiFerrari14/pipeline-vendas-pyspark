# Pipeline de Vendas com PySpark no Databricks

Projeto simples de Engenharia de Dados utilizando PySpark no Databricks, com foco na construção de um pipeline de dados do zero.

## Objetivo
Construir um pipeline que realiza ingestão, limpeza, transformação e agregação de dados de vendas, gerando uma tabela analítica final.

## Tecnologias Utilizadas
- Python
- PySpark
- Databricks
- Parquet / Delta Lake

## Etapas do Pipeline
1. Ingestão de dados a partir de arquivo CSV
2. Limpeza e tratamento de dados
3. Transformações e criação de métricas
4. Agregação dos dados (camada Gold)

pipeline-vendas-pyspark/
├── pipeline_vendas
├── README
└── data/
└── vendas.csv

## Resultado Final
Tabela agregada com total de vendas por categoria.
