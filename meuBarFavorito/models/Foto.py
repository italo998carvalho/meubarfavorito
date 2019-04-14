from meuBarFavorito.app import db

class Foto(db.Model):
    __tablename__: 'fotos'

    id = db.Column(db.Integer, primary_key=True)
    midia = db.Column(db.String)
    idEstabelecimento = db.Column(db.Integer, db.ForeignKey('estabelecimento.id'))

    def __init__(self, midia, idEstabelecimento):
        self.midia = midia
        self.idEstabelecimento = idEstabelecimento