![CI](https://github.com/Pbezerra-dev/planilha_django/workflows/CI/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gh/Pbezerra-dev/planilha_django/branch/master/graph/badge.svg)](https://codecov.io/gh/Pbezerra-dev/planilha_django)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

>## Sistema Para Controle De Gastos
#

__Como Rodar o Projeto?__

```bash
git clone https://github.com/Pbezerra-dev/planilha_django.git
cd planilha_django
python contrib/env_gen.py
poetry shell
poetry install
docker-compose up -d
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Depêndencias do __SO__ para rodar o projeto # __docker/docker-compose__ e __poetry__

#

*__Funcionalidades__*

- [x] CRUD dos gastos
- [x] Sitema de login
- [x] Listagem dos gastos
- [x] Cálculo dos gastos
- [x] Troca de senha
- [ ] Filtragem por mês
- [ ] Sistema de cadastro
