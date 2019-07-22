## Meu Bar Favorito
This is the API of my final project on the graduation, projected with @danielfssz, and named "Meu Bar Favorito", which means something like "My Favorite Pub" in english.
We've made an application to help people to find establishments e.g. pubs, restaurants, fast foods, that broadcast soccer games (at first), then  you can plan to watch with friends, family, hold an event, etc.

### Requirements to run the project
- Python 3
- PostgreSQL (or any other SQL database supported by the Flask-SQLAlchemy lib)

### Running
1. Clone this repository and open it in the terminal
2. Run `python3 -m venv venv` to create a virtual environment
3. Run `source venv/bin/activate` to activate your virtual environment
4. Run `pip install -r requirements.txt` to install all the dependencies of the project
5. Now you need to configure the environment variables of the database connection on flask running something like these `export VARIABLE_NAME=value`, replacing `VARIABLE_NAME` for the variables shown below:
	- CONN_USER (The user of your DB)
	- CONN_PASSWORD (The password of your DB)
	- CONN_HOST (The host of your DB e.g. localhost:5432)
	- CONN_DB (The name of your DB)
6. Then run `python3 run.py` to run the project

Note: All of this configuration were made in a Linux Ubuntu 18.04 environment

### Routes
#### Auth

  

###### /login - POST

###### Log in the establishment

```bash

{

"email": "bardoze@email.com",

"senha": "123"

}

```

  

#### Establishment

  

###### /estabelecimento - POST

###### Register an establishment

```bash

{

	"nome": "John's pub",

	"descricao": "It's an awesome place",

	"cnpj": "66.729.363/0001-80",

	"endereco": "12th Street, 124",

	"cep": "45998123",

	"email": "johnspub@email.com",

	"senha": "123",

	"telefone": "40028923",

	"celular": "948875621",

	"fotoPerfil": "b64pokpokpok",

	"fotosEstabelecimento": [

		"b64jhagsdjghbds",

		"b64qiouweoiqvwoieq",

		"b64znvxczvxdmbz"

	]

}

```

  

###### /estabelecimento - GET

###### Returns the complete informations of the logged establishment

```bash

{

	"cnpj": "60701190000104",

	"descricao": "It's an awesome place",

	"email": "johnspub@email.com",

	"endereco": "12th Street, 124",

	"fotoPerfil": "b64pokpokpok",

	"fotosEstabelecimento": [

		"b64jhagsdjghbds",

		"b64qiouweoiqvwoieq",

		"b64znvxczvxdmbz"

	],

	"id": 3,

	"nome": "John's Pub",

	"telefone": "40028923"

}

```

  

###### /estabelecimento - PUT

###### Updates the informarion of the logged establishment

```bash

{

	"celular": "948875621",

	"cep": "45998123",

	"descricao": "It's an incredible place",

	"email": "johnspub@outlook.com",

	"endereco": "12th Street, 200",

	"nome": "John's Pub",

	"telefone": "40028923"

}

```

  

##### /estabelecimento - DELETE

##### Excludes the logged establishment

  
  

#### Event

  

###### /evento - POST

###### Register an event

```bash

{

	"idPartida": "1",

	"horaInicio": "21:00",

	"horaFim": "00:00",

	"descricao": "promoção..."

}

```

  

###### /evento - GET

###### Returns all the events

```bash

[

	{

		"campeonato": "Brazilian League",

		"data": "Sun, 30 Jun 2019 21:45:00 GMT",

		"enderecoEstabelecimento": "12th Street, 124",

		"escudoMandante": "b64qoiwueoquwoeoqie",

		"escudoVisitante": "b64qoiwueoquwoeoqqw",

		"fotoPerfil": "b64hueheuhue",

		"id": 3,

		"nomeEstabelecimento": "John's Pub",

		"nomeMandante": "Palmeiras",

		"nomeVisitante": "Corinthians"

	},

	{

		"campeonato": "Brazilian League",

		"data": "Sun, 02 Jul 2019 21:45:00 GMT",

		"enderecoEstabelecimento": "12th Street, 125",

		"escudoMandante": "b64qoiwueoquwoeoqas",

		"escudoVisitante": "b64qoiwueoquwoeoqjh",

		"fotoPerfil": "b64qiowueoqiwe",

		"id": 5,

		"nomeEstabelecimento": "Andy's Fast Food",

		"nomeMandante": "Internacional",

		"nomeVisitante": "Grêmio"

	}

]

```

  

###### /evento/<id> - GET

###### Returns all the information of an event

```bash

{

	"campeonato": "Brazilian League",

	"celular": "948875621",

	"cep": "45998123",

	"data": "Sun, 30 Jun 2019 21:45:00 GMT",

	"descricaoEstabelecimento": "It's an awesome place",

	"email": "johnspub@email.com",

	"enderecoEstabelecimento": "12th Street, 124",

	"escudoMandante": "b64qoiwueoquwoeoqie",

	"escudoVisitante": "b64qoiwueoquwoeoqqw",

	"estadio": "Allianz Park",

	"fotoPerfil": "b64hueheuhue",

	"fotosEstabelecimento": [

		"b64jhagsdjghbds",

		"b64qiouweoiqvwoieq",

		"b64znvxczvxdmbz"

	],

	"id": 3,

	"nomeEstabelecimento": "Jonh's Pub",

	"nomeMandante": "Palmeiras",

	"nomeVisitante": "Corinthians",

	"telefone": "40028923",

	"visualizacoes": 0

}

```

  

###### /partida/<id>/evento - GET | PS: O id é do estabelecimento

###### Returns the list of events of the logged establishment

```bash

[

	{

	"campeonato": "Brazilian League",

	"data": "Sun, 30 Jun 2019 21:45:00 GMT",

	"enderecoEstabelecimento": "12th Street, 124",

	"escudoMandante": "b64qoiwueoquwoeoqie",

	"escudoVisitante": "b64qoiwueoquwoeoqqw",

	"fotoPerfil": "b64qiowueoqiwe",

	"id": 3,

	"nomeEstabelecimento": "John's Pub",

	"nomeMandante": "Palmeiras",

	"nomeVisitante": "Corinthians"

	}

]

```

  
  

#### Match

  

###### /partida - GET

###### Returns a list with all the matches registered

```bash

[

	{

	"campeonato": "Brazilian League",

	"dataHora": "Sun, 30 Jun 2019 21:45:00 GMT",

	"id": 17,

	"nomeMandante": "Palmeiras",

	"escudoMandante": "b64qoiwueoquwoeoqie",

	"nomeVisitante": "Corinthians",

	"escudoVisitante": "b64qoiwueoquwoeoqqw"

	},

	{

	"campeonato": "Brazilian League",

	"dataHora": "Sun, 02 Jul 2019 21:45:00 GMT",

	"id": 1,

	"nomeMandante": "Internacional",

	"escudoMandante": "b64qoiwueoquwoeoqas",

	"nomeVisitante": "Grêmio",

	"escudoVisitante": "b64qoiwueoquwoeoqjh"

	}

]

```

  

###### /partida/<id> - GET

###### Retorna as informações de uma única partida
###### Returns the information of a single match

```bash

{

"campeonato": "Brazilian League",

"dataHora": "Sun, 30 Jun 2019 21:45:00 GMT",

"escudoMandante": "b64qoiwueoquwoeoqie",

"escudoVisitante": "b64qoiwueoquwoeoqqw",

"estadio": "Allianz Park",

"nomeMandante": "Palmeiras",

"nomeVisitante": "Corinthians"

}

```
Note 1: CEP is a street indentification number in Brazil

Note 2: CNPJ is a company identification number in Brazil, we use it to check if the company is valid during the registration in an external API

### Update matches
We've built a crawler to update the matches automatically when you executes it, to do so, run: `python3 crawler.py`

### Apply migrations

```bash

export FLASK_APP=meuBarFavorito/app.py

```

```bash

flask db migrate

```

```bash

flask db upgrade

```