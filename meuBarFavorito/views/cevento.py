from flask import Blueprint, request, jsonify
from meuBarFavorito.infraestructure.DbAccess import commit, salvar, deletar, abortComErro
from meuBarFavorito.infraestructure.DbAccess import getEstabelecimento, getEvento, getEventoPorPartida, getFoto, getListaDeFotosDoEstabelecimento, getPartida
from meuBarFavorito.models.Evento import Evento
from meuBarFavorito.models.Partida import Partida
from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.app import db
from meuBarFavorito.views.login import token_required

bpevento = Blueprint('bpevento', __name__)

@bpevento.route('/evento', methods=['POST'])
@token_required
def postEvento(estabelecimentoAtual):
    data = request.get_json()

    idEstabelecimento = estabelecimentoAtual.id

    verificarEventoRepetido(idEstabelecimento, data['idPartida'])
    
    cadastrarEvento(
        idEstabelecimento = idEstabelecimento, 
        idPartida = data['idPartida'], 
        horaInicio = data['horaInicio'], 
        horaFim = data['horaFim'], 
        descricao = data['descricao']
    )

    return jsonify({'code': 200, 'body': {'mensagem': 'Evento cadastrado com sucesso!'}}), 200

@bpevento.route('/evento', methods=['GET'])
def getEventos():
    eventos = Evento.query.all()

    eventosCompletos = []
    for evento in eventos:
        partida = getPartida(evento.idPartida)
        estabelecimento = getEstabelecimento(evento.idEstabelecimento)
        fotoPerfil = getFoto(estabelecimento.fotoPerfil)

        eventoAtual = {}
        eventoAtual['id'] = evento.id
        eventoAtual['nomeEstabelecimento'] = estabelecimento.nome
        eventoAtual['enderecoEstabelecimento'] = estabelecimento.endereco
        eventoAtual['fotoPerfil'] = fotoPerfil.midia
        eventoAtual['nomeMandante'] = partida.nomeMandante
        eventoAtual['escudoMandante'] = partida.escudoMandante
        eventoAtual['nomeVisitante'] = partida.nomeVisitante
        eventoAtual['escudoVisitante'] = partida.escudoVisitante
        eventoAtual['data'] = partida.dataHora
        eventoAtual['campeonato'] = partida.campeonato
        eventoAtual['estadio'] = partida.estadio

        eventosCompletos.append(eventoAtual)

    return jsonify(eventosCompletos)

@bpevento.route('/evento/<int:id>', methods=['GET'])
def getOneEvento(id):
    evento = getEvento(id)
    partida = getPartida(evento.idPartida)
    estabelecimento = getEstabelecimento(evento.idEstabelecimento)
    fotoPerfil = getFoto(estabelecimento.fotoPerfil)

    eventoAtual = {}
    eventoAtual['id'] = evento.id
    eventoAtual['visualizacoes'] = evento.visualizacoes

    evento.visualizacoes += 1
    db.session.commit()

    eventoAtual['nomeEstabelecimento'] = estabelecimento.nome
    eventoAtual['descricaoEstabelecimento'] = estabelecimento.descricao
    eventoAtual['email'] = estabelecimento.email
    eventoAtual['telefone'] = estabelecimento.telefone
    eventoAtual['celular'] = estabelecimento.celular
    eventoAtual['enderecoEstabelecimento'] = estabelecimento.endereco
    eventoAtual['fotoPerfil'] = fotoPerfil.midia
    eventoAtual['cep'] = estabelecimento.cep

    fotos = getListaDeFotosDoEstabelecimento(estabelecimento.id)

    fotosEvento = []
    for foto in fotos:
        fotosEvento.append(foto.midia)
    
    eventoAtual['fotosEstabelecimento'] = fotosEvento

    eventoAtual['nomeMandante'] = partida.nomeMandante
    eventoAtual['escudoMandante'] = partida.escudoMandante
    eventoAtual['nomeVisitante'] = partida.nomeVisitante
    eventoAtual['escudoVisitante'] = partida.escudoVisitante
    eventoAtual['estadio'] = partida.estadio
    eventoAtual['data'] = partida.dataHora
    eventoAtual['campeonato'] = partida.campeonato

    return jsonify(eventoAtual)

@bpevento.route('/partida/<int:id>/evento', methods=['GET'])
def getEventosPorPartida(id):
    partida = getPartida(id)
    eventos = getEventoPorPartida(partida.id)

    eventosCompletos = []
    for evento in eventos:
        estabelecimento = getEstabelecimento(evento.idEstabelecimento)
        fotoPerfil = getFoto(estabelecimento.fotoPerfil)

        eventoAtual = {}
        eventoAtual['id'] = evento.id
        eventoAtual['nomeEstabelecimento'] = estabelecimento.nome
        eventoAtual['enderecoEstabelecimento'] = estabelecimento.endereco
        eventoAtual['fotoPerfil'] = fotoPerfil.midia
        eventoAtual['nomeMandante'] = partida.nomeMandante
        eventoAtual['escudoMandante'] = partida.escudoMandante
        eventoAtual['nomeVisitante'] = partida.nomeVisitante
        eventoAtual['escudoVisitante'] = partida.escudoVisitante
        eventoAtual['data'] = partida.dataHora
        eventoAtual['campeonato'] = partida.campeonato
        eventoAtual['estadio'] = partida.estadio

        eventosCompletos.append(eventoAtual)

    return jsonify(eventosCompletos)

def cadastrarEvento(idEstabelecimento, idPartida, horaInicio, horaFim, descricao):
    novoEvento = Evento(idEstabelecimento, idPartida, horaInicio, horaFim, descricao)
    salvar(novoEvento)

    return novoEvento

def verificarEventoRepetido(idEstabelecimento, idPartida):
    checkEventos = Evento.query.filter_by(idEstabelecimento = idEstabelecimento, idPartida = idPartida).first()

    if checkEventos is not None:
        abortComErro({'code': 409, 'body': {'mensagem': 'Você já possui um evento desta partida!'}}, 409)