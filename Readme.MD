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
 	"fotos": [
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
    "fotos": [
        "b64jhagsdjghbds",
        "b64qiouweoiqvwoieq",
        "b64znvxczvxdmbz"
    ],
    "id": 3,
    "nome": "Bar do Zé",
    "telefone": "40028923"
}
```


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
        "escudoMandante": "linkEscudoPalmeiras",
        "escudoVisitante": "linkEscudoCorinthians",
        "id": 3,
        "nomeEstabelecimento": "Bar do Zé",
        "nomeMandante": "Palmeiras",
        "nomeVisitante": "Corinthians"
    }, 
	{
        "campeonato": "Campeonato Brasileiro", 
        "data": "Sun, 02 Jul 2019 21:45:00 GMT",
        "enderecoEstabelecimento": "rua 12, 125",
        "escudoMandante": "linkEscudoInternacional",
        "escudoVisitante": "linkEscudoGremio",
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
    "escudoMandante": "linkEscudoPalmeiras",
    "escudoVisitante": "linkEscudoCorinthians",
    "estadio": "Allianz Park",
    "fotos": [
        "b64jhagsdjghbds",
        "b64qiouweoiqvwoieq",
        "b64znvxczvxdmbz"
    ],
    "id": 3,
    "nomeEstabelecimento": "Bar do Zé",
    "nomeMandante": "Palmeiras",
    "nomeVisitante": "Corinthians",
    "siglaMandante": "PAL",
    "siglaVisitante": "COR",
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
        "escudoMandante": "linkEscudoPalmeiras",
        "escudoVisitante": "linkEscudoCorinthians",
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
        "nomeVisitante": "Corinthians"
    },
    {
        "campeonato": "Campeonato Brasileiro", 
        "dataHora": "Sun, 02 Jul 2019 21:45:00 GMT",
        "id": 1,
        "nomeMandante": "Internacional",
        "nomeVisitante": "Grêmio"
    }
]
```

###### /partida/<id> - GET
###### Retorna as informações de uma única partida
```bash
{
    "campeonato": "Campeonato Brasileiro", 
    "dataHora": "Sun, 30 Jun 2019 21:45:00 GMT",
    "escudoMandante": "linkEscudoPalmeiras",
    "escudoVisitante": "linkEscudoCorinthians",
    "estadio": "Allianz Park",
    "nomeMandante": "Palmeiras",
    "nomeVisitante": "Corinthians",
    "siglaMandante": "PAL",
    "siglaVisitante": "COR"
}
```

###### /novapartida - POST
###### Cadastra uma partida
```bash
{
	"nomeMandante": "Palmeiras", 
	"siglaMandante": "PAL", 
	"escudoMandante": "linkEscudoPalmeiras", 
	"nomeVisitante": "Corinthians", 
	"siglaVisitante": "COR", 
	"escudoVisitante": "linkEscudoCorinthians", 
	"dataHora": "30-06-2019 21:45", 
	"estadio": "Allianz Park", 
    "campeonato": "Campeonato Brasileiro"
}
```