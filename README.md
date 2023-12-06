# Projeto Streamlit com Autenticação e Testes Cypress

Este projeto demonstra um sistema de login básico usando Streamlit e inclui testes automatizados usando Cypress com a API Faker para gerar dados de login falsos.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git

## Instale as dependências do projeto:
````
cd seu-projeto
pip install -r requirements.txt
npm install
````

## Execução do Streamlit
Para iniciar o aplicativo Streamlit, execute o seguinte comando:
````
streamlit run app.py

````
**OBS**: acesse o front-end feito no streamlit em python - "https://localhost:8501"

## Execução dos Testes Cypress
1 - Abra um novo temrinal e navegue até o diretório do seu projeto
2 - Execute os testes Cypress em modo interativo:
````
npx cypress open
````

Ou, para executar em modo headless
````
npx cypress run
````
**OBS**: Certifique-se de que o aplicativo Streamlit está em execução antes de executar os teste Cypress

Configuração do Cypress
* O arquivo de configuração do cypress está localizado em `cypress/config.js`.
* Certifique-se de ajustar as configurações conforme necessário, incluindo opções de vídeo, caso deseje gravar as execuções dos testes.

## Notas Adicionais
* Este projeto utiliza a API Faker para gerar dados falsos de login.
* A pasta `cypress/integration` contém os testes Cypress.




