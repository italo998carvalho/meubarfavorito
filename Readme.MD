##### Post de estabelecimento

```bash
{
 	"nome": "Bar do Zé", 
 	"descricao": "o bar é top", 
 	"cnpj": "66.729.363/0001-80", 
 	"endereco": "rua 12, 124", 
 	"email": "bardoze@email.com", 
 	"senha": "123", 
 	"telefone": "40028923", 
 	"fotos": [
 		"b64jhagsdjghbds", 
 		"b64qiouweoiqvwoieq", 
 		"b64znvxczvxdmbz"
 	]
}
```


##### Post de evento

```bash
{
	"idPartida": "1", 
	"horaInicio": "21:00", 
	"horaFim": "00:00", 
	"descricao": "promoção..."
}
```

# TEMPORÁRIO
insert into partida ("nomeMandante", "siglaMandante", "escudoMandante", "nomeVisitante", "siglaVisitante", "escudoVisitante", "dataHora", "estadio")
values ('Palmeiras', 'PAL', 'linkEscudoPalmeiras', 'Vasco', 'VAS', 'linkEscudoVasco', NOW(), 'Allianz Park')

insert into partida ("nomeMandante", "siglaMandante", "escudoMandante", "nomeVisitante", "siglaVisitante", "escudoVisitante", "dataHora", "estadio")
values ('Grêmio', 'GRE', 'linkEscudoGremio', 'Internacional', 'INT', 'linkEscudoInternacional', NOW(), 'Estádio Olímpico')

insert into partida ("nomeMandante", "siglaMandante", "escudoMandante", "nomeVisitante", "siglaVisitante", "escudoVisitante", "dataHora", "estadio")
values ('Vitória', 'VIT', 'linkEscudoVitoria', 'Bahia', 'BAH', 'linkEscudoBahia', NOW(), 'Barradão')