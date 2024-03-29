from flask import Blueprint, request, jsonify, abort, make_response
from meuBarFavorito.infraestructure.DbAccess import commit, salvar, deletar, abortComErro
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
    data = request.get_json()

    # recebe e limpa a string de cnpj
    cnpj = data['cnpj'].replace(".", "").replace("/", "").replace("-", "")

    # verifica se ja tem um cnpj igual no banco
    verificaCNPJRepetido(cnpj)

    # consulta a API de CNPJ para verificar a situação atual
    consultaCNPJ(cnpj)

    cadastraEstabelecimento(
        nome = data['nome'], 
        descricao = data['descricao'], 
        cnpj = cnpj, 
        cep = data['cep'], 
        endereco = data['endereco'], 
        email = data['email'], 
        senha = data['senha'], 
        telefone = data['telefone'], 
        celular = data['celular'], 
        fotoPerfil = data['fotoPerfil'], 
        fotosEstabelecimento = data['fotosEstabelecimento']
    )

    return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento cadastrado com sucesso!'}}), 200

@bpestabelecimento.route('/estabelecimento', methods=['GET'])
@token_required
def getEstabelecimento(estabelecimentoAtual):
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

    fotoPerfil = getFoto(estabelecimentoAtual.fotoPerfil)
    estabelecimento['fotoPerfil'] = fotoPerfil.midia

    fotos = getListaDeFotosDoEstabelecimento(estabelecimentoAtual)
    
    estabelecimentoFotos = []
    for foto in fotos:
        estabelecimentoFotos.append(foto.midia)

    estabelecimento['fotosEstabelecimento'] = estabelecimentoFotos

    return jsonify(estabelecimento)

@bpestabelecimento.route('/estabelecimento', methods=['PUT'])
@token_required
def putEstabelecimento(estabelecimentoAtual):
    data = request.get_json()

    estabelecimentoAtual.nome = data['nome']
    estabelecimentoAtual.descricao = data['descricao']
    estabelecimentoAtual.cep = data['cep']
    estabelecimentoAtual.endereco = data['endereco']
    estabelecimentoAtual.email = data['email']
    estabelecimentoAtual.telefone = data['telefone']
    estabelecimentoAtual.celular = data['celular']

    commit()

    return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento atualizado com sucesso!'}}), 200

@bpestabelecimento.route('/estabelecimento', methods=['DELETE'])
@token_required
def delEstabelecimento(estabelecimentoAtual):
    eventos = Evento.query.filter_by(idEstabelecimento=estabelecimentoAtual.id).all()
    for evento in eventos:
        deletar(evento)

    fotos = Foto.query.filter_by(idEstabelecimento=estabelecimentoAtual.id).all()
    for foto in fotos:
        deletar(foto)

    deletar(estabelecimentoAtual)

    return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento atualizado com sucesso!'}}), 200

def cadastraEstabelecimento(nome, descricao, cnpj, cep, endereco, email, senha, telefone, celular, fotoPerfil, fotosEstabelecimento):
    novoEstabelecimento = Estabelecimento(nome, descricao, cnpj, cep, endereco, email, senha, telefone, celular)
    salvar(novoEstabelecimento)

    fotoPerfil = salvaFoto(fotoPerfil, novoEstabelecimento.id)

    novoEstabelecimento.fotoPerfil = fotoPerfil.id
    commit()

    for foto in fotosEstabelecimento:
        novaFoto = salvaFoto(foto, novoEstabelecimento.id)

    return novoEstabelecimento

def salvaFoto(midia, idEstabelecimento):
    novaFoto = Foto(midia, idEstabelecimento)
    salvar(novaFoto)

    return novaFoto

def consultaCNPJ(cnpj):
    source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
    while source.status_code == 429:
        time.sleep(3)
        source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
    
    source = source.json()

    if source['status'] == 'ERROR':
        abortComErro({'code': 409, 'body': {'mensagem': source['message']}}, 409)
    if source['status'] == "OK" and source['situacao'] != "ATIVA":
        abortComErro({'code': 409, 'body': {'mensagem': 'Situação da empresa: {}'.format(source['situacao'])}}, 409)

def verificaCNPJRepetido(cnpj):
    checkCnpj = Estabelecimento.query.filter_by(cnpj = cnpj).first()
    if checkCnpj is not None:
        abortComErro({'code': 409, 'body': {'mensagem': 'Este CNPJ já está cadastrado!'}}, 409)

def getFoto(id):
    try:
        return Foto.query.filter_by(id = id).first()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)

# retorna todas as fotos do estabelecimento, com exceção da foto de perfil
def getListaDeFotosDoEstabelecimento(estabelecimento):
    try:
        return Foto.query.filter(Foto.idEstabelecimento == estabelecimento.id).filter(Foto.id != estabelecimento.fotoPerfil).all()
    except Exception as ex:
        print(ex.args)
        abortComErro({'code': 500, 'body': {'mensagem': 'Erro interno!'}}, 500)