from meuBarFavorito.app import db
from werkzeug.security import generate_password_hash

class Estabelecimento(db.Model):
    __tablename__: 'estabelecimentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.Text)
    cnpj = db.Column(db.String)
    cep = db.Column(db.String)
    endereco = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    telefone = db.Column(db.String)
    celular = db.Column(db.String)
    visualizacoes = db.Column(db.Integer)
    fotos = db.relationship('Foto', backref='estabelecimento')
    eventos = db.relationship('Evento', backref='estabelecimento')

    def __init__(self, nome, descricao, cnpj, cep, endereco, email, senha, telefone, celular):
        self.nome = nome
        self.descricao = descricao
        self.cnpj = cnpj
        self.cep = cep
        self.endereco = endereco
        self.email = email
        self.senha = generate_password_hash(senha)
        self.telefone = telefone
        self.celular = celular
        self.visualizacoes = 0