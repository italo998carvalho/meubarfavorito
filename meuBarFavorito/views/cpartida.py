from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Partida import Partida
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required

bppartida = Blueprint('bppartida', __name__)

@bppartida.route('/partida', methods=['GET'])
def partida():
    try:
        partidas = Partida.query.all()

        listaPartidas = []

        for partida in partidas:
            partidaAtual = {}
            partidaAtual['id'] = partida.id
            partidaAtual['nomeMandante'] = partida.nomeMandante
            partidaAtual['escudoMandante'] = partida.escudoMandante
            partidaAtual['nomeVisitante'] = partida.nomeVisitante
            partidaAtual['escudoVisitante'] = partida.escudoVisitante
            partidaAtual['dataHora'] = partida.dataHora
            partidaAtual['campeonato'] = partida.campeonato
            
            listaPartidas.append(partidaAtual)
        
        return jsonify(listaPartidas)
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bppartida.route('/partida/<int:id>', methods=['GET'])
def onePartida(id):
    try:
        partida = Partida.query.filter_by(id = id).first()

        partidaAtual = {}
        partidaAtual['nomeMandante'] = partida.nomeMandante
        partidaAtual['siglaMandante'] = partida.siglaMandante
        partidaAtual['escudoMandante'] = partida.escudoMandante
        partidaAtual['nomeVisitante'] = partida.nomeVisitante
        partidaAtual['siglaVisitante'] = partida.siglaVisitante
        partidaAtual['escudoVisitante'] = partida.escudoVisitante
        partidaAtual['dataHora'] = partida.dataHora
        partidaAtual['estadio'] = partida.estadio
        partidaAtual['campeonato'] = partida.campeonato
        
        return jsonify(partidaAtual)
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bppartida.route('/novapartida', methods=['POST'])
@token_required
def postPartida(estabelecimentoAtual):
    try:
        data = request.get_json()

        nomeMandante = data['nomeMandante']
        siglaMandante = data['siglaMandante']
        escudoMandante = data['escudoMandante']
        nomeVisitante = data['nomeVisitante']
        siglaVisitante = data['siglaVisitante']
        escudoVisitante = data['escudoVisitante']
        dataHora = data['dataHora']
        estadio = data['estadio']
        campeonato = data['campeonato']

        partida = Partida(nomeMandante, siglaMandante, escudoMandante, nomeVisitante, siglaVisitante, escudoVisitante, dataHora, estadio, campeonato)

        db.session.add(partida)
        db.session.commit()

        return jsonify({'code': 200, 'body': {'mensagem': 'Partida cadastrada com sucesso!'}}), 200
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500