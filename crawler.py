import bs4
import requests, time, datetime, base64
from urllib.request import urlopen
from meuBarFavorito.app import db, app
from meuBarFavorito.models.Partida import Partida
from meuBarFavorito.models.Evento import Evento

def getSource(link):
    source = requests.get(link)
    while source.status_code == 429:
        time.sleep(3)
        source = requests.get(link)
    
    return source

source = getSource('https://especiais.gazetadopovo.com.br/futebol/tabela-campeonato-brasileiro-2019/')
soup = bs4.BeautifulSoup(source.text, 'lxml')

rodadas = soup.find("article", class_="rodadas")

for idRodada in range(38):
    idRodada += 1

    rodada = rodadas.find("div", id="rodada{}".format(idRodada))
    listaJogos = rodada.find("ul", class_="rodadas-classificacao")
    jogos = listaJogos.find_all("li", recursive=False)

    for jogo in jogos:
        dados = jogo.find("data")
        dados = dados.text.strip()
        dados = dados.split("   ")
        dados = [x for x in dados if x != ""]
        if len(dados) == 1: # se dados tiver apenas um registro (o estádio), significa que o jogo já ocorreu, portanto não é processado
            break

        # dataHora
        dataHora = dados[1].strip()
        dataHora = dataHora.split(" ")
        dataHora = str(dataHora[0] + " " + dataHora[2].replace("h", ":"))
        dataHora = datetime.datetime.strptime(dataHora, '%d/%m/%Y %H:%M')

        if (dataHora > (datetime.datetime.now() + datetime.timedelta(weeks = 2))): # se a partida for em mais de duas semanas, não executa
            break

        # estadio
        estadio = str(dados[2].strip())

        # nomes do mandante e visitante
        times = jogo.find_all("a")
        nomeMandante = times[0].text
        nomeVisitante = times[1].text

        # escudos do mandante e visitante
        escudos = jogo.find_all("img")

        escudoMandante = escudos[0].get("src")
        escudoMandante = urlopen("http:" + escudoMandante)
        escudoMandante = "data:image/png;base64," + base64.b64encode(escudoMandante.read()).decode("utf-8")

        escudoVisitante = escudos[1].get("src")
        escudoVisitante = urlopen("http:" + escudoVisitante)
        escudoVisitante = "data:image/png;base64," + base64.b64encode(escudoVisitante.read()).decode("utf-8")

        campeonato = "Campeonato Brasileiro SÉRIE-A"

        partida = Partida(nomeMandante, escudoMandante, nomeVisitante, escudoVisitante, dataHora, estadio, campeonato)

        checkPartida = Partida.query.filter_by(nomeMandante = nomeMandante, nomeVisitante = nomeVisitante).first()

        if checkPartida is None:
            db.session.add(partida)
            db.session.commit()

jogosPassados = Partida.query.filter(Partida.dataHora <= datetime.datetime.now()).all()
for jogo in jogosPassados:
    eventos = Evento.query.filter_by(idPartida=jogo.id).all()
    for evento in eventos:
        db.session.delete(evento)
        db.session.commit()
    db.session.delete(jogo)
    db.session.commit()