#### Autenticação

###### /login - POST
###### Efetua o login de um estabelecimento
```bash
{
	"email": "bardoze@email.com", 
	"senha": "123"
}
```

#### Estabelecimento

###### /estabelecimento - POST
###### Cadastro do estabelecimento
```bash
{
 	"nome": "Bar do Zé", 
 	"descricao": "o bar é top", 
 	"cnpj": "66.729.363/0001-80", 
 	"endereco": "rua 12, 124", 
	"cep": "45998123", 
 	"email": "bardoze@email.com", 
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
###### Retorna as informações completas do estabelecimento logado
```bash
{
    "cnpj": "60701190000104",
    "descricao": "o bar é top",
    "email": "bardoze@email.com",
    "endereco": "rua 12, 124",
    "fotoPerfil": "b64pokpokpok",
    "fotosEstabelecimento": [
        "b64jhagsdjghbds",
        "b64qiouweoiqvwoieq",
        "b64znvxczvxdmbz"
    ],
    "id": 3,
    "nome": "Bar do Zé",
    "telefone": "40028923"
}
```

###### /estabelecimento - PUT
###### Atualiza as informações do estabelecimento logado
```bash
{
    "celular": "948875621",
    "cep": "45998123",
    "descricao": "o bar é muito bom",
    "email": "bardoze@email.com",
    "endereco": "rua 12, 200",
    "nome": "Bar do Zé",
    "telefone": "40028923"
}
```

##### /estabelecimento - DELETE
##### Exclui o estabelecimento logado e todas as suas informações


#### Evento

###### /evento - POST
###### Cadastra um evento
```bash
{
	"idPartida": "1", 
	"horaInicio": "21:00", 
	"horaFim": "00:00", 
	"descricao": "promoção..."
}
```

###### /evento - GET
###### Retorna todos os eventos
```bash
[
    {
        "campeonato": "Campeonato Brasileiro", 
        "data": "Sun, 30 Jun 2019 21:45:00 GMT",
        "enderecoEstabelecimento": "rua 12, 124",
        "escudoMandante": "b64qoiwueoquwoeoqie",
        "escudoVisitante": "b64qoiwueoquwoeoqqw",
        "fotoPerfil": "b64hueheuhue", 
        "id": 3,
        "nomeEstabelecimento": "Bar do Zé",
        "nomeMandante": "Palmeiras",
        "nomeVisitante": "Corinthians"
    }, 
	{
        "campeonato": "Campeonato Brasileiro", 
        "data": "Sun, 02 Jul 2019 21:45:00 GMT",
        "enderecoEstabelecimento": "rua 12, 125",
        "escudoMandante": "b64qoiwueoquwoeoqas",
        "escudoVisitante": "b64qoiwueoquwoeoqjh",
        "fotoPerfil": "b64qiowueoqiwe", 
        "id": 5,
        "nomeEstabelecimento": "Bar do João",
        "nomeMandante": "Internacional",
        "nomeVisitante": "Grêmio"
    }
]
```

###### /evento/<id> - GET
###### Retorna as informações de um evento
```bash
{
    "campeonato": "Campeonato Brasileiro", 
    "celular": "948875621",
    "cep": "45998123",
    "data": "Sun, 30 Jun 2019 21:45:00 GMT",
    "descricaoEstabelecimento": "o bar é top",
    "email": "bardoze@email.com",
    "enderecoEstabelecimento": "rua 12, 124",
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
    "nomeEstabelecimento": "Bar do Zé",
    "nomeMandante": "Palmeiras",
    "nomeVisitante": "Corinthians",
    "telefone": "40028923",
    "visualizacoes": 0
}
```

###### /partida/<id>/evento - GET | PS: O id é do estabelecimento
###### Retorna a lista de eventos do estabelecimento logado
```bash
[
    {
        "campeonato": "Campeonato Brasileiro", 
        "data": "Sun, 30 Jun 2019 21:45:00 GMT",
        "enderecoEstabelecimento": "rua 12, 124",
        "escudoMandante": "b64qoiwueoquwoeoqie",
        "escudoVisitante": "b64qoiwueoquwoeoqqw",
        "fotoPerfil": "b64qiowueoqiwe", 
        "id": 3,
        "nomeEstabelecimento": "Bar do Zé",
        "nomeMandante": "Palmeiras",
        "nomeVisitante": "Corinthians"
    }
]
```


#### Partida

###### /partida - GET
###### Retorna uma lista com todas as partidas cadastradas
```bash
[
    {
        "campeonato": "Campeonato Brasileiro", 
        "dataHora": "Sun, 30 Jun 2019 21:45:00 GMT",
        "id": 17,
        "nomeMandante": "Palmeiras",
        "escudoMandante": "b64qoiwueoquwoeoqie", 
        "nomeVisitante": "Corinthians", 
        "escudoVisitante": "b64qoiwueoquwoeoqqw"
    },
    {
        "campeonato": "Campeonato Brasileiro", 
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
```bash
{
    "campeonato": "Campeonato Brasileiro", 
    "dataHora": "Sun, 30 Jun 2019 21:45:00 GMT",
    "escudoMandante": "b64qoiwueoquwoeoqie",
    "escudoVisitante": "b64qoiwueoquwoeoqqw",
    "estadio": "Allianz Park",
    "nomeMandante": "Palmeiras",
    "nomeVisitante": "Corinthians"
}
```

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