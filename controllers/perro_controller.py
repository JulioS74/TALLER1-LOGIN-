
from flask import render_template, make_response
from flask_restful import Resource
from flask_login import login_required, current_user
from models.perros import Perros
from db import db

class PerroController(Resource):

    @login_required
    def get(self):
        perros = Perros.query.all()
        print(current_user)
        return make_response(render_template("perros.html", perros=perros))