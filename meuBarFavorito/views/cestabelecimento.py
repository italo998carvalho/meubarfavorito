from flask import Blueprint, request, jsonify
from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required
import requests as req
import time, ast

bpestabelecimento = Blueprint('bpestabelecimento', __name__)

@bpestabelecimento.route('/estabelecimento', methods=['POST'])
def estabelecimento():
    # Consulta na API de cnpj
    cnpj = 60701190000104
    source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
    while source.status_code == 429:
        time.sleep(3)
        source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))

    print(str(dir(source)))
    source = source.text
    return source

    if source['status'] == "OK" and source['situacao'] == "ATIVA":
        return 'ativa'
    else:
        return source['message']

    # try:
    #     data = request.get_json()

    #     nome = data['nome']
    #     descricao = data['descricao']
    #     cnpj = data['cnpj']
    #     cep = data['cep']
    #     endereco = data['endereco']
    #     email = data['email']
    #     senha = data['senha']
    #     telefone = data['telefone']
    #     celular = data['celular']

    #     cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

    #     checkCnpj = Estabelecimento.query.filter_by(cnpj = cnpj).first()

    #     if checkCnpj is not None:
    #         return jsonify({'code': 409, 'body': {'mensagem': 'Este CNPJ já está cadastrado!'}}), 409

    #     # Consulta na API de cnpj
    #     source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
    #     while source.status_code == 429:
    #         time.sleep(3)
    #         source = req.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))

    #     if source['status'] == "OK" and source['situacao'] == "ATIVA":
    #         return 'ativa'
    #     else:
    #         return source['message']


    #     novoEstabelecimento = Estabelecimento(nome, descricao, cnpj, cep, endereco, email, senha, telefone, celular)

    #     db.session.add(novoEstabelecimento)
    #     db.session.commit()

    #     fotos = data['fotos']
    #     for foto in fotos:
    #         novaFoto = Foto(foto, novoEstabelecimento.id)

    #         db.session.add(novaFoto)
    #         db.session.commit()
            
    #     return jsonify({'code': 200, 'body': {'mensagem': 'Estabelecimento cadastrado com sucesso!'}}), 200
    # except Exception as ex:
    #     print(ex.args)
    #     return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

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