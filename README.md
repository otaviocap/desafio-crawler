# Scrapper (desafio)

## Proposta
Criar um scrapper em Python, capaz de coletar dados de um dos seguintes sites: 
- [quotes.toscrape](https://quotes.toscrape.com/)
- [imdb.com](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

Para este projeto o escolhido foi o imdb.

## Utilizando
O projeto pode ser utilizado de duas maneiras:

### Dependências
Antes de instalar o projeto certifiquê-se que os seguintes programas estão instalados:
* Python 3 
* virtualenv
* Docker (caso quiser rodar ele em um container)

### Local
Da maneira local a execução pode ser realizada da seguinte maneira.

1. Suba seu ambiente virtual
```commandline
virtualenv .venv
```

2. Instale as depêndencias do projeto
```commandline
pip install -r requirements.txt
```

3. Inicie a aplicação
```commandline
./run.sh
```

**Obs.:** Para subir localmente é **necessário** que esteje rodando na máquina o **Selenium Hub**, um **Nodo
Chrome** e o banco de dados **Postgres**. Por isso é mais fácil subir seguindo a próxima opção.

### Docker
Para subir com o Docker é muito simples, apenas utilize o docker compose que já está pronto nesse repositório

```commandline
docker compose up
```

# Objetivos do projeto

## Minimo Entregável:

- Buscar dados de forma automatizada(script de linha de comando ou interface clicavel)
  - Ao executar o programa ele ira se conectar no Selenium Hub e assim que tiver um nodo disponível ele
  ira começar a fazer o scrapping do imdb.
  

- Padronizar os retornos de forma estruturada (json/csv)
  - Ao finalizar o processo de scrapping ele ira criar na pasta `./logs/data` dois arquivos, um csv e outro json
  com o retorno dos dados do imdb


- Sistema de logs de para acompanhamento da execução
  - O sistema de logs é centralizado, ele durante a execução ira criar arquivos de log na pasta `./logs/text` e
  também colocar no _stdout_
  

- Ter um prova da consulta (Screenshot)
  - Ao finalizar o processo de scrapping o programa ira colocar uma screenshot na pasta de log `./logs/images` com
  o conteúdo da parte superior do site imdb

## Pontos Extra para:

- Armazenamento dos resultados em um banco relacional ou não relacional
  - Todos os dados que forem coletados são armazenados em uma instância do Postgres
  

- fazer um dataframe que possibilite visualizar os resultados via pandas
  - Ao finalizar o processo de scrapping o programa transforma a lista de filmes retornados em um _dataframe_
  do Pandas e utiliza dele para gerar os arquivos json e csv


- Trazer resultados de forma dinamica sem fixar caminhos no `xpath`
  - A coleta de dados usa um Css Selector para assim caso o site mudar a posição dos elementos ele 
  ainda conseguir trazer os dados


- Dockerizar a aplicação
  - Como citado anteriormente o docker é uma das alternativas de subir a aplicação. Tanto sua infraestrutura e
  persistência da dados estão configurados, além de poder subir a própria aplicação como um container.


- Conseguir agendar uma execução para um dia e horario.

### Libs sugeridas:

 - Selenium 
 - Scrapy
 - Pandas
 - Requests
 - BeautifulSoup 


### O que iremos avaliar:

- Conhecimento em HTML
- Conhecimento em fluxo de request/response
- Conhecimento em extração de dados
- Conhecimento em base64
- Boas práticas de programação
- Utilização de bibliotecas de terceiros
- Documentação
- Criatividade
- Cobertura de testes
- Tempo de execução do código
- Versionamento do código



