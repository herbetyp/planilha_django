![CI](https://github.com/Pbezerra-dev/planilha_django/workflows/CI/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

>## Simples Panilha Para Controle De Gastos
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

- [ ] CRUD dos gastos
- [ ] Sitema de login
- [ ] Listagem dos gastos
- [ ] Cálculo dos gastos
