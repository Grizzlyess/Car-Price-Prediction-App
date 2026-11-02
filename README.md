# Car Price Prediction App

###  Disponível em: 
```bash
https://car-price-prediction-app-3iww.onrender.com/
```

Este projeto é uma aplicação web completa desenvolvida para prever o preço de venda de carros usados com base em caraterísticas do veículo (como ano, quilometragem, tipo de combustível, transmissão e historial de proprietários).

O foco deste repositório é demonstrar o ciclo completo de desenvolvimento em Inteligência Artificial, abrangendo a engenharia de atributos, treino de modelos de regressão avançados com **Random Forest**, construção de uma interface web em **Django** e integração com serviços de alojamento em nuvem.

## Tecnologias Utilizadas

*   **Machine Learning:** Python, Scikit-Learn (Random Forest Regressor), Pandas, NumPy
*   **Framework Web:** Django, HTML5, CSS3
*   **Deploy & Infraestrutura:** Git, GitHub, Heroku

## Arquitetura do Projeto

O sistema está dividido em três fases principais:
1.  **Modelação Preditiva:** Limpeza de dados, engenharia de atributos (*feature engineering*) e treino de um modelo de regressão baseado em árvores de decisão.
2.  **Aplicação Web (Django):** Um sistema web integrado que carrega o modelo treinado para a memória, processa os inputs introduzidos pelo utilizador e devolve a estimativa de preço em tempo real.
3.  **Implementação (Deployment):** Configuração de dependências, variáveis de ambiente e ficheiros de configuração para publicação em nuvem via GitHub e Heroku.


## Como Executar o Projeto Localmente

Siga os passos abaixo para clonar e executar a aplicação na sua máquina:

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-utilizador/car-price-prediction.git
cd car-price-prediction
```

### 2. Configurar o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Executar as migrações da base de dados
```bash
python manage.py migrate
```

### 5. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Aceda à aplicação no seu navegador através de: **http://127.0.0.1:8000/**

## Metodologia de Machine Learning

*   **Algoritmia:** Utilizou-se o `RandomForestRegressor`, um modelo de ensemble altamente eficaz para lidar com relações não-lineares entre as variáveis dos veículos e o preço de mercado.
*   **Extração de Atributos:** Focou-se numa fase robusta de transformação de dados e engenharia de atributos em vez de análises exploratórias complexas, otimizando o poder preditivo do regressor.

## Próximos Passos (Roadmap)
*   [ ] Conteinerizar a aplicação utilizando Docker para garantir portabilidade.
*   [ ] Substituir o modelo atual por pipelines automatizados com otimização de hiperparâmetros.
