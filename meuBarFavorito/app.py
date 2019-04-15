from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://italo:1234@localhost:5432/meubarfavoritodb'
db = SQLAlchemy(app)
app.secret_key = '123456789'

@app.route('/')
def index():
    return 'MEU BAR FAVORITO'

from meuBarFavorito.views.login import auth
app.register_blueprint(auth)

from meuBarFavorito.views.cestabelecimento import bpestabelecimento
app.register_blueprint(bpestabelecimento)