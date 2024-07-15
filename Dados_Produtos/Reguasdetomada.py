import json

# Dados da Régua de Tomada DA-5.000
dados_regua_da5000 = {
    "nome": "Régua de Tomada DA-5.000",
    "descricao": "A RÉGUA DE TOMADA DA-5000 oferece uma potência de 5000 Watts e possui uma alta proteção de disjuntor de segurança. Ele vem com um suporte de fixação para facilitar a instalação.\n\nO disjuntor incluso é de 32A, proporcionando proteção adequada para o equipamento.\n\nA Régua conta com 8 tomadas de saída e 1 tomada de serviço, permitindo que você conecte vários dispositivos simultaneamente. As tomadas de saída possuem capacidade de até 20A cada e estão dispostas na vertical, o que facilita a organização dos cabos e evita emaranhados.\n\nCom a RÉGUA DE TOMADA DA-5000, você terá um sistema seguro e eficiente para alimentar seus dispositivos elétricos.",
    "caracteristicas_tecnicas": {
        "modelo": "DA-5.000",
        "padrao_rack": "DA-5.000",
        "amperagem_disjuntor": "32 A",
        "tomadas_saida": 8,
        "tomada_servico": 1,
        "potencia_110v": "3200 W",
        "potencia_220v": "5600 W",
        "dimensoes_aproximadas": {
            "produto": "5,7 x 48,26 x 42,9 x 12,3 cm",
            "embalagem": "8 x 55 x 20 cm"
        },
        "indicador_tensao": "110/220 Volts (por leds)",
        "peso": {
            "liquido": "1,8 Kg",
            "bruto": "2,1 Kg"
        }
    }
}

# Dados da Régua de Tomada DA-4.000
dados_regua_da4000 = {
    "nome": "Régua de Tomada DA-4.000",
    "descricao": "A RÉGUA DE TOMADA DA-4000 oferece uma potência em 127V de 4000 Watts e em 220v 4.400 Watts, possui uma alta proteção de disjuntor de segurança. Ele vem com um suporte de fixação para facilitar a instalação.\n\nO disjuntor incluso é de 25A, proporcionando proteção adequada para o equipamento.\n\nA Régua conta com 8 tomadas de saída e 1 tomada de serviço, permitindo que você conecte vários dispositivos simultaneamente. As tomadas de saída possuem capacidade de até 20A cada e estão dispostas na vertical, o que facilita a organização dos cabos e evita emaranhados.\n\nCom a RÉGUA DE TOMADA DA-4000, você terá um sistema seguro e eficiente para alimentar seus dispositivos elétricos.",
    "caracteristicas_tecnicas": {
        "modelo": "DA-4.000",
        "padrao_rack": "19”",
        "amperagem_disjuntor": "25 A",
        "tomadas_saida": 8,
        "tomada_servico": 1,
        "potencia_110v": "2500 W",
        "potencia_220v": "4400 W",
        "dimensoes_aproximadas": {
            "produto": "5,7 x 48,26 x 42,9 x 12,3 cm",
            "embalagem": "8 x 55 x 20 cm"
        },
        "indicador_tensao": "110/220 Volts (por leds)",
        "peso": {
            "liquido": "1,8 Kg",
            "bruto": "2,1 Kg"
        }
    }
}

# Combinando os dados das duas réguas em uma lista
dados_reguas = [dados_regua_da5000, dados_regua_da4000]

# Convertendo os dados para JSON
json_dados = json.dumps(dados_reguas, indent=4, ensure_ascii=False)

# Salvando em um arquivo JSON
with open("dados_reguas.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(json_dados)

print("Dados das Régua de Tomada DA-5.000 e DA-4.000 convertidos e salvos em dados_reguas.json")
