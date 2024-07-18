
from db import db

class Cuidadores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_guarderia = db.Column(db.Integer, db.ForeignKey("guarderias.id"), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45), nullable=False)

    perros = db.relationship('Perros', backref="cuidadores", lazy=True)

    def setNombre(self, nombre):
        self.nombre = nombre
        db.session.commit()