from meuBarFavorito.app import app, db

from meuBarFavorito.models.Estabelecimento import Estabelecimento
from meuBarFavorito.models.Evento import Evento
from meuBarFavorito.models.Foto import Foto
from meuBarFavorito.models.Partida import Partida

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)