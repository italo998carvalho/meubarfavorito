from flask import Blueprint, request, jsonify
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
    try:
        data = request.get_json()

        idEstabelecimento = estabelecimentoAtual.id
        idPartida = data['idPartida']
        horaInicio = data['horaInicio']
        horaFim = data['horaFim']
        descricao = data['descricao']

        checkEventos = Evento.query.filter_by(idEstabelecimento = estabelecimentoAtual.id, idPartida = idPartida).first()

        if checkEventos is not None:
            return jsonify({'code': 409, 'body': {'mensagem': 'Você já possui um evento desta partida!'}}), 409
        
        novoEvento = Evento(idEstabelecimento, idPartida, horaInicio, horaFim, descricao)

        db.session.add(novoEvento)
        db.session.commit()

        return jsonify({'code': 200, 'body': {'mensagem': 'Evento cadastrado com sucesso!'}}), 200
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bpevento.route('/evento', methods=['GET'])
def getEventos():
    try:
        eventos = Evento.query.all()

        eventosCompletos = []
        for evento in eventos:
            partida = Partida.query.filter_by(id = evento.idPartida).first()
            estabelecimento = Estabelecimento.query.filter_by(id = evento.idEstabelecimento).first()
            fotoPerfil = Foto.query.filter_by(id = estabelecimento.fotoPerfil).first()

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

    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bpevento.route('/evento/<int:id>', methods=['GET'])
def getOneEvento(id):
    try:
        evento = Evento.query.filter_by(id = id).first()
        partida = Partida.query.filter_by(id = evento.idPartida).first()
        estabelecimento = Estabelecimento.query.filter_by(id = evento.idEstabelecimento).first()
        fotoPerfil = Foto.query.filter_by(id = estabelecimento.fotoPerfil).first()

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

        fotos = Foto.query.filter_by(idEstabelecimento = estabelecimento.id).all()

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
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500

@bpevento.route('/partida/<int:id>/evento', methods=['GET'])
def getEventosPorPartida(id):
    try:
        partida = Partida.query.filter_by(id = id).first()
        eventos = Evento.query.filter_by(idPartida = partida.id).all()

        eventosCompletos = []
        for evento in eventos:
            estabelecimento = Estabelecimento.query.filter_by(id = evento.idEstabelecimento).first()
            fotoPerfil = Foto.query.filter_by(id = estabelecimento.fotoPerfil).first()

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
    
    except Exception as ex:
        print(ex.args)
        return jsonify({'code': 500, 'body': {'mensagem': 'Erro interno!'}}), 500