# Startup Funding Analytics

Dashboard interativo desenvolvido para análise de investimentos, valuation e distribuição de startups a partir de dados de funding.

## Equipe

**Grupo 9**

- Andre Oliveira
- Caliel Farias
- Guilherme Vilarim

## Objetivo

O projeto tem como objetivo analisar dados de financiamento de startups, permitindo explorar padrões de investimento, distribuição geográfica, setores de atuação, valuation e evolução temporal.

O dashboard foi desenvolvido com foco em análise exploratória e visualização interativa dos dados, permitindo que o usuário aplique filtros e observe os impactos diretamente nos indicadores e gráficos.

## Dataset

O projeto utiliza o dataset **Startup Funding Analytics**, disponibilizado em formato CSV.

O conjunto de dados contém informações relacionadas a startups, incluindo:

- Indústria
- País
- Ano
- Valor de investimento
- Investimento total
- Valuation
- Indicador de unicórnio

Arquivo utilizado:

    data/Startup_Funding_Analytics_150k.csv

## Funcionalidades

O dashboard permite:

- Filtrar os dados por país
- Filtrar por indústria
- Selecionar um período de análise
- Alterar a métrica utilizada no ranking
- Visualizar o total de startups no recorte selecionado
- Visualizar o total de investimento
- Analisar o valuation médio
- Identificar a participação de startups unicórnio
- Visualizar a distribuição geográfica dos investimentos
- Comparar investimentos entre indústrias
- Analisar a evolução temporal das indústrias
- Visualizar a distribuição de valuation por setor

Todos os indicadores e gráficos são atualizados de acordo com os filtros selecionados.

## Tecnologias

O projeto foi desenvolvido utilizando:

- Python
- Streamlit
- Pandas
- Plotly

## Estrutura do projeto

    Startup-Funding-Analytics/
    │
    ├── .streamlit/
    │
    ├── assets/
    │   └── Logo.png
    │
    ├── data/
    │   └── Startup_Funding_Analytics_150k.csv
    │
    ├── src/
    │   ├── data.py
    │   ├── filters.py
    │   ├── metrics.py
    │   └── charts.py
    │
    ├── st-venv/
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

## Organização do código

A aplicação foi organizada de forma modular para separar responsabilidades:

**`app.py`**

Responsável pela execução principal da aplicação, composição da interface, identidade visual, CSS e integração entre os módulos.

**`src/data.py`**

Responsável pelo carregamento, seleção e preparação dos dados.

**`src/filters.py`**

Responsável pela criação dos filtros da barra lateral e aplicação dos filtros ao dataset.

**`src/metrics.py`**

Responsável pelo cálculo dos indicadores apresentados nos cards do dashboard.

**`src/charts.py`**

Responsável pela criação dos gráficos utilizados no dashboard.

## Como executar

### 1. Criar o ambiente virtual

No terminal, dentro da pasta do projeto:

    python -m venv st-venv

### 2. Ativar o ambiente virtual

No Windows:

    st-venv\Scripts\activate

### 3. Instalar as dependências

    pip install -r requirements.txt

### 4. Executar o dashboard

    streamlit run app.py

Após a execução, o Streamlit disponibilizará o endereço local para acessar o dashboard pelo navegador.

## Observações técnicas

O carregamento dos dados utiliza cache do Streamlit para evitar leituras desnecessárias do arquivo CSV durante as interações com o dashboard.

Os filtros são aplicados antes do cálculo dos indicadores e da geração dos gráficos, garantindo que as visualizações representem o mesmo recorte selecionado pelo usuário.

O projeto utiliza uma organização modular para facilitar a manutenção, reutilização e evolução da aplicação.

## Fonte dos dados

**Dataset:** Startup Funding Analytics

**Fonte:** Kaggle
