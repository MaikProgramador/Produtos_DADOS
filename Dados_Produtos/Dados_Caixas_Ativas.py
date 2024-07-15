import json

# Dados das caixas ativas duplas
caixas_ativas = [
    {
        "modelo": "AT-8X2",
        "potencia": "150 W",
        "conectividade": "Bluetooth, Pendrive, Cartões SD, Rádio FM",
        "altoFalante": "02 x 8\" e TWEETER",
        "sistema2em1": "Pedestal ou Retorno",
        "impedanciaEntrada": {
            "LINE": "5K Ohms",
            "MIC": "200-600 Ohms"
        },
        "equalizacaoAtiva": "03 vias (Agudo, Médio e Grave)",
        "divisorFrequencia": "01 via",
        "canaisEntrada": {
            "01": "LINE (P10)",
            "02": "Auxiliar (RCA)",
            "03": "Microfone (P10)",
            "04": "Módulo Multimídia"
        },
        "controleVolume": "Geral e Independente (por canal)",
        "canaisSaida": "LINEOUT (P10)",
        "telaMetalicaProtecaoFrontal": "Sim",
        "suportePedestal": "Sim",
        "dimensoesProduto": {
            "altura": "61,5 cm",
            "largura": "28 cm",
            "profundidade": "30,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "63 cm",
            "largura": "29 cm",
            "profundidade": "32 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "10,9 Kg",
        "pesoBruto": "11,8 Kg",
        "sobre": [
            "A Caixa Ativa dupla AT-8X2 DATREL conta com duplo woofer de 8 polegadas e driver tweeter, com 150W de potência e módulo multimídia (conexão via Bluetooth, entrada para Pendrive, Cartões SD e Rádio FM), tudo controlado por controle remoto de autonomia e praticidade em instalações onde não se permite acesso ao módulo multimídia, como, por exemplo, pedestais de parede.",
            "A AT-8X2 conta com entradas tipo P10 e RCA que garantem conectividade com equipamentos como DVD, PC, KARAOKE e microfone (com controle independente) excelente para barzinhos, área de lazer, entre outros eventos.",
            "A AT -8X2 conta com alça superior que oferece um conforto na hora do transporte, seu gabinete permite o uso na horizontal e na vertical possibilitando o uso como monitor de palco.",
            "Com a caixa ativa dupla AT-8X2 DATREL o sucesso é garantido em dobro!"
        ]
    },
    {
        "modelo": "AT-10X2",
        "potencia": "300 W",
        "conectividade": "Bluetooth, Pendrive, Cartões SD, Rádio FM",
        "altoFalante": "02 x 10\" e Driver Titânio",
        "sistema2em1": "Pedestal ou Retorno",
        "impedanciaEntrada": {
            "LINE": "5K Ohms",
            "MIC": "200-600 Ohms"
        },
        "equalizacaoAtiva": "03 vias (Agudo, Médio e Grave)",
        "divisorFrequencia": "01 via",
        "canaisEntrada": {
            "01": "LINE (P10)",
            "02": "Microfone (P10)"
        },
        "controleVolume": "USB/Sinal e Microfone",
        "canaisSaida": "LINEOUT (XLR)",
        "telaMetalicaProtecaoFrontal": "Sim",
        "suportePedestal": "Sim",
        "dimensoesProduto": {
            "altura": "75,5 cm",
            "largura": "32,5 cm",
            "profundidade": "33,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "77 cm",
            "largura": "34 cm",
            "profundidade": "35 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "17,1 Kg",
        "pesoBruto": "18,2 Kg",
        "sobre": [
            "A Caixa Ativa dupla AT-10X2 DATREL conta com duplo woofer de 10 polegadas e driver tweeter, com 300W de potência e módulo multimídia (conexão via Bluetooth, entrada para Pendrive, Cartões SD e Rádio FM), tudo controlado por controle remoto de autonomia e praticidade em instalações onde não se permite acesso ao módulo multimídia, como, por exemplo, pedestais de parede.",
            "A AT-10X2 conta com entradas tipo P10 e RCA que garantem conectividade com equipamentos como DVD, PC, KARAOKE e microfone (com controle independente) excelente para barzinhos, área de lazer, entre outros eventos.",
            "A AT -10X2 conta com alça superior que oferece um conforto na hora do transporte, seu gabinete permite o uso na horizontal e na vertical possibilitando o uso como monitor de palco."
        ]
    },
    {
        "modelo": "AT-12X2",
        "potencia": "400 W",
        "conectividade": "Bluetooth, Pendrive, Cartões SD, Rádio FM",
        "altoFalante": "02 x 12\" e Driver Titânio",
        "sistema2em1": "Pedestal ou Retorno",
        "impedanciaEntrada": {
            "LINE": "5K Ohms",
            "MIC": "200-600 Ohms"
        },
        "equalizacaoAtiva": "03 vias (Agudo, Médio e Grave)",
        "divisorFrequencia": "01 via",
        "canaisEntrada": {
            "01": "LINE (P10)",
            "02": "Microfone (P10)"
        },
        "controleVolume": "USB/Sinal e Microfone",
        "canaisSaida": "LINEOUT (XLR)",
        "telaMetalicaProtecaoFrontal": "Sim",
        "suportePedestal": "Sim",
        "dimensoesProduto": {
            "altura": "91,5 cm",
            "largura": "42,5 cm",
            "profundidade": "50 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "93 cm",
            "largura": "44 cm",
            "profundidade": "51 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "26,2 Kg",
        "pesoBruto": "27,7 Kg",
        "sobre": [
            "A Caixa Ativa dupla AT-12X2 DATREL conta com duplo woofer de 12 polegadas e driver tweeter, com 400W de potência e módulo multimídia (conexão via Bluetooth, entrada para Pendrive, Cartões SD e Rádio FM), tudo controlado por controle remoto de autonomia e praticidade em instalações onde não se permite acesso ao módulo multimídia, como, por exemplo, pedestais de parede.",
            "A AT-12X2 conta com entradas tipo P10 e RCA que garantem conectividade com equipamentos como DVD, PC, KARAOKE e microfone (com controle independente) excelente para barzinhos, área de lazer, entre outros eventos.",
            "A AT-12X2 conta com alça superior que oferece um conforto na hora do transporte, seu gabinete permite o uso na horizontal e na vertical possibilitando o uso como monitor de palco.",
            "Com a caixa ativa dupla AT-12X2 DATREL o sucesso é garantido em dobro!"
        ]
    },
    {
        "modelo": "AT-15X2",
        "potencia": "500 W",
        "conectividade": "Bluetooth, Pendrive, Cartões SD, Rádio FM",
        "altoFalante": "02 x 15\" e Driver Titânio",
        "sistema2em1": "Pedestal ou Retorno",
        "impedanciaEntrada": {
            "LINE": "5K Ohms",
            "MIC": "200-600 Ohms"
        },
        "equalizacaoAtiva": "03 vias (Agudo, Médio e Grave)",
        "divisorFrequencia": "01 via",
        "canaisEntrada": {
            "01": "LINE (P10)",
            "02": "Microfone (P10)"
        },
        "controleVolume": "USB/Sinal e Microfone",
        "canaisSaida": "LINEOUT (XLR)",
        "telaMetalicaProtecaoFrontal": "Sim",
        "suportePedestal": "Sim",
        "dimensoesProduto": {
            "altura": "104 cm",
            "largura": "45 cm",
            "profundidade": "50 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "106 cm",
            "largura": "46 cm",
            "profundidade": "51 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "36,8 Kg",
        "pesoBruto": "38,9 Kg",
        "sobre": [
            "A Caixa Ativa dupla AT-15X2 DATREL conta com duplo woofer de 15 polegadas e driver titânio, com 500W de potência e módulo multimídia (conexão via Bluetooth, entrada para Pendrive, Cartões SD e Rádio FM), tudo controlado por um prático controle remoto que garante autonomia e praticidade em instalações onde não se permite acesso ao módulo multimídia, como, por exemplo, pedestais de parede.",
            "A AT-15X2 conta com entradas tipo P10 que garantem conectividade com equipamentos como DVD, PC, KARAOKE e microfone (com controle independente) perfeita para uso em barzinhos, sem contar que seu gabinete trapezoidal é produzido em MDF, que traz uma maior qualidade e leveza ao produto, essencial na hora do transporte.",
            "Com a caixa ativa dupla AT-15X2 DATREL o sucesso é garantido em dobro!"
        ]
    }
]

# Exportando os dados para JSON
for caixa in caixas_ativas:
    filename = f"caixa_ativa_dupla_{caixa['modelo'].lower()}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(caixa, f, indent=4, ensure_ascii=False)
    print(f"Dados exportados para {filename}")
