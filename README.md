![CI](https://github.com/Pbezerra-dev/planilha_django/workflows/CI/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gh/Pbezerra-dev/planilha_django/branch/master/graph/badge.svg)](https://codecov.io/gh/Pbezerra-dev/planilha_django)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3](https://pyup.io/repos/github/Pbezerra-dev/planilha_django/python-3-shield.svg)](https://pyup.io/repos/github/Pbezerra-dev/planilha_django/)
[![Updates](https://pyup.io/repos/github/Pbezerra-dev/planilha_django/shield.svg)](https://pyup.io/repos/github/Pbezerra-dev/planilha_django/)


>## Sistema Para Controle De Gastos
#

__Como Rodar o Projeto?__

```bash
git clone https://github.com/Pbezerra-dev/planilha_django.git
cd planilha_django
python contrib/env_gen.py
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up -d
```
- Depêndencias do __SO__ para rodar o projeto [__docker__](https://www.docker.com/) e [__docker-compose__](https://docs.docker.com/compose/)

#

*__Funcionalidades__*

- [x] CRUD dos gastos
- [x] Sitema de login
- [x] Listagem dos gastos
- [x] Cálculo dos gastos
- [x] Troca de senha
- [x] Filtragem por mês
- [x] Sistema de cadastro
- [ ] Recuperação de senha
