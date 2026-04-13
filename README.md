# **Google Play Store Dataset**

O objetivo é analisar dados da Play Store da Google, para identificar as características dos aplicativos associadas ao seu desempenho na plataforma, gerando insights que possam contribuir para a melhoria da experiência do usuário.

## **Dataset**

```
Fonte: Kaggle
Nome: Google Play Store Apps
link: https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps

Arquivo utilizado: 'Google-Playstore.csv'
Registros: 2312944 linhas e 24 colunas
Acessado em: Fevereiro/2026
```

## **Principais colunas**

```
Category: Categoria do aplicativo.  
Rating: Valor médio das avaliações recebidas pelo aplicativo.  
Rating Count: Total de avaliações recebidas pelo aplicativo.  
Minimum Installs: Número mínimo total de instalações.  
Price: Preço do aplicativo.  
Size: Tamanho do aplicativo.  
Minimum Android: Versão mínima do sistema Android.  
Ad Supported: Indicador de suporte a propagandas dentro do aplicativo.  
In App Purchases: Indicador de compras dentro do aplicativo.  
Editors Choice: Aplicativos indicados pelos editores.   
```

## **Tecnologias**

* matplotlib
* numpy
* pandas 
* seaborn
* streamlit

## **Estrutura do projeto**

```
play_store_dataset
├── README.md
├── app
│   └── google_play_streamlit_app.py
├── notebooks
│   └── google_play_store_apps.ipynb
├── requirements.txt
└── src
    ├── __init__.py
    ├── dados
    │   ├── processed
    │   │   └── play_store_app_processed.csv
    │   └── raw
    │       ├── play_store_app_raw.csv
    │       └── play_store_app_raw_sample.csv
    └── google_play_cleaner.py
```

## **Como executar**

1. Clone o repositório:
```bash
git clone https://github.com/rafaelhsnts/play_store_dataset.git
cd play_store_dataset
```
2. Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Abra o notebook no Jupyter ou Colab:
```bash
pip install jupyterlab
jupyter lab notebooks/google_play_store_apps.ipynb
```