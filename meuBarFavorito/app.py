from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = '***REMOVED***'
db = SQLAlchemy(app)
app.secret_key = '123456789'

@app.route('/')
def index():
    return 'MEU BAR FAVORITO'

from meuBarFavorito.views.login import auth
app.register_blueprint(auth)

from meuBarFavorito.views.cestabelecimento import bpestabelecimento
app.register_blueprint(bpestabelecimento)

from meuBarFavorito.views.cpartida import bppartida
app.register_blueprint(bppartida)

from meuBarFavorito.views.cevento import bpevento
app.register_blueprint(bpevento)
