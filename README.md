# Plantilla para iniciar proyecto con Wagtail

Entornos dev y prod bien separados. Ambos usando postgres db para poder implementar en local una búsqueda eficiente.

## Requisitos para desarrollo

* [Poetry](https://python-poetry.org/)
* [Docker](https://docs.docker.com/get-docker/)
* [docker-compose](https://docs.docker.com/compose/install/)

## Para empezar a andar

```bash
# Fork this repository or use it as a template
git clone <your-repo>

cd <the-folder-you-have-just-pulled>

docker-compose -f docker-compose.local.yml up --build
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

## Características incluídas

### Desarrollo

* [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
* [Django Extensions](https://django-extensions.readthedocs.io/en/latest/) con shell_plus configurado para usar Jupyter Lab.
* [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/)
* Formateado de código usando [Black](https://github.com/psf/black)

TODOs para desplegar en producción con docker-deploy
* Hacer que docker-compose no trate de generar los estáticos de librearías de desarrollo
* Hacer que docker-compose local sirva correctamente css y js