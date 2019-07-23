from meuBarFavorito.app import db
from flask import abort, make_response, jsonify
from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Evento import Evento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.models.Partida import Partida

def commit():
    try:
        db.session.commit()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def salvar(obj):
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def deletar(obj):
    try:
        db.session.delete(obj)
        db.session.commit()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def abortComErro(json, codigo):
    abort(make_response(jsonify(json), codigo))

def getEstabelecimento(id):
    try:
        return Estabelecimento.query.filter_by(id = id).first()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def getEvento(id):
    try:
        return Evento.query.filter_by(id = id).first()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def getEventoPorPartida(idPartida):
    try:
        return Evento.query.filter_by(idPartida = idPartida).all()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def getFoto(id):
    try:
        return Foto.query.filter_by(id = id).first()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def getListaDeFotosDoEstabelecimento(idEstabelecimento):
    try:
        return Foto.query.filter_by(idEstabelecimento = idEstabelecimento).all()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

def getPartida(id):
    try:
        return Partida.query.filter_by(id = id).first()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)