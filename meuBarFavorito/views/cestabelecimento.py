from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required
import sys

bpestabelecimento = Blueprint('bpestabelecimento', __name__)

@bpestabelecimento.route('/estabelecimento', methods=['POST'])
def estabelecimento():
    try:
        data = request.get_json()

        nome = data['nome']
        descricao = data['descricao']
        cnpj = data['cnpj']
        cep = data['cep']
        endereco = data['endereco']
        email = data['email']
        senha = data['senha']
        telefone = data['telefone']
        celular = data['celular']

        checkCnpj = Estabelecimento.query.filter_by(cnpj = cnpj).first()

        if checkCnpj is not None:
            return jsonify({'code': 409, 'body': {'mensagem': 'Este CNPJ já está cadastrado!'}}), 409

        # Aqui vai a consulta na API de cnpj

        novoEstabelecimento = Estabelecimento(nome, descricao, cnpj, cep, endereco, email, senha, telefone, celular)

        db.session.add(novoEstabelecimento)
        db.session.commit()

        fotos = data['fotos']
        for foto in fotos:
            novaFoto = Foto(foto, novoEstabelecimento.id)

            db.session.add(novaFoto)
            db.session.commit()
            
        return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento cadastrado com sucesso!'}}), 200
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bpestabelecimento.route('/estabelecimento', methods=['GET'])
@token_required
def getEstabelecimento(estabelecimentoAtual):
    try:
        estabelecimento = {}
        estabelecimento['nome'] = estabelecimentoAtual.nome
        estabelecimento['descricao'] = estabelecimentoAtual.descricao
        estabelecimento['cnpj'] = estabelecimentoAtual.cnpj
        estabelecimento['endereco'] = estabelecimentoAtual.endereco
        estabelecimento['email'] = estabelecimentoAtual.email
        estabelecimento['telefone'] = estabelecimentoAtual.telefone

        fotos = Foto.query.filter_by(idEstabelecimento = estabelecimentoAtual.id)
        
        estabelecimentoFotos = []
        for foto in fotos:
            fotoAtual = foto.midia
            estabelecimentoFotos.append(fotoAtual)

        estabelecimento['fotos'] = estabelecimentoFotos

        return jsonify(estabelecimento)
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500