- Cuando desarrollamos proyectos en python es recomendable hacerlos en un entorno virtual, es un espacio donde estan los paquetes de un proyecto.
Ej virtualenv, pipenv, anaconda, etc

Utilizamos Anaconda

```console
conda create --name FasAPI-FaztCode python=3

conda activate FasAPI-FaztCode

code .

```
- Para ejecutar y que lo reconozca con el entorno virtual hacemos ctrl + p y escribimos:

```markdown
python select interpreter
```
y elegimos la de nuestro entorno virtual.
Para comprobarlo vemos que abajo en la linea celeste nos dice la version y el nombre.

    

 - Instalamos paquetes fastapi y uvicorn.
 Para guardar estas dependencias,listarlas en un archivo aparte
 ```python
pip freeze > requirements.txt

pip list --format=freeze > requirements.txt
```
Aca se guardan los paquetes que instalamos.

**PARA HEROKU**
- Crear nueva app en la pagina de heroku
- Crear archivo runtime.txt con la version de python
- Crear procfile para que arranque la aplicacion

**PARA GIT**
- Crear el proyecto, fijarse que este en el entorno virtual la terminal
```python
git init
```
 - Crear archivo .gitignore 
 - Crear .vscode y colocar los archivos dentro de esta carpeta
 - En la terminal
 ```python
git add .
```
- Para ver los archivos que se van a subir
```python
git status
```
- Para subirlo
```console
git commit -m 'comentario'
```
- Comprobar si funciona heroku
```python
heroku --version
```
- Para que nos muestre el link
```python
heroku git:remote -a app-posts
```
- Nos lista hacia donde se va a listar el codigo
```python
git remote -v
```
- Finalmente subirlo. Antes vemos que la rama esta en *master y queremos subirlo con el branch main de git
- Para cambiar las ramas ejecutamos, creamos la rama main y eliminamos la master
```python
git checkout -b main
git branch -D master

```