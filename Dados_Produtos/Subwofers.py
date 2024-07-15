import json

# Dados das caixas subwoofer já existentes
dados_swa400 = {
    "nome": "Caixa Subwoofer Ativo DATREL SWA-400",
    "descricao": "Um sistema de som super profissional é equilibrado entre agudos, médios e graves, mas é geralmente o Subwoofer responsável pelas frequências mais baixas, foi nessa regra que a DATREL desenvolveu o SWA-400, um moderníssimo Subwoofer Ativo de 15 polegadas e 400W de potência. O SWA-400 tem ajuste de ganho e frequência, com resposta de trabalho de 30Hz a 300Hz, saída para caixa escrava 8 Ohms, conta com alça lateral para transporte e suporte para pedestal. SWA-400 o Subwoofer de quem gosta de potência e graves impactantes. Reproduza suas músicas com impacto e qualidade que só a DATREL tem!",
    "caracteristicas_tecnicas": {
        "modelo": "SWA-400",
        "potencia": "400 W",
        "alto_falante": "15\" (8 Ohms)",
        "impedancia_entrada": "LINE: 5K Ohms",
        "sensibilidade_entrada": "LINE: 500 mV",
        "canais_entrada": "LINE (P10)",
        "canais_saida": "Saída Escrava 8 Ohms (P10)",
        "tela_protecao": True,
        "suporte_pedestal": True,
        "dimensoes_produto": {
            "altura": "62 cm",
            "largura": "50 cm",
            "profundidade": "60 cm"
        },
        "dimensoes_embalagem": {
            "altura": "64 cm",
            "largura": "53 cm",
            "profundidade": "62 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "peso_liquido": "36 Kg",
        "peso_bruto": "37,8 Kg"
    }
}

dados_sw400 = {
    "nome": "Caixa Subwoofer Passivo DATREL SW-400",
    "descricao": "O SW-400 DATREL, Subwoofer Passivo AF de 15 polegadas e 400W de potência, desenvolvido para ser usado preferencialmente em conjunto com o Subwoofer Ativo SWA400, mas suas características proporcionam uma usabilidade excelente em amplificadores de potência, cabeçotes ou como você preferir, desde que seja aplicado potência e cortes necessários para extrair o máximo rendimento do Subwoofer. O SW400 é indispensável na composição de um sistema de som, com resposta de frequência de 30Hz até 300Hz. O SW400 conta com alça lateral para transporte e suporte para pedestal. SW400 DATREL, com ele seus graves é garantido!",
    "caracteristicas_tecnicas": {
        "modelo": "SW-400",
        "potencia": "400 W",
        "alto_falante": "15\" (8 Ohms)",
        "canais_entrada": "SPEAKON (8 Ohms)",
        "tela_protecao": True,
        "suporte_pedestal": True,
        "dimensoes_produto": {
            "altura": "62 cm",
            "largura": "50 cm",
            "profundidade": "60 cm"
        },
        "dimensoes_embalagem": {
            "altura": "64 cm",
            "largura": "53 cm",
            "profundidade": "62 cm"
        },
        "peso_liquido": "28,7 Kg",
        "peso_bruto": "30,5 Kg"
    }
}

dados_swa300 = {
    "nome": "Caixa Subwoofer Ativo DATREL SWA-300",
    "descricao": "Um sistema de som super profissional é equilibrado entre agudos, médios e graves, mas é geralmente o Subwoofer responsável pelas frequências mais baixas, foi nessa regra que a DATREL desenvolveu o SWA-400, um moderníssimo Subwoofer Ativo de 15 polegadas e 400W de potência. O SWA-400 tem ajuste de ganho e frequência, com resposta de trabalho de 30Hz a 300Hz, saída para caixa escrava 8 Ohms, conta com alça lateral para transporte e suporte para pedestal. SWA-400 o Subwoofer de quem gosta de potência e graves impactantes. Reproduza suas músicas com impacto e qualidade que só a DATREL tem!",
    "caracteristicas_tecnicas": {
        "modelo": "SWA-300",
        "potencia": "300 W",
        "alto_falante": "12\" (8 Ohms)",
        "impedancia_entrada": "LINE: 5K Ohms",
        "sensibilidade_entrada": "LINE: 500 mV",
        "canais_entrada": "LINE (P10)",
        "canais_saida": "Saída Escrava 8 Ohms (P10)",
        "tela_protecao": True,
        "suporte_pedestal": True,
        "dimensoes_produto": {
            "altura": "40 cm",
            "largura": "40 cm",
            "profundidade": "52 cm"
        },
        "dimensoes_embalagem": {
            "altura": "44 cm",
            "largura": "43 cm",
            "profundidade": "54 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "peso_liquido": "20,2 Kg",
        "peso_bruto": "21,4 Kg"
    }
}

dados_sw300 = {
    "nome": "Caixa Subwoofer Passivo DATREL SW300",
    "descricao": "Sub Woofer Passivo SW-300 da Datrel, que proporciona uma maior pureza sonora e incrível clareza dos graves. Com alto falante de 12″ polegadas e 300 Watts de potência, garantem toda a qualidade que seu evento e/ou suas apresentações merecem. O modelo é robusta resistente, essa caixa de som possui gabinete produzido em madeira MDF. Utilizável em Bandas, Shows, Igrejas, Barzinhos. Grave com pureza e clareza sonora. Possui furação (base) para encaixe de Tripé e alça de transporte. Caixa em Madeira MDF.",
    "caracteristicas_tecnicas": {
        "modelo": "SW300",
        "potencia": "300 W",
        "alto_falante": "12\" (8 Ohms)",
        "canais_entrada": "P10 (8 Ohms)",
        "tela_protecao": True,
        "suporte_pedestal": True,
        "dimensoes_produto": {
            "altura": "40 cm",
            "largura": "40 cm",
            "profundidade": "52 cm"
        },
        "dimensoes_embalagem": {
            "altura": "44 cm",
            "largura": "43 cm",
            "profundidade": "54 cm"
        },
        "peso_liquido": "16,5 Kg",
        "peso_bruto": "17,7 Kg"
    }
}

# Juntando os dados em uma lista
caixas_subwoofer = [dados_swa400, dados_sw400, dados_swa300, dados_sw300]

# Convertendo para JSON
json_caixas_subwoofer = json.dumps(caixas_subwoofer, ensure_ascii=False, indent=4)

# Imprimindo o JSON resultante
print(json_caixas_subwoofer)
