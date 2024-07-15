import json

# Dados a serem convertidos
dados = {
    "kits": [
        {
            "nome_kit": "Kit BAS800 + BAS-4X10 + BAS-1X15",
            "descricao": "O Kit BAS800 é um poderoso e versátil rig de baixo que oferece uma ampla gama de opções tonais para qualquer estilo de música. O cabeçote BAS800 fornece 800 watts de potência e possui EQ e controles de compressão para moldar seu som. As caixas BAS-4X10 e BAS-1X15 são projetados para fornecer graves nítidos e fortes com bastante baque de graves. Juntos, eles oferecem um som de baixo poderoso e responsável que corta qualquer mixagem. Esteja você tocando em um pequeno clube ou em um grande palco de festival, o Kit BAS800 tem o poder e a versatilidade de que você precisa para fornecer tons graves de alto nível.",
            "componentes": [
                {
                    "nome": "BAS800",
                    "caracteristicas_tecnicas": {
                        "modelo": "BAS-800",
                        "potencia": "800 W (4 Ohms)",
                        "canais_de_entrada": "02, sendo: (1) HIGH: P10 (Contra Baixo Passivo), (2) LOW: P10 (Contra Baixo Ativo)",
                        "sensibilidade_de_entrada": "LOW e HIGH",
                        "canais_de_saida": "03, sendo: (1) PHONE: Fone de Ouvido (P10 STEREO), (2) LINEOUT: XLR Balanceada, (3) Caixa Passiva: 01 SPEAKON (BAS-4X10 ou BAS-1X15 DATREL) no painel traseiro",
                        "equalizacao_ativa": "03 Vias, sendo: (1) LOW; MID e HIGH",
                        "dimensoes_aproximadas": {
                            "produto": "8,8 x 48,5 x 31 cm",
                            "embalagem": "11 x 52 x 36 cm"
                        },
                        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
                        "padrao_de_fabrica": "pré-ajustado em 220V",
                        "peso": {
                            "liquido": "6,8 Kg",
                            "bruto": "7,4 Kg"
                        }
                    }
                },
                {
                    "nome": "BAS-4X10",
                    "caracteristicas_tecnicas": {
                        "modelo": "BAS-4X10",
                        "potencia": "400 W",
                        "alto_falante": "04 x 10\" (8 Ohms) Cone Alumínio",
                        "entrada": "SPEAKON (8 Ohms)",
                        "tela_metalica_de_protecao_frontal": True,
                        "dimensoes_aproximadas": {
                            "produto": "61 x 65 x 60 cm",
                            "embalagem": "63 x 66 x 61 cm"
                        },
                        "peso": {
                            "liquido": "23,5 Kg",
                            "bruto": "24,7 Kg"
                        }
                    }
                },
                {
                    "nome": "BAS-1X15",
                    "caracteristicas_tecnicas": {
                        "modelo": "BAS-1X15",
                        "potencia": "300 W",
                        "alto_falante": "01 x 15\" (8 Ohms) Cone Alumínio",
                        "entrada": "SPEAKON (8 Ohms)",
                        "tela_metalica_de_protecao_frontal": True,
                        "dimensoes_aproximadas": {
                            "produto": "61 x 65 x 60 cm",
                            "embalagem": "63 x 66 x 61 cm"
                        },
                        "peso": {
                            "liquido": "21,5 Kg",
                            "bruto": "22,7 Kg"
                        }
                    }
                }
            ]
        },
        {
            "nome_kit": "Kit BAS400 + BAS-4X10",
            "descricao": "Combo BAS 400 e 4X10 da DATREL é um sistema de amplificação de baixa frequência que consiste no amplificador BAS 400 e na caixa passiva 4X10 equipado com quatro alto-falantes de 10 polegadas. É uma ótima opção para músicos e bandas que precisam de um sistema de amplificação de baixo portátil e fácil de usar. O amplificador BAS 400 tem potência de 400 watts RMS em 4 Ohms e é equipado com um pré-amplificador de 3 bandas para ajustar o som de acordo com as preferências do usuário. Ele também tem um loop de efeitos e uma saída de linha equilibrada para conexão com mesas de som ou gravação. A caixa passiva 4X10 é equipado com quatro alto-falantes de alumínio de 10 polegadas e é construído em compensado de alta densidade para maior durabilidade e resistência aos impactos. A caixa passiva 4×10 tem uma impedância de 4 Ohms e pode ser conectado diretamente ao amplificador BAS 400 para obter um som potente e de alta qualidade. No geral, o combo BAS 400 e 4X10 da DATREL é uma ótima escolha para quem precisa de um sistema de amplificação de baixo confiável, eficiente e de alta qualidade. Ele é fácil de transportar e pode ser usado em uma variedade de configurações, desde ensaios até shows ao vivo.",
            "componentes": [
                {
                    "nome": "BAS400",
                    "caracteristicas_tecnicas": {
                        "modelo": "BAS-400",
                        "potencia": "400 W (4 Ohms)",
                        "canais_de_entrada": "02, sendo: (1) HIGH: P10 (Contra Baixo Passivo), (2) LOW: P10 (Contra Baixo Ativo)",
                        "sensibilidade_de_entrada": "LOW e HIGH",
                        "canais_de_saida": "03, sendo: (1) PHONE: Fone de Ouvido (P10 STEREO), (2) LINEOUT: XLR Balanceada, (3) Caixa Passiva: 01 SPEAKON (BAS-4X10 ou BAS-1X15 DATREL) no painel traseiro",
                        "equalizacao_ativa": "03 Vias, sendo: (1) LOW; MID e HIGH",
                        "dimensoes_aproximadas": {
                            "produto": "8,8 x 48,5 x 31 cm",
                            "embalagem": "11 x 52 x 36 cm"
                        },
                        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
                        "padrao_de_fabrica": "pré-ajustado em 220V",
                        "peso": {
                            "liquido": "6 Kg",
                            "bruto": "6,6 Kg"
                        }
                    }
                },
                {
                    "nome": "BAS-4X10",
                    "caracteristicas_tecnicas": {
                        "modelo": "BAS-4X10",
                        "potencia": "400 W",
                        "alto_falante": "04 x 10\" (8 Ohms) Cone Alumínio",
                        "entrada": "SPEAKON (8 Ohms)",
                        "tela_metalica_de_protecao_frontal": True,
                        "dimensoes_aproximadas": {
                            "produto": "61 x 65 x 60 cm",
                            "embalagem": "63 x 66 x 61 cm"
                        },
                        "peso": {
                            "liquido": "23,5 Kg",
                            "bruto": "24,7 Kg"
                        }
                    }
                }
            ]
        },
        {
            "nome_kit": "Kit HDSD700 + DA 15300",
            "descricao": "O KIT HDSD-700 de 350W da DATREL é ideal para conectar instrumentos musicais ou ouvir aquela música que tanto gosta. O Amplificador HDSD-700 dispensa o uso de outros meios de amplificação ou pré-amplificadores, conta com saída para 02 caixas acústicas, possui entradas para Guitarra, teclado, DVD, PC, Microfones, Smartphones com fio ou sem fio via conexão Bluetooth com controle remoto, Smart TVs (desde que disponível conexão Bluetooth, para saber consulte manual de instruções da sua TV), o HDSD-700 é perfeito para seus eventos. Junto com o cabeçote vem as Caixa acústica DA 15.300 que forma esse kit sensacional. A DA15.300 é equipada com driver titânio de altíssima qualidade, que proporciona uma ampla resposta de frequência seja qual for a sua aplicação, indicada para o uso nos mais variados amplificadores, sistemas de PA, retorno de palco, monitoração e até sistemas de multi-canais. Sua caixa é construída em madeira com um design robusto e acabamento excelente. O KIT HDSD-700 é excelente para quem busca um conjunto versátil e de alta qualidade para suas apresentações.",
            "componentes": [
                {
                    "nome": "HDSD700",
                    "caracteristicas_tecnicas": {
                        "modelo": "HDSD-700",
                        "potencia": "350 W (4 Ohms)",
                        "canais_de_entrada": "05, sendo: (1) Auxiliar (RCA) e LINE/KEY (P10); (2) Guitarra HIGH/LOW (P10); (3) Módulo Multimídia; e (4 e 5) Microfone (P10)",
                        "controle_de_volume": "Geral e Independente (por canal)",
                        "canais_de_saida": "02, sendo: (1) LINEOUT (P10) e (2) Caixa Passiva 8 Ohms (02 x P10) painel traseiro",
                        "indicacao_de_uso": "* Toca 02 CE-250 DATREL",
                        "dimensoes_aproximadas": {
                            "produto": "12,8 x 46 x 25 cm",
                            "embalagem": "17 x 48 x 28 cm"
                        },
                        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
                        "padrao_de_fabrica": "pré-ajustado em 220V",
                        "peso": {
                            "liquido": "7,2 Kg",
                            "bruto": "7,7 Kg"
                        }
                    }
                },
                {
                    "nome": "DA15300",
                    "caracteristicas_tecnicas": {
                        "modelo": "DA 15.300",
                        "potencia": "300 W",
                        "alto_falante": "15\" (8 Ohms) Cone Alumínio",
                        "driver": "Titanium",
                        "entrada": "02 x P10 (8 Ohms)",
                        "tela_metalica_de_protecao_frontal": True,
                        "dimensoes_aproximadas": {
                            "produto": "56,5 x 40,5 x 40,5 cm",
                            "embalagem": "58 x 42 x 42 cm"
                        },
                        "peso": {
                            "liquido": "11,2 Kg",
                            "bruto": "12,3 Kg"
                        }
                    }
                }
            ]
        },
        {
            "nome_kit": "Kit HDSD500 + CE250",
            "descricao": "O KIT HDSD500 Com sua ampla gama de conexões e tecnologia avançada, o HDSD-500 é ideal para amantes da música em geral. Além disso, sua potência de 250W garante um som potente e de qualidade, tornando-o perfeito para eventos e apresentações ao vivo. Seu design compacto e leve torna-o fácil de transportar e configurar, e sua tecnologia sem cooler garante um funcionamento silencioso e sem interrupções, mesmo durante longas sessões de uso. As duas caixas passiva CE12-250 DATREL são caixas de som de alta qualidade, com potência de 250W RMS cada uma. Elas possuem duas vias e woofer de 12 polegadas, proporcionando uma excelente qualidade de som e potência sonora. Se você procura um amplificador versátil, potente e de alta qualidade, o KIT HDSD-500 DATREL é a escolha certa para você!",
            "componentes": [
                {
                    "nome": "HDSD500",
                    "caracteristicas_tecnicas": {
                        "modelo": "HDSD-500",
                        "potencia": "250 W",
                        "versoes": "Bluetooth (Acompanha Controle Remoto do Módulo)",
                        "canais_de_entrada": "05, sendo: (1) Auxiliar (RCA) e LINE/KEY (P10); (2) Guitarra HIGH/LOW (P10); (3) Módulo Multimídia e (4 e 5) Microfone (P10)",
                        "controle_de_volume": "Geral e Independente (por canal)",
                        "canais_de_saida": "02, sendo: (1) LINEOUT (P10) e (2) Caixa Passiva 8 Ohms (02 x P10) painel traseiro",
                        "indicacao_de_uso": "* Toca 02 CE-250 DATREL",
                        "dimensoes_aproximadas": {
                            "produto": "12,8 x 46 x 25 cm",
                            "embalagem": "17 x 48 x 28 cm"
                        },
                        "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
                        "padrao_de_fabrica": "pré-ajustado em 220V",
                        "peso": {
                            "liquido": "7,2 Kg",
                            "bruto": "7,7 Kg"
                        }
                    }
                },
                {
                    "nome": "CE250",
                    "caracteristicas_tecnicas": {
                        "modelo": "CE-250",
                        "potencia": "250 W",
                        "alto_falante": "12\" e TWEETER ou Driver Titânio",
                        "sistema_2_em_1": "Pedestal ou Retorno",
                        "divisor_de_frequencia": "01 via",
                        "canal_de_entrada": "02 x P10 (8 Ohms)",
                        "tela_metalica_de_protecao_frontal": True,
                        "suporte_para_pedestal": True,
                        "dimensoes_aproximadas": {
                            "produto": "56,5 x 40,5 x 40,5 cm",
                            "embalagem": "58 x 42 x 42 cm"
                        },
                        "peso": {
                            "liquido": "11,2 Kg",
                            "bruto": "12,3 Kg"
                        }
                    }
                }
            ]
        }
    ]
}

# Convertendo para JSON
json_data = json.dumps(dados, indent=4, ensure_ascii=False)

# Imprimindo o JSON formatado
print(json_data)
