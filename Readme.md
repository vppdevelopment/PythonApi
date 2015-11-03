# Ambiente con Python

## Instalando
[Paso a paso en youtube](https://www.youtube.com/watch?v=PEcWR882goU)

### Python
1. [Descargar python](https://www.python.org/downloads/)
2. Instalar PIP
>`easy_install pip`
3. [Crear ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
>`virtualenv venv --distribute`
4. Activar el ambiente
> `"venv/Scripts/activate.bat"` y luego deve verse (venv)

 > `"venv/Scripts/deactivate.bat"`
5. Instalar flask
>`pip install flask`
6. Guardar requerimientos instalados
>`pip freeze > requirements.txt`
>
>`pip install -r requirements.txt`
