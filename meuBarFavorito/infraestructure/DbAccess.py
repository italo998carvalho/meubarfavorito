from meuBarFavorito.app import db
from flask import abort, make_response, jsonify

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