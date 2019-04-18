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
            partidaAtual['nomeVisitante'] = partida.nomeVisitante
            partidaAtual['dataHora'] = partida.dataHora
            
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
        
        return jsonify(partidaAtual)
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500