import json

# Dados dos Cubos de Guitarra DATREL

# Cubo Guitar 1X12
cubo_guitar_1x12 = {
    "modelo": "GUITAR 1x12",
    "descricao": "O Cubo de Guitarra GUITAR1x12 profissional é projetado para oferecer um som de alta qualidade para músicos exigentes. Com sua potência de 150 Watts e alto falante de 12 polegadas, ele é capaz de entregar um som poderoso e claro.",
    "caracteristicas_tecnicas": {
        "potencia": "150 W",
        "alto_falante": "12\" (4 Ohms)",
        "saida_phone": "P10 MONO",
        "saida_line_out": "P10 MONO",
        "canais_entrada": "P10",
        "fusivel_reposicao": "2A",
        "dimensoes": {
            "produto": "51 x 52,5 x 23 cm",
            "embalagem": "53,5 x 53,5 x 28,5 cm",
            "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
            "peso": {
                "liquido": "17 Kg",
                "bruto": "17,5 Kg"
            }
        }
    }
}

# Cubo Guitar 2X8
cubo_guitar_2x8 = {
    "modelo": "GUITAR 2X8",
    "descricao": "O GUITAR2x8 possui um design compacto e moderno, facilitando o transporte e a utilização em diferentes ambientes. Com uma potência de 100W e dois alto-falantes de 8 polegadas cada, oferece um som limpo e potente, ideal para músicos profissionais e amadores.",
    "caracteristicas_tecnicas": {
        "potencia": "100 W",
        "alto_falante": "2X8 (4 Ohms)",
        "saida_phone": "P10 MONO",
        "saida_line_out": "P10 MONO",
        "canais_entrada": "P10",
        "fusivel_reposicao": "2A",
        "dimensoes": {
            "produto": "51 x 52,5 x 23 cm",
            "embalagem": "42 x 53,5 x 28,5 cm",
            "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
            "peso": {
                "liquido": "15,7 Kg",
                "bruto": "16,2 Kg"
            }
        }
    }
}

# Cubo Guitar-30
cubo_guitar_30 = {
    "modelo": "GUITAR-30",
    "descricao": "É sempre bom encontrar produtos de qualidade para iniciantes, principalmente quando se trata de um instrumento musical como a guitarra. O Cubo de Guitarra GUITAR30 oferece boa qualidade de som, fácil utilização e recursos ideais para ensaios e aulas.",
    "caracteristicas_tecnicas": {
        "potencia": "30 W",
        "alto_falante": "8\" (8 Ohms) Cone Papel",
        "canal_entrada": "Entrada para Guitarra",
        "saida_phone": "P10 STEREO para fone de ouvido",
        "ajustes": {
            "distorcao": "GAIN, BOOST SELECT e LEVEL",
            "equalizacao": "BASS, MIDLE e TREBLE"
        },
        "tela_protecao": "Metálica frontal",
        "dimensoes": {
            "produto": "33,5 x 32,5 x 17,5 cm",
            "embalagem": "35 x 34 x 19 cm",
            "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
            "peso": {
                "liquido": "6,5 Kg",
                "bruto": "7,0 Kg"
            }
        }
    }
}

# Lista de todos os cubos
cubos_guitarra_datrel = [cubo_guitar_1x12, cubo_guitar_2x8, cubo_guitar_30]

# Convertendo para JSON
json_data = json.dumps(cubos_guitarra_datrel, indent=2, ensure_ascii=False)
print(json_data)
