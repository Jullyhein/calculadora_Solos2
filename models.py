from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy()

class Mesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poste = db.Column(db.String(50))
    fileiras = db.Column(db.String(50))
    graus = db.Column(db.String(50))
    regiao = db.Column(db.String(50))
    modulo = db.Column(db.String(50))
    preco = db.Column(db.Float)  # PREÇO DA MESA /MÓDULO

    def __init__(self, poste, fileiras, graus, regiao, modulo, preco):
        self.poste = poste
        self.fileiras = fileiras
        self.graus = graus
        self.regiao = regiao
        self.modulo = modulo
        self.preco = preco


    def __repr__(self):
        return f'<Mesa {self.poste}, {self.fileiras}, {self.graus}, {self.regiao}, {self.modulo}>'
    

class Pesquisa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(50), nullable=False)  # Estado (String)
    municipio = db.Column(db.String(100), nullable=False)  # Município (String)
    regiao = db.Column(db.Integer, nullable=False)  # Região (Inteiro)

    def __init__(self, estado, municipio, regiao):
        self.estado = estado
        self.municipio = municipio
        self.regiao = regiao


    def __repr__(self):
        return f'<Pesquisa {self.id}: {self.estado}, {self.municipio}, {self.regiao}>'
