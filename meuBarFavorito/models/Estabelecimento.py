from meuBarFavorito.app import db

class Estabelecimento(db.Model):
    __tablename__: 'estabelecimentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.Text)
    cnpj = db.Column(db.Integer)
    endereco = db.Column(db.String)
    email = db.Column(db.String)
    telefone = db.Column(db.String)
    fotos = db.relationship('Foto', backref='estabelecimento')
    eventos = db.relationship('Evento', backref='estabelecimento')

    def __init__(self, nome, descricao, cnpj, endereco, email, telefone):
        self.nome = nome
        self.descricao = descricao
        self.cnpj = cnpj
        self.endereco = endereco
        self.email = email
        self.telefone = telefone