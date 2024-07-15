import json

# Dados do Combo Completo Vertical Line DATREL KSWA300-VOX4.0 + SW300
kswa300_vox40_sw300 = {
    "nome": "Combo Completo Vertical Line DATREL KSWA300-VOX4.0 + SW300",
    "descricao": "O modelo KSWA300 é um sistema de som com potência de 300 W e um alto-falante de 12 polegadas com impedância de 8 Ohms. Ele possui entradas e saídas para conexão de dispositivos de áudio, como players ou microfones, com opções de conexão P10 mono e XLR fêmea balanceada. Os controles do subwoofer incluem ajuste de volume e frequência de corte, além de saída para conexão com caixa passiva por meio de uma entrada P10 de 8 Ohms. Já os controles do módulo de voz incluem uma entrada de linha P10, uma entrada de microfone P10 de 8 Ohms e ajustes de graves, médios e agudos. O sistema também possui saídas, incluindo uma saída balanceada XLR para linha e uma saída P10 de 8 Ohms para caixa passiva. Além disso, o alto-falante possui uma tela metálica de proteção frontal e suporte para pedestal. O modelo também é equipado com tecnologia Bluetooth e acompanha controle remoto para o módulo.",
    "caracteristicas_tecnicas": {
        "modelo": "KSWA300-VOX4.0",
        "versoes": "Bluetooth (Acompanha Controle Remoto do Módulo)",
        "potencia": "300 W",
        "alto_falante": "12” (8 Ohms)",
        "impedancia_entrada": "LINE: 5K Ohms",
        "sensibilidade_entrada": "LINE: 500 mV",
        "controles_subwoofer": {
            "saída_lineout": "XLR (Balanceada)",
            "entradas": [
                "P10 Mono",
                "XLR Fêmea (Balanceada)"
            ],
            "ajustes": "Volume e FC (Frequência de Corte)",
            "saida_slaveout": "P10 (8 Ohms) para caixa passiva"
        },
        "controles_vox": {
            "entrada_line": "P10",
            "entrada_microfone": "P10 (8 Ohms)",
            "controle_volume": "Módulo Multimidia e Microfone",
            "ajustes": "Grave, Médio e Agudo",
            "saidas": [
                "LINEOUT: XLR",
                "Caixa Passiva: P10 (8 Ohms)"
            ]
        },
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
        "padrao_fabrica": "pré-ajustado em 220V",
        "peso_liquido": "23 Kg",
        "peso_bruto": "24,2 Kg"
    }
}

# Dados do Combo Completo Vertical Line DATREL KSWA-400 + VOX4.0
kswa400_vox40 = {
    "nome": "Combo Completo Vertical Line DATREL KSWA-400 + VOX4.0",
    "descricao": "O modelo KSWA400 é um sistema de som com potência de 400 W e um alto-falante de 15 polegadas com impedância de 8 Ohms. Ele possui entradas e saídas para conexão de dispositivos de áudio, como players ou microfones, com opções de conexão P10 mono e XLR fêmea balanceada. Os controles do subwoofer incluem ajuste de volume e frequência de corte, além de saída para conexão com caixa passiva por meio de uma entrada P10 de 8 Ohms. Já os controles do módulo de voz incluem uma entrada de linha P10, uma entrada de microfone P10 de 8 Ohms e ajustes de graves, médios e agudos. O sistema também possui saídas, incluindo uma saída balanceada XLR para linha e uma saída P10 de 8 Ohms para caixa passiva. Além disso, o alto-falante possui uma tela metálica de proteção frontal e suporte para pedestal. O modelo também é equipado com tecnologia Bluetooth e acompanha controle remoto para o módulo.",
    "caracteristicas_tecnicas": {
        "modelo": "KSWA-400",
        "versoes": "Bluetooth (Acompanha Controle Remoto do Módulo)",
        "potencia": "400 W",
        "alto_falante": "15” (8 Ohms)",
        "impedancia_entrada": "LINE: 5K Ohms",
        "sensibilidade_entrada": "LINE: 500 mV",
        "canais_entrada": [
            "01 P10",
            "01 XLR Fêmea"
        ],
        "canais_saida": [
            "Saída Escrava 8 Ohms (P10)",
            "01 LINEOUT XRL Macho"
        ],
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
        "padrao_fabrica": "pré-ajustado em 220V",
        "peso_liquido": "36 Kg",
        "peso_bruto": "37,8 Kg"
    }
}

# Convertendo para JSON e exibindo
json_kswa300_vox40_sw300 = json.dumps(kswa300_vox40_sw300, indent=2, ensure_ascii=False)
json_kswa400_vox40 = json.dumps(kswa400_vox40, indent=2, ensure_ascii=False)

print("Dados do Combo Completo Vertical Line DATREL KSWA300-VOX4.0 + SW300:")
print(json_kswa300_vox40_sw300)

print("\nDados do Combo Completo Vertical Line DATREL KSWA-400 + VOX4.0:")
print(json_kswa400_vox40)
