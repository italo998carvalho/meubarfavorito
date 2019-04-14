from meuBarFavorito.app import db

class Foto(db.Model):
    __tablename__: 'fotos'

    id = db.Column(db.Integer, primary_key=True)
    idEstabelecimento = db.Column(db.Integer, db.ForeignKey('estabelecimento.id'))
    idPartida = db.Column(db.Integer, db.ForeignKey('partida.id'))
    horaInicio = db.Column(db.String)
    horaFim = db.Column(db.String)
    descricao = db.Column(db.Text)

    def __init__(self, idEstabelecimento):
        self.idEstabelecimento = idEstabelecimento
        self.idPartida = idPartida
        self.horaInicio = horaInicio
        self.horaFim = horaFim
        self.descricao = descricao