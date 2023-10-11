# Scrapper (desafio)
Criar um scrapper em Python, capaz de coletar dados de um dos seguintes sites: 
- [quotes.toscrape](https://quotes.toscrape.com/)
- [imdb.com](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

Para este projeto o escolhido foi o imdb.

# Conteúdo
<!-- TOC -->
* [Scrapper (desafio)](#scrapper-desafio)
* [Conteúdo](#conteúdo)
  * [Utilizando](#utilizando)
    * [Dependências](#dependências)
    * [Local](#local)
    * [Docker](#docker)
  * [Atenção](#atenção)
* [Testes](#testes)
* [Objetivos do projeto](#objetivos-do-projeto)
  * [Minimo Entregável:](#minimo-entregável)
  * [Pontos Extra para:](#pontos-extra-para)
    * [Libs sugeridas:](#libs-sugeridas)
    * [O que iremos avaliar:](#o-que-iremos-avaliar)
<!-- TOC -->

## Utilizando
O projeto pode ser utilizado de duas maneiras, mas antes certifique-se de instalar as dependências:

### Dependências
Antes de instalar o projeto certifiquê-se que os seguintes programas estão instalados:
* Python 3;
* virtualenv;
* Docker (caso quiser rodar ele em um container).

### Local
Da maneira local a execução pode ser realizada da seguinte maneira.

1. Suba seu ambiente virtual
```commandline
virtualenv .venv
```

2. Habilite o ambiente virtual
```commandline
source .venv/bin/activate
```
3. Instalar as depêndencias do banco de dados.
O projeto utiliza o PostgreSQL e a biblioteca psycopg na versão 3.
```commandline
sudo apt install libpq5
```
Para mais dúvidas sobre a instalação existe a [documentação da biblioteca](https://www.psycopg.org/psycopg3/docs/basic/install.html#pure-python-installation)

4. Instale as depêndencias do projeto
```commandline
pip install -r requirements.txt
```

5. Inicie a aplicação
```commandline
./run.sh
```

**Obs.:** Para subir localmente é **necessário** que esteje rodando na máquina o **Selenium Hub**, um **Nodo
Chrome** e o banco de dados **Postgres**. Por isso é mais fácil subir seguindo a próxima opção.

### Docker
Para subir com o Docker é muito simples, apenas utilize o docker compose que já está pronto nesse repositório.

```commandline
docker compose up
```

Caso precise reconstruir a imagem, após uma atualização, é possível rodar:
```commandline
docker compose build app
```

Ou caso prefira reconstruir os serviços e já subir a aplicação:
```commandline
docker compose up --build
```

Caso queira subir apenas o container da aplicação é possível rodar
```commandline
docker compose up -d --no-deps --build app
```
Isso ira forçar o docker a reconstruir a imagem, não atribuir o terminal para ela e subir a aplicação sem verificar 
os outros containers no compose.

## Atenção
Antes de iniciar o projeto e começar a realizar o scrapping é necessário ter atenção a alguns detalhes:
* Os scripts da pasta `scripts/`, com exceção do `entry-point.sh`, pressupõem que o ambiente esteja configurado localmente, 
pois dependem da presença do ambiente virtual e devem ser usados para a configuração pré execução da aplicação ou testes.
* O scrapper automaticamente salva os dados em uma tabela em um banco de dados, para que isso seja possível
rode antes de iniciar a utilizar a aplicação `./scripts/prepare.sh` esse script será responsável por preparar
o banco de dados. Esencialmente rodando todos os arquivos `.sql` dentro da pasta `sql/`.
* Caso o sistema rodando não tenha um usuário padrão não root criado na máquina é possível que o docker compose 
apresente algum erro, para isso é só remover a seguinte linha `user: 1000:1000` do arquivo `compose.yml`. Isso
foi colocado, pois pela maneira configurada o docker ira mapear a pasta `logs` para dentro do container do app
e assim rodando como um usuário não root ficará mais fácil de deletar os arquivos gerados.

# Testes
O projeto apresenta testes automatizados, para rodá-los é apenas necessário garantir que todos os serviços estão
funcinando (Nodo Chrome, Selenium Hub e Postgres) e executar o script de testes:
```commandline
./scripts/test.sh
```

# Objetivos do projeto

## Minimo Entregável:

- Buscar dados de forma automatizada(script de linha de comando ou interface clicavel)
  - Ao executar o programa ele ira se conectar no Selenium Hub e assim que tiver um nodo disponível ele
  ira começar a fazer o scrapping do imdb.
  

- Padronizar os retornos de forma estruturada (json/csv)
  - Ao finalizar o processo de scrapping ele ira criar na pasta `./logs/data` dois arquivos, um csv e outro json
  com o retorno dos dados do imdb.


- Sistema de logs de para acompanhamento da execução
  - O sistema de logs é centralizado, ele durante a execução ira criar arquivos de log na pasta `./logs/text` e
  também colocar no _stdout_.
  

- Ter um prova da consulta (Screenshot)
  - Ao finalizar o processo de scrapping o programa ira colocar uma screenshot na pasta de log `./logs/images` com
  o conteúdo da parte superior do site imdb.

## Pontos Extra para:

- Armazenamento dos resultados em um banco relacional ou não relacional
  - Todos os dados que forem coletados são armazenados em uma instância do Postgres.
  

- fazer um dataframe que possibilite visualizar os resultados via pandas
  - Ao finalizar o processo de scrapping o programa transforma a lista de filmes retornados em um _dataframe_
  do Pandas e utiliza dele para gerar os arquivos json e csv. Isso caso executar a aplicação com as opções
  `--csv --json`.


- Trazer resultados de forma dinamica sem fixar caminhos no `xpath`
  - A coleta de dados usa um Css Selector para assim caso o site mudar a posição dos elementos ele 
  ainda ira conseguir trazer os dados.


- Dockerizar a aplicação
  - Como citado anteriormente o docker é uma das alternativas de subir a aplicação. Tanto sua infraestrutura e
  persistência da dados estão configurados, além de poder subir a própria aplicação como um container.


- Conseguir agendar uma execução para um dia e horario.
  - Para agendar dia e horário basta utilizar ou o Task System no Windows ou o cron no Linux. Por
  desenvolver no Linux este projeto, coloquei dentro da raiz um arquivo `cronfile`, nele tem o conteúdo 
  que deve ser colocado no seus de cronjobs. Para isso voce pode ir até as pastas 
  `/etc/cron.{hourly, daily, weekly, monthly}` ou `/etc/cron.d` e colocar o arquivo lá. Lembre-se de alterar
  para os parêmetros desejados e colocar o caminho da pasta que este repo foi clonado. Da maneira que está ele 
  vai rodar diáriamente a meia noite.

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