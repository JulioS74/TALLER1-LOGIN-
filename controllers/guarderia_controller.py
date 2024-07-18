
from flask import render_template, make_response
from flask_restful import Resource
from models.perros import Perros
from models.guarderias import Guarderias
from db import db

class GuarderiaController(Resource):
    def get(self):
        guarderias = Guarderias.query.all()
        return make_response(render_template("guarderias.html", guarderias=guarderias))    
    