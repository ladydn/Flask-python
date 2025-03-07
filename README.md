# Flask-python

Flask es un microframework hecho en Python el cual una de sus grandes ventajas es que es simple y facil de personalizar a medida que la aplicación crezca también las dependencias que se van a utilizar.

Algunas diferencias de con Django son:

Utiliza un template llamado Jinja2 que esta inspirado en los Django Templates.
Django es todo incluido mientras que Flask es lo más simple posible.
Django tiene un módelo MVC mientras que Flask no tiene un módelo especifico es libre.
Django tiene ORM mientras que Flask es más personalizable al trabajar con bases de datos.

## Instalacion de python, pip y virtualenv en Linux

### Actualizar los paquetes del sistema

```bash
sudo apt update && sudo apt upgrade -y
```

### Instalar Python y pip

```bash
sudo apt install python3 python3-pip -y
```

Verifica la instalación:

```bash
python3 --version
pip3 --version
```

### Instalar virtualenv

```bash
pip3 install virtualenv
```

### Crear y activar un entorno virtual

```bash
mkdir mi_proyecto && cd mi_proyecto
virtualenv ven
```

```bash
source venv/bin/activate
```

### Instalar Flask

```bash
pip install Flask
```

### Verificar la instalación

```bash
python -m flask --version
```

### verificar lo que se tiene instalado en Flask

```bash
pip freeze
```

correr el comando cuando se instale nuevas dependencias o extensiones para flask

```bash
pip install -r requirements.txt
```

### Crear un archivo básico de Flask (app.py)

```bash
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Flask en Linux!"

if __name__ == "__main__":
    app.run(debug=True)
```

declarar la variable de ambiente FLASK_APP, que es el archivo donde se encuentra nuestroa archivo de la instancia de
flask

### Crear un archivo básico de Flask

```bash
python app.py
```

### Desactivar el entorno virtual

```bash
deactivate
```

## Ante un error

```bash
flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.
```

### solucion

Declara una variable de ambiente

```bash
FLASK_APP=main.py
```

verificar si existe

```bash
echo $FLASK_APP
```

## Ejecutar la aplicacion

flask run

## DEBUG

muestra el error dentro de browser

```bash
export FLASK_DEBUG=1
echo $FLASK_DEBUG
flask run 
```

## CODIGOS DE ERROR

Códigos de error:
100: no son errores sino mensajes informativos. Como usuario nunca los verás, sino que entre bambalinas indica que la petición se ha recibido y se continúa el proceso.

200: estos códigos también indican que todo ha ido correctamente. La petición se ha recibido, se ha procesado y se ha devuelto satisfactoriamente. Por tanto, nunca los verás en tu navegador, pues significan que todo ha ido bien.

300: están relacionados con redirecciones. Los servidores usan estos códigos para indicar al navegador que la página o recurso que han pedido se ha movido de sitio. Como usuario, no verás estos códigos, aunque gracias a ellos una página te podría redirigir automáticamente a otra.

400: corresponden a errores del cliente y con frecuencia sí los verás. Es el caso del conocido error 404, que aparece cuando la página que has intentado buscar no existe. Es, por tanto, un error del cliente (la dirección web estaba mal).

500: mientras que los códigos de estado 400 implican errores por parte del cliente (es decir, de parte tuya, tu navegador o tu conexión), los errores 500 son errores desde la parte del servidor. Es posible que el servidor tenga algún problema temporal y no hay mucho que puedas hacer salvo probar de nuevo más tarde.