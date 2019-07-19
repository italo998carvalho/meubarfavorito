import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connUser = os.environ.get('CONN_USER')
connPassword = os.environ.get('CONN_PASSWORD')
connHost = os.environ.get('CONN_HOST')
connDb = os.environ.get('CONN_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://{connUser}:{connPassword}@{connHost}/{connDb}'

db = SQLAlchemy(app)
app.secret_key = '123456789'
migrate = Migrate(app, db)

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
