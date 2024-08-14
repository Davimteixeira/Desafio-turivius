## ✨ Estrutura Base do Projeto

O projeto é um desafio proposto pela empresa Turivius. Utilizando tecnologias como Python, Django, JWT, Django Rest Framework (DRF), soft delete, Docker, PostgreSQL e Swagger.

## ✨ Como Executar Localmente

```bash
$ # Baixe o código
$ git clone https://github.com/Davimteixeira/Desafio-turivius
$ cd Desafio-turivius
$
$ # Instalação do ambiente com Virtualenv (Sistemas baseados em Unix)
$ virtualenv venv
$ source venv/bin/activate
$
$ # Instalação do ambiente com Virtualenv (Sistemas baseados em Windows)
$ # virtualenv venv
$ # .\venv\Scripts\activate
$
$ # Instale os módulos
$ pip3 install -r requirements.txt
$
$ # Baixe o arquivo env do Drive e copie para dentro do primeiro diretório core. Mais informações abaixo em nota.
$
$
$ # Acesse o projeto em django e crie as tabelas
$ cd Desafio-turivius
$ python manage.py makemigrations
$ python manage.py migrate
$
$
$ # Comando para rodar os tests
$ python manage.py test apps.tasks.tests.TaskViewSetTests
$
$
$ # Inicie a aplicação (development mode)
$ python manage.py runserver # porta default 8000
$
$ # Inicie a aplicação com um porta customizada
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Acesse a aplicação web no navegador: http://127.0.0.1:8000/
$
$ # OPCIONAL, segue um exemplo de rota para testar os filtros (apenas exemplos)
$ http://127.0.0.1:8000/api/tasks/?due_date=2024-08-14
$ http://127.0.0.1:8000/api/tasks/?title=string
$
```

> Nota: Para utilizar o aplicativo, é necessário atualizar o arquivo exemple.env na raiz do projeto, você deve alterar seu nome para .env
> <br />

## ✨ Como Executar no Docker (Deploy)

1. Clone o repositório
1. Baixe os arquivos .env e copie-os para o diretório core conforme informado no tópico anterior. Certifique-se de tê-lo na raiz do projeto
1. Atualize a variável de ambiente `POSTGRES_HOST` com o host adequado e as que forem necessárias
1. Execute os containers com o seguinte comando:

   ```bash
   # Usando o arquivo docker-compose default
   docker compose build
   docker-compose up
   ```

1. Após os containeres serem inicializados, execute os comandos a seguir:

   ```bash
   # Aplicar makemigrations
   docker-compose exec web python manage.py migrate
   # Para parar os contêineres, você pode usar:
   docker-compose down

   ```

<br />
