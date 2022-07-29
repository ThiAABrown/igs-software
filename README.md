# IGS Software

Este é um sistema para gerenciamento de funcionários e departamentos.


## A) Features

- Na página inicial, mostra uma lista de todos os funcionários e seus departamentos.
Acessada em 'http://localhost:8080/'

- Django Admin para gerenciamento do CRUD de funcionários e departamentos.
Acessado em 'http://localhost:8080/admin/'

- API REST com os métodos.
Documentação disponível em 'http://localhost:8080/api/'


## B) Tecnologias utilizadas

### Frontend

- Simple CSS (https://simplecss.org/)

### Backend

- Python 3.10.1
- Django 4.0.6
- Django Rest Framework 3.13.1
- SQLite como banco de dados

## C) Instruções de instalação

1) Crie um virtualenv (usei o pyenv/pyenv-virtualenv)

2) Clone esse projeto:
`git clone https://github.com/ThiAABrown/igs-software.git`

3) Entre na pasta onde o repositório foi clonado:
`cd igs-software`

4) Instale os requirements na virtualenv criada:
`pip install -r requirements.txt`

5) Rode as migrations, para popular o banco SQLite com as tabelas:

`cd igsSoftwareManager`

`python manage.py migrate`

6) Crie um superuser para poder acessar o Django Admin:
`python manage.py createsuperuser`

7) Suba o servidor local de desenvolvimento:
`python manage.py runserver`

8) Acesse as features descritas na seção "A) Features" acima. Para acessar o Django Admin, use as credenciais que você criou no passo 6 (createsuperuser).

## D) Processo de desenvolvimento

A branch principal desse projeto é a master. A branch está protegida de pushs diretos.

Para cada feature que implementei criei uma nova branch derivada da master, e ao terminar a feature, realizei um push, criei um pull request no github e mergeei o pull request na master.

Trabalhei com issues no repositório do github, para ter um controle das tarefas. O link para as issues é este: https://github.com/ThiAABrown/igs-software/issues?q=is%3Aissue+is%3Aclosed .

