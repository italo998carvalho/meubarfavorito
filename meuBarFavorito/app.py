from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'URL DO BANCO'
db = SQLAlchemy(app)
app.secret_key = '123456789'

@app.route('/')
def index():
    return 'MEU BAR FAVORITO'