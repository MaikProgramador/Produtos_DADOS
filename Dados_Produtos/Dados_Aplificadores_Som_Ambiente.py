import json

# Dados dos amplificadores
amplificadores_ambiente = [
    {
        "modelo": "HDSD-200",
        "potencia": "200 W - 4 Ohms",
        "conectividade": "Bluetooth, Pendrive, Rádio FM",
        "entradaMicrofone": "P10",
        "impedanciaEntrada": {
            "LINE": "5K Ohms",
            "MIC": "600 Ohms"
        },
        "sensibilidadeEntrada": {
            "LINE": "500mV",
            "MIC": "35 mV"
        },
        "canaisEntrada": "02 (Microfone P10, Módulo Multimídia)",
        "inputs": "AUX 1 e AUX 2 (RCA)",
        "lineout": "RCA (STEREO)",
        "outputs": "02 x P10 (8 Ohms)",
        "indicacaoUso": [
            "Toca 02 AF 8\" ou 10\" de 100 W - 8 Ohms",
            "Toca 08 AF 4\" ou 6\" de 25 W - 8 Ohms"
        ],
        "dimensoesProduto": {
            "altura": "7,5 cm",
            "largura": "20,3 cm",
            "profundidade": "24,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "10 cm",
            "largura": "22 cm",
            "profundidade": "28 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "3 Kg",
        "pesoBruto": "3,2 Kg",
        "sobre": [
            "O Amplificador HDSD-200 de 200W da DATREL é ideal para sonorização de ambientes diversos, oferecendo conectividade Bluetooth, Pendrive e Rádio FM. Compacto e silencioso, é perfeito para uso profissional ou doméstico."
        ]
    },
    {
        "modelo": "HDSD-100",
        "potencia": "100 W (4 Ohms)",
        "conectividade": "Bluetooth, Pendrive, Rádio FM",
        "entradaMicrofone": "P10",
        "impedanciaEntrada": "LINE e MIC",
        "sensibilidadeEntrada": "LINE e MIC",
        "canaisEntrada": "03 (Microfone P10, Módulo Multimídia, AUX 1 e AUX 2)",
        "canaisSaida": "03 (LINEOUT RCA, OUTPUTS 02 x P10)",
        "indicacaoUso": [
            "Toca 02 AF 8\" ou 10\" de 50 W (8 Ohms)",
            "Toca 04 AF 6\" ou 8\" de 25 W (8 Ohms)",
            "Toca 08 AF 4\" ou 6\" de 12 W (8 Ohms)"
        ],
        "dimensoesProduto": {
            "altura": "7,5 cm",
            "largura": "20,3 cm",
            "profundidade": "24,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "10 cm",
            "largura": "22 cm",
            "profundidade": "28 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "3 Kg",
        "pesoBruto": "3,2 Kg",
        "sobre": [
            "O Amplificador HDSD-100 de 100W da DATREL é ideal para sonorização de ambientes diversos, oferecendo conectividade Bluetooth, Pendrive e Rádio FM. Compacto e silencioso, é perfeito para uso profissional ou doméstico."
        ]
    }
]

# Exportando para JSON
with open('amplificadores_hd_datrel.json', 'w', encoding='utf-8') as f:
    json.dump(amplificadores_ambiente, f, indent=4, ensure_ascii=False)

print("Dados exportados para amplificadores_hd_datrel.json")
