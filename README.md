TODO:


- Item existence record - done
- Price was edited 
- Rental or Purchase - done
- Database config - done
- Docker support
- Web server - done
- Event Notifier 
- Admin Interface
- Calculate item existence in days/months


{
    "identifier": "supercasas",
    "config": "./sites/supercasas/config.json",
    "baseUrl": "https://www.supercasas.com",
    "max_items": 50,
    "items_per_page": 20,
    "usd_conversion_rate": 55,
    "defaults": [
        "tipo:Header:true",
        "Metros Cuadrados:Datos Generales:true",
        "Sector:Datos Generales:true",
        "Precio:Datos Generales:true",
        "Habitaciones:Datos Generales:true",
        "Banos:Datos Generales:true",
        "Parqueo:Datos Generales:true",
        "Piso:Datos Generales:true",
        "Cantidad de visitas al anuncio:Header:true",
        "Cuotas desde:Financiamiento:true",
        "Inicial:Financiamiento:true",
        "Localizacion:Datos Generales:true",
        "condicion:Datos Generales:true",
        "edificable:Datos Generales:true",
        "uso actual:Datos Generales:true",
        "terreno:Datos Generales:true",
        "ascensores:Datos Generales:true",
        "ao construccion:Datos Generales:true",
        "Comodidades:Comodidades:true",
        "Observaciones:Observaciones:true",
        "Nombre:Datos de Inmobiliaria:true",
        "Telefono:Datos de Inmobiliaria:true",
        "Ciudad:Datos de Inmobiliaria:true",
        "Direccion:Datos de Inmobiliaria:true",
        "Nombre Agente:Agente:true",
        "Telefono Agente:Agente:true",
        "WhatsApp Agente:Agente:true"
    ]
}