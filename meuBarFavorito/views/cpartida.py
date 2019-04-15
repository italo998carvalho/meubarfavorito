from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Partida import Partida
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required
import sys

bppartida = Blueprint('bppartida', __name__)

@bppartida.route('/partida', methods=['GET'])
def partida():
    try:
        partidas = Partida.query.all()
    except:
        print("Erro:", sys.exc_info()[0])
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

    listaPartidas = []

    for partida in partidas:
        partidaAtual = {}
        partidaAtual['id'] = partida.id
        partidaAtual['nomeMandante'] = partida.nomeMandante
        partidaAtual['nomeVisitante'] = partida.nomeVisitante
        partidaAtual['dataHora'] = partida.dataHora
        
        listaPartidas.append(partidaAtual)
    
    return jsonify(listaPartidas)

@bppartida.route('/partida/<int:id>', methods=['GET'])
def onePartida(id):
    try:
        partida = Partida.query.filter_by(id = id).first()
    except:
        print("Erro:", sys.exc_info()[0])
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

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