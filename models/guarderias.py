
from db import db

class Guarderias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45), nullable=False)

    cuidadores = db.relationship('Cuidadores', backref="guarderias", lazy=True)
    perros = db.relationship('Perros', backref="guarderias", lazy=True)
