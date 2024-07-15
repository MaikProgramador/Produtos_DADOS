import json

# Dados dos amplificadores
amplificadores_multiuso = [
    {
        "modelo": "HDSD-500",
        "potencia": "250 W",
        "conectividade": "Bluetooth, Pendrive, Rádio FM",
        "canaisEntrada": {
            "01": "Auxiliar (RCA) e LINE/KEY (P10)",
            "02": "Guitarra HIGH/LOW (P10)",
            "03": "Módulo Multimídia",
            "04 e 05": "Microfone (P10)"
        },
        "controleVolume": "Geral e Independente (por canal)",
        "canaisSaida": {
            "01": "LINEOUT (P10)",
            "02": "Caixa Passiva 8 Ohms (02 x P10) painel traseiro"
        },
        "indicacaoUso": [
            "Toca 02 CE-250 DATREL"
        ],
        "dimensoesProduto": {
            "altura": "12,8 cm",
            "largura": "46 cm",
            "profundidade": "25 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "17 cm",
            "largura": "48 cm",
            "profundidade": "28 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "pesoLiquido": "7,2 Kg",
        "pesoBruto": "7,7 Kg",
        "sobre": [
            "O Cabeçote Amplificador HDSD-500 de 250W da DATREL é ideal para conectar instrumentos musicais ou ouvir aquela música que tanto gosta.",
            "O Amplificador HDSD-500 dispensa o uso de outros meios de amplificação ou pré-amplificadores, conta com saída para 02 caixas acústicas, possui entradas para Guitarra, teclado, DVD, PC, Microfones, Smartphones com fio ou sem fio via conexão Bluetooth com controle remoto, Smart TVs (desde que disponível conexão Bluetooth, para saber consulte manual de instruções da sua TV), o HDSD-500 é perfeito para seus eventos.",
            "Além disso, o HDSD-500 possui conexão de Pendrive e Rádio FM, que garante uma ótima aplicação em uso doméstico.",
            "O HDSD-500 é leve, robusto e silencioso, pois não utiliza cooler de ventilação por ser um Amplificador moderno que consegue entregar toda sua potência sem danificar seus componentes com superaquecimento.",
            "O HDSD-500 é perfeito para nossas caixas acústicas CE 12.250 da DATREL, pois trazem as especificações ideais para o rendimento do Amplificador.",
            "Procurando o melhor Amplificador Multiúso? O HDSD-500 DATREL, a escolha certa!"
        ]
    },
    {
        "modelo": "HDSD-700",
        "potencia": "350 W",
        "conectividade": "Bluetooth, Pendrive, Rádio FM",
        "canaisEntrada": {
            "01": "Auxiliar (RCA) e LINE/KEY (P10)",
            "02": "Guitarra HIGH/LOW (P10)",
            "03": "Contra Baixo (P10)",
            "04": "Módulo Multimídia",
            "05 e 06": "Microfone (P10)"
        },
        "controleVolume": "Geral e Independente (por canal)",
        "canaisSaida": {
            "01": "LINEOUT (P10)",
            "02": "Caixa Passiva 8 Ohms (02 x P10) painel traseiro"
        },
        "indicacaoUso": [
            "Toca 02 CE-250 DATREL"
        ],
        "dimensoesProduto": {
            "altura": "12,8 cm",
            "largura": "52,5 cm",
            "profundidade": "25 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "17 cm",
            "largura": "54 cm",
            "profundidade": "28 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "7,6 Kg",
        "pesoBruto": "8,1 Kg",
        "sobre": [
            "O Cabeçote Amplificador HDSD-700 de 350W da DATREL é ideal para conectar instrumentos musicais ou ouvir aquela música que tanto gosta.",
            "O Amplificador HDSD-700 dispensa o uso de outros meios de amplificação ou pré-amplificadores, conta com saída para 02 caixas acústicas, possui entradas para Guitarra, teclado, DVD, PC, Microfones, Smartphones com fio ou sem fio via conexão Bluetooth com controle remoto, Smart TVs (desde que disponível conexão Bluetooth, para saber consulte manual de instruções da sua TV), o HDSD-700 é perfeito para seus eventos.",
            "Além disso, o HDSD-700 possui conexão de Pendrive e Rádio FM, que garante uma ótima aplicação em uso doméstico.",
            "O HDSD-700 é leve, robusto e silencioso, pois não utiliza cooler de ventilação por ser um Amplificador moderno que consegue entregar toda sua potência sem danificar seus componentes com superaquecimento.",
            "O HDSD-700 é perfeito para nossas caixas acústicas DA15-300 da DATREL, pois trazem as especificações ideais para o rendimento do Amplificador.",
            "Procurando o melhor Amplificador Multiúso? O HDSD-700 DATREL, a escolha certa!"
        ]
    }
]

# Exportando para JSON
with open('amplificadores_multiuso_datrel.json', 'w', encoding='utf-8') as f:
    json.dump(amplificadores_multiuso, f, indent=4, ensure_ascii=False)

print("Dados exportados para amplificadores_multiuso_datrel.json")
