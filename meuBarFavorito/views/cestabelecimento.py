from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required
import sys

bpestabelecimento = Blueprint('bpestabelecimento', __name__)

@bpestabelecimento.route('/estabelecimento', methods=['POST'])
def estabelecimento():
    data = request.get_json()

    nome = data['nome']
    descricao = data['descricao']
    cnpj = data['cnpj']
    endereco = data['endereco']
    email = data['email']
    senha = data['senha']
    telefone = data['telefone']

    # Aqui vai a consulta na API de cnpj

    novoEstabelecimento = Estabelecimento(nome, descricao, cnpj, endereco, email, senha, telefone)

    try:
        db.session.add(novoEstabelecimento)
        db.session.commit()
    except:
        print("Erro:", sys.exc_info()[0])
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

    fotos = data['fotos']
    for foto in fotos:
        novaFoto = Foto(foto, novoEstabelecimento.id)
        try:
            db.session.add(novaFoto)
            db.session.commit()
        except:
            print("Erro:", sys.exc_info()[0])
            return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
        
    return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento cadastrado com sucesso!'}}), 200

@bpestabelecimento.route('/estabelecimento', methods=['GET'])
@token_required
def getEstabelecimento(estabelecimentoAtual):
    estabelecimento = {}
    estabelecimento['nome'] = estabelecimentoAtual.nome
    estabelecimento['descricao'] = estabelecimentoAtual.descricao
    estabelecimento['cnpj'] = estabelecimentoAtual.cnpj
    estabelecimento['endereco'] = estabelecimentoAtual.endereco
    estabelecimento['email'] = estabelecimentoAtual.email
    estabelecimento['telefone'] = estabelecimentoAtual.telefone

    try:
        fotos = Foto.query.filter_by(idEstabelecimento = estabelecimentoAtual.id)
    except:
        print("Erro:", sys.exc_info()[0])
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
    
    estabelecimentoFotos = []
    for foto in fotos:
        fotoAtual = foto.midia
        estabelecimentoFotos.append(fotoAtual)

    estabelecimento['fotos'] = estabelecimentoFotos

    return jsonify(estabelecimento)