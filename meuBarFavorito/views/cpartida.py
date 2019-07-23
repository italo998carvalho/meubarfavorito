from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Partida import Partida
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required
from meuBarFavorito.infraestructure.DbAccess import getPartida, getListaDePartidas

bppartida = Blueprint('bppartida', __name__)

@bppartida.route('/partida', methods=['GET'])
def partida():
    partidas = getListaDePartidas()

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
        partidaAtual['estadio'] = partida.estadio
        
        listaPartidas.append(partidaAtual)
    
    return jsonify(listaPartidas)

@bppartida.route('/partida/<int:id>', methods=['GET'])
def onePartida(id):
    partida = getPartida(id)

    partidaAtual = {}
    partidaAtual['nomeMandante'] = partida.nomeMandante
    partidaAtual['escudoMandante'] = partida.escudoMandante
    partidaAtual['nomeVisitante'] = partida.nomeVisitante
    partidaAtual['escudoVisitante'] = partida.escudoVisitante
    partidaAtual['dataHora'] = partida.dataHora
    partidaAtual['estadio'] = partida.estadio
    partidaAtual['campeonato'] = partida.campeonato
    
    return jsonify(partidaAtual)