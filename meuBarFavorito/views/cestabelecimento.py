from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.models.Evento import Evento
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required
import requests as req
import time, ast

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
        fotoPerfil = data['fotoPerfil']

        # limpa a string de cnpj
        cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

        # verifica se ja tem um cnpj igual no banco
        checkCnpj = Estabelecimento.query.filter_by(cnpj = cnpj).first()
        if checkCnpj is not None:
            return jsonify({'code': 409, 'body': {'mensagem': 'Este CNPJ já está cadastrado!'}}), 409

        # Consulta na API de cnpj
        source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
        while source.status_code == 429:
            time.sleep(3)
            source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
        
        source = source.json()

        if source['status'] == 'ERROR':
            return jsonify({'code': 409, 'body': {'mensagem': source['message']}}), 409
        if source['status'] == "OK" and source['situacao'] != "ATIVA":
            return jsonify({'code': 409, 'body': {'mensagem': 'Situação da empresa: {}'.format(source['situacao'])}}), 409


        novoEstabelecimento = Estabelecimento(nome, descricao, cnpj, cep, endereco, email, senha, telefone, celular)
        db.session.add(novoEstabelecimento)
        db.session.commit()

        fotoPerfil = Foto(fotoPerfil, novoEstabelecimento.id)
        db.session.add(fotoPerfil)
        db.session.commit()

        novoEstabelecimento.fotoPerfil = fotoPerfil.id
        db.session.commit()

        fotosEstabelecimento = data['fotosEstabelecimento']
        for foto in fotosEstabelecimento:
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
        estabelecimento['id'] = estabelecimentoAtual.id
        estabelecimento['nome'] = estabelecimentoAtual.nome
        estabelecimento['descricao'] = estabelecimentoAtual.descricao
        estabelecimento['cep'] = estabelecimentoAtual.cep
        estabelecimento['cnpj'] = estabelecimentoAtual.cnpj
        estabelecimento['endereco'] = estabelecimentoAtual.endereco
        estabelecimento['email'] = estabelecimentoAtual.email
        estabelecimento['telefone'] = estabelecimentoAtual.telefone
        estabelecimento['celular'] = estabelecimentoAtual.celular

        fotoPerfil = Foto.query.filter_by(id = estabelecimentoAtual.fotoPerfil).first()
        estabelecimento['fotoPerfil'] = fotoPerfil.midia

        # retorna todas as fotos do estabelecimento, com exceção da foto de perfil
        fotos = Foto.query.filter(Foto.idEstabelecimento == estabelecimentoAtual.id).filter(Foto.id != estabelecimentoAtual.fotoPerfil).all()
        
        estabelecimentoFotos = []
        for foto in fotos:
            fotoAtual = foto.midia
            estabelecimentoFotos.append(fotoAtual)

        estabelecimento['fotosEstabelecimento'] = estabelecimentoFotos

        return jsonify(estabelecimento)
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bpestabelecimento.route('/estabelecimento', methods=['PUT'])
@token_required
def putEstabelecimento(estabelecimentoAtual):
    try:
        data = request.get_json()

        nome = data['nome']
        descricao = data['descricao']
        cep = data['cep']
        endereco = data['endereco']
        email = data['email']
        telefone = data['telefone']
        celular = data['celular']

        estabelecimentoAtual.nome = nome
        estabelecimentoAtual.descricao = descricao
        estabelecimentoAtual.cep = cep
        estabelecimentoAtual.endereco = endereco
        estabelecimentoAtual.email = email
        estabelecimentoAtual.telefone = telefone
        estabelecimentoAtual.celular = celular

        db.session.commit()

        return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento atualizado com sucesso!'}}), 200
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bpestabelecimento.route('/estabelecimento', methods=['DELETE'])
@token_required
def delEstabelecimento(estabelecimentoAtual):
    try:
        eventos = Evento.query.filter_by(idEstabelecimento=estabelecimentoAtual.id).all()
        for evento in eventos:
            db.session.delete(evento)
            db.session.commit()

        fotos = Foto.query.filter_by(idEstabelecimento=estabelecimentoAtual.id).all()
        for foto in fotos:
            db.session.delete(foto)
            db.session.commit()

        db.session.delete(estabelecimentoAtual)
        db.session.commit()

        return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento atualizado com sucesso!'}}), 200
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500
