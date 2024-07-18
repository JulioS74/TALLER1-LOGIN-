
from db import db

class Perros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    raza = db.Column(db.String(45), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    id_guarderia = db.Column(db.Integer, db.ForeignKey("guarderias.id"), nullable=False)
    id_cuidador = db.Column(db.Integer, db.ForeignKey("cuidadores.id"), nullable=False)