from meuBarFavorito.app import db

class Partida(db.Model):
    __tablename__: 'partidas'

    id = db.Column(db.Integer, primary_key=True)
    nomeMandante = db.Column(db.String)
    siglaMandante = db.Column(db.String)
    escudoMandante = db.Column(db.String)
    nomeVisitante = db.Column(db.String)
    siglaVisitante = db.Column(db.String)
    escudoVisitante = db.Column(db.String)
    dataHora = db.Column(db.DateTime)
    estadio = db.Column(db.String)
    eventos = db.relationship('Evento', backref='partida')

    def __init__(self, nomeMandante, siglaMandante, escudoMandante, nomeVisitante, siglaVisitante, escudoVisitante, dataHora, estadio):
        self.nomeMandante = nomeMandante
        self.siglaMandante = siglaMandante
        self.escudoMandante = escudoMandante
        self.nomeVisitante = nomeVisitante
        self.siglaVisitante = siglaVisitante
        self.escudoVisitante = escudoVisitante
        self.dataHora = dataHora
        self.estadio = estadio