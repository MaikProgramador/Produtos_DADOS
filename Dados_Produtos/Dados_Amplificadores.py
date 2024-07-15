import json

# Dados dos amplificadores
amplificadores = [
    {
        "modelo": "PA-20.0",
        "potencia": "2.000 W (1.000 por canal)",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "BORN",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "Canais Independentes",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 12\", 15\" ou 18\" (500 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "41,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "11 cm",
            "largura": "52 cm",
            "profundidade": "44 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "11,7 Kg",
        "pesoBruto": "12,4 Kg",
        "sobre": [
            "O Amplificador de Potência PA-20.0 DATREL conta com 2000W de potência, e tecnologia Toroidal que entrega uma melhor eficiência energética para seus componentes proporcionando o máximo rendimento possível.",
            "O PA-20.0 pode ser amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para DJS, eventos como festas em geral, igrejas, palestras, convenções, casa de shows, auditórios e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas graças ao seu sistema de ventilação forçada.",
            "O Amplificador PA-20.0 DATREL conta com sistema de proteção contra curto-circuito acidental nos canais de saída, com indicação por LEDs (verde que indica presença de sinal, e vermelho que indica CLIP e OVERLOAD) e controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Potência e qualidade para seu evento? DATREL é a escolha!"
        ]
    },
    {
        "modelo": "PA-10.000",
        "potencia": "1.000 W",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "BORN",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "Canais Independentes",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 10\", 12\" ou 15\" (250 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "41,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "11 cm",
            "largura": "52 cm",
            "profundidade": "44 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "9,2 Kg",
        "pesoBruto": "9,9 Kg",
        "sobre": [
            "O Amplificador de Potência PA-10.000 DATREL conta com 1000W de potência, sendo amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para eventos como festas em geral, igrejas, palestras, convenções, casa de shows, auditórios, DJS e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas graças ao seu sistema de ventilação forçada.",
            "O Amplificador PA-10.000 DATREL conta com sistema de proteção contra curto-circuito acidental nos canais de saída, com indicação por LEDs (verde que indica presença de sinal, e vermelho que indica CLIP e OVERLOAD) e controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Quer potência e qualidade para seu evento? DATREL é a escolha!"
        ]
    },
    {
        "modelo": "PA-8.000",
        "potencia": "800 W em 4 Ohms (400 por canal)",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "BORN",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "Canais Independentes",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 10\", 12\" ou 15\" (200 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "41,5 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "11 cm",
            "largura": "52 cm",
            "profundidade": "44 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "9 Kg",
        "pesoBruto": "9,7 Kg",
        "sobre": [
            "O Amplificador de Potência PA-8.000 DATREL conta com 800W de potência, sendo amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para eventos como festas em geral, igrejas, palestras, convenções, casa de shows, auditórios, DJS e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas graças ao seu sistema de ventilação forçada.",
            "O Amplificador PA-8.000 DATREL conta com sistema de proteção contra curto-circuito acidental nos canais de saída, com indicação por LEDs (verde que indica presença de sinal, e vermelho que indica CLIP e OVERLOAD) e controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Potência e qualidade para seu evento? DATREL é a escolha!"
        ]
    },
    {
        "modelo": "PA-5.000",
        "potencia": "600 W",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "04 JACK P10",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "Canais Independentes",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 8\", 10\" ou 12\" (150 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "33 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "33 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "7,3 Kg",
        "pesoBruto": "7,9 Kg",
        "sobre": [
            "O Amplificador de Potência PA-5.000 DATREL conta com 600W de potência, sendo amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para eventos como festas em geral, igrejas, palestras, convenções, casa de shows, auditórios, DJS e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas graças ao seu sistema de ventilação forçada.",
            "O Amplificador PA-5.000 DATREL conta com sistema de proteção contra curto-circuito acidental nos canais de saída, com indicação por LEDs (verde que indica presença de sinal, e vermelho que indica CLIP e OVERLOAD) e controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Potência e qualidade para seu evento? DATREL é a escolha!"
        ]
    },
    {
        "modelo": "PA-3.000",
        "potencia": "400 W",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "04 JACK P10",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "LINE: 775 mV",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 8\", 10\" ou 12\" (100 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "33 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "33 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "6,4 Kg",
        "pesoBruto": "7 Kg",
        "sobre": [
            "O Amplificador de Potência PA-3.000 DATREL conta com 400W de potência, sendo amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para eventos como festas em geral, igrejas, palestras, convenções, casa de shows, DJS, auditórios e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas graças ao seu sistema de ventilação forçada.",
            "O Amplificador PA-3.000 DATREL conta com sistema de proteção contra curto-circuito acidental nos canais de saída, controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Potência e qualidade para seu evento? DATREL é a escolha!"
        ]
    },
    {
        "modelo": "PA-1.800",
        "potencia": "300 W",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "04 JACK P10",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "Canais Independentes",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 8\" ou 10\" (75 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "33 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "11 cm",
            "largura": "52 cm",
            "profundidade": "36 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "5,9 Kg",
        "pesoBruto": "6,5 Kg",
        "sobre": [
            "O Amplificador de Potência PA-1.800 DATREL conta com 300W de potência, sendo amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para eventos como festas em geral, igrejas, palestras, convenções, casa de shows, auditórios, DJS e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas.",
            "O Amplificador PA-1.800 DATREL conta com sistema de proteção contra curto circuito acidental nos canais de saída, controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Potência e qualidade para seu evento? DATREL é a escolha!"
        ]
    },
    {
        "modelo": "PA-1.200",
        "potencia": "200 W",
        "conectoresEntradaSaidaSinal": "P10",
        "conectoresSaida": "04 JACK P10",
        "sensibilidadeEntrada": "LINE: 775 mV",
        "controleVolume": "Canais Independentes",
        "indicacaoUso": "FULL-RANGE: 04 Caixas Acústicas com AF de 8\" ou 10\" (50 W por alto falante); 02 por canal em paralelo",
        "dimensoesProduto": {
            "altura": "8,8 cm",
            "largura": "48,5 cm",
            "profundidade": "33 cm"
        },
        "dimensoesEmbalagem": {
            "altura": "11 cm",
            "largura": "52 cm",
            "profundidade": "36 cm"
        },
        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
        "padraoFabrica": "pré-ajustado em 220V",
        "pesoLiquido": "5,5 Kg",
        "pesoBruto": "6,2 Kg",
        "sobre": [
            "O Amplificador de Potência PA-1.200 DATREL conta com 200W de potência, sendo amplamente usado em sistemas de som profissionais com aplicações nas mais diversas áreas, com resposta de frequência FULL RANGE excelente opção para eventos como festas em geral, igrejas, palestras, convenções, casa de shows, auditórios, DJS e projetos de sonorização de pequeno, médio e grande porte onde se exige qualidade e desempenho por longas horas.",
            "O Amplificador PA-1.200 DATREL conta com sistema de proteção contra curto-circuito acidental nos canais de saída, controle independente dos canais A e B que garante uma melhor calibragem na entrega do canal.",
            "Potência e qualidade para seu evento? PA1.200 DATREL é a escolha!"
        ]
    }
]

# Exportando para JSON
with open('amplificadores_datrel.json', 'w', encoding='utf-8') as f:
    json.dump(amplificadores, f, indent=4, ensure_ascii=False)

print("Dados exportados para amplificadores_datrel.json")
