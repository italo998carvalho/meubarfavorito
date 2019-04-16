from meuBarFavorito.app import db

class Evento(db.Model):
    __tablename__: 'eventos'

    id = db.Column(db.Integer, primary_key=True)
    idEstabelecimento = db.Column(db.Integer, db.ForeignKey('estabelecimento.id'))
    idPartida = db.Column(db.Integer, db.ForeignKey('partida.id'))
    horaInicio = db.Column(db.String)
    horaFim = db.Column(db.String)
    descricao = db.Column(db.Text)
    visualizacoes = db.Column(db.Integer)

    def __init__(self, idEstabelecimento, idPartida, horaInicio, horaFim, descricao):
        self.idEstabelecimento = idEstabelecimento
        self.idPartida = idPartida
        self.horaInicio = horaInicio
        self.horaFim = horaFim
        self.descricao = descricao