from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_login import LoginManager, login_required, login_user, current_user 
from dotenv import load_dotenv
from db import db
from controllers.guarderia_controller import GuarderiaController
from controllers.perro_controller import PerroController
from controllers.cuidador_controller import CuidadorController
from models.user import User # Importamos la clase User desde models.user
import os

load_dotenv()

# Generamos una clave secreta para la app Flask
secret_key = os.urandom(24)
print(secret_key.hex())

# Creamos la aplicación Flask 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)

# Configuramos Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Función para cargar un usuario dado su ID
    user = User.query.get(user_id)
    if user:
        return user
    return None

@app.route("/")
def main():
    # Ruta principal del sistema
    return "Ingresé al sistema"

@app.route("/login", methods= ["GET", "POST"])    
def login():
    if request.method == "GET":
        # Método GET: mostrar el formulario de login
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        # Buscamos al usuario en la base de datos por nombre de usuario y contraseña
        user = User.query.filter_by(username=username, password=password).first()
        print(user)
        if user:

            login_user(user)
            print(current_user)
            # Redireccionamos según el tipo de usuario (administrador o no)
            if user.is_admin:
                return redirect(url_for("perrocontroller")) # Redirigir a controlador de perros (administrador)
            else:
                return redirect(url_for("cuidadorcontroller")) # Redirigir a controlador de cuidadores (usuario normal)
    # Si no se encuentra al usuario o las credenciales son incorrectas, volvemos al formulario de login
    return render_template("login.html")

# Registramos los controladores RESTful para Guardería, Perro y Cuidador
api.add_resource(GuarderiaController, '/guarderias')
api.add_resource(PerroController, '/perros')
api.add_resource(CuidadorController, '/cuidadores')

