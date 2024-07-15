import json

# Dados existentes
dados = {
    "monitores_retornos": [
        {
            "nome": "Monitor/Retorno de Palco Ativo DATREL AT12-250",
            "descricao": "O Monitor de Palco Ativo 12′ 250 Watts MA 12-250, foi desenvolvido para atender as necessidades dos profissionais mais exigentes, imprimindo som potente e com qualidade. Ideal para ser utilizado em estúdios de gravações ou apresentações no palco, esse modelo possui falante de12 polegadas e atinge potencia máxima de 250 Watts RMS. Conta com designe discreto, possui tela metálica frontal, que protege o equipamento, garantindo maior durabilidade. Dispõe de equalização em 3 vias, divisor de frequência de 1 via, Canais de Line e Microfone P10 independentes, saída line out XLR e escrava P10 8 Ohms.",
            "caracteristicas_tecnicas": {
                "modelo": "AT12-250 Monitor",
                "versoes": "Normal ou Bluetooth (Acompanha Controle Remoto do Modulo)",
                "potencia": "250 W",
                "alto_falante": "12\" e TWEETER ou Driver Titânio",
                "sistema_2_em_1": "Pedestal ou Retorno",
                "impedancia_de_entrada": "LINE: 5K Ohms, MIC: 200-600 Ohms",
                "equalizacao_ativa": "03 vias, sendo: Agudo, Médio e Grave",
                "divisor_de_frequencia": "01 via",
                "canais_de_entrada": "02, sendo: (1) LINE (P10) e (2) Microfone (P10)",
                "controle_de_volume": "USB/Sinal e Microfone",
                "canais_de_saida": "02, sendo: (1) LINEOUT (XLR) e (2) Caixa Passiva 8 Ohms (P10)",
                "tela_metalica_de_protecao_frontal": True,
                "suporte_para_pedestal": True,
                "dimensoes_aproximadas": {
                    "produto": "56,5 x 40,5 x 40,5 cm",
                    "embalagem": "58 x 42 x 42 cm"
                },
                "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
                "padrao_de_fabrica": "pré-ajustado em 220V",
                "peso": {
                    "liquido": "15 Kg",
                    "bruto": "16,1 Kg"
                }
            }
        },
        {
            "nome": "Monitor/Retorno de Palco Passivo DATREL MP12-250",
            "descricao": "A Caixa Retorno MP 12-250 da Datrel, atinge incríveis 250 Watts de potência e possui alto-falante de 12 polegadas, perfeito para ser utilizada em redes de sonorização, em eventos de porte pequeno, médio e grande, como auditórios, eventos, igrejas, shows e bares. Conta com 2 saídas P10, design compacto e versátil, além de possuir furação (base) para encaixe de tripé e alça de transporte.",
            "caracteristicas_tecnicas": {
                "modelo": "MP12-250",
                "potencia": "250 W",
                "alto_falante": "12\" e TWEETER",
                "sistema_2_em_1": "Pedestal ou Retorno",
                "divisor_de_frequencia": "01 via",
                "canais_de_entrada": "02 x P10 (8 Ohms)",
                "tela_metalica_de_protecao_frontal": True,
                "suporte_para_pedestal": True,
                "dimensoes_aproximadas": {
                    "produto": "56,5 x 40,5 x 40,5 cm",
                    "embalagem": "56,5 x 40,5 x 40,5 cm"
                },
                "peso": {
                    "liquido": "12,3 Kg",
                    "bruto": "12,3 Kg"
                }
            }
        },
        {
            "nome": "Monitor/Retorno de Palco Passivo DATREL MP10-200",
            "descricao": "A Caixa de Som Monitor Retorno Palco Passiva 10″ 200w MP10-200 da Datrel é uma caixa de som profissional projetado para oferecer qualidade sonora excepcional em ambientes de palco e estúdio. Com uma potência de 200 watts, essa caixa de som passiva possui um alto-falante de 10 polegadas que proporciona uma reprodução de áudio clara e nítida, abrangendo uma ampla faixa de frequências para atender às necessidades de músicos e artistas. Seu design robusto e durável produzido em madeira MDF garante que ela possa resistir ao uso intenso em ambientes de apresentações ao vivo, enquanto sua construção cuidadosamente projetada minimiza as interferências e distorções indesejadas. A caixa de som monitor MP10-200 é especialmente concebida para funcionar como um retorno de palco, permitindo que os músicos ou vocalistas ouçam o som de maneira precisa e detalhada durante suas apresentações, contribuindo para um desempenho musical excepcional. Os recursos adicionais, como entradas e saídas de áudio bem configuradas, facilitam a integração com outros equipamentos de som e sistemas de amplificação. Seja para uso em palcos, igrejas, bares, cultos, estúdios de gravação ou ambientes de ensaio, a Caixa de Som Monitor Retorno Palco Passiva 10″ 200w MP10-200 Datrel se destaca como uma escolha confiável e de alta qualidade para aprimorar a experiência auditiva dos artistas e garantir um som excepcional em qualquer cenário musical.",
            "caracteristicas_tecnicas": {
                "modelo": "MP10-200",
                "potencia": "200 W",
                "alto_falante": "10\" e TWEETER",
                "sistema_2_em_1": "Pedestal ou Retorno",
                "divisor_de_frequencia": "01 via",
                "canais_de_entrada": "02 x P10 (8 Ohms)",
                "tela_metalica_de_protecao_frontal": True,
                "suporte_para_pedestal": True,
                "dimensoes_aproximadas": {
                    "produto": "46 x 32,5 x 33,5 cm",
                    "embalagem": "48 x 34 x 35 cm"
                },
                "peso": {
                    "liquido": "7,4 Kg",
                    "bruto": "8,2 Kg"
                }
            }
        },
        {
            "nome": "Monitor/Retorno de Palco Ativo DATREL AT10-200",
            "descricao": "A Caixa Retorno Ativa 10″ 200W MA10-200 da Datrel é um equipamento de áudio de alta qualidade projetada para oferecer uma experiência sonora excepcional em ambientes de palco, estúdios e apresentações ao vivo. Com sua potência de 200 watts, essa caixa ativa é capaz de fornecer um som nítido, claro e poderoso, adequado para uma variedade de aplicações musicais e de entretenimento. O design compacto da Caixa Acústica a torna uma escolha ideal para músicos, bandas e artistas que buscam um retorno de palco eficaz. Seu alto-falante de 10 polegadas é otimizado para reproduzir frequências médias com precisão, garantindo uma reprodução sonora balanceada e envolvente. Além disso, a caixa é equipada com um driver de ótima qualidade para reproduzir agudos detalhados. Uma característica notável da Caixa de Som MA10-200 é a sua capacidade de atuar como uma unidade ativa principal para alimentar outra caixa passiva de mesma potência. Isso proporciona uma configuração flexível, permitindo que você expanda seu sistema de som de acordo com suas necessidades. Ao conectar uma caixa passiva compatível com a mesma potência, você pode criar um sistema de som estéreo ou ampliar a cobertura sonora do palco, garantindo uma experiência de audição imersiva para o público. Além disso, a Caixa de Som MA10-200 apresenta controles de equalização integrados, permitindo ajustar o som de acordo com as preferências e o ambiente acústico. Seu gabinete durável e resistente em madeira MDF protege os componentes internos, tornando-a adequada para uso em apresentações ao vivo onde a durabilidade é essencial.",
            "caracteristicas_tecnicas": {
                "modelo": "AT10-200 Monitor",
                "versoes": [
                    "Normal",
                    "Pop"
                ],
                "potencia": "200 W",
                "alto_falante": "10\" e TWEETER",
                "impedancia_de_entrada": "LINE e MIC",
                "equalizacao_ativa": "03 vias, sendo: Agudo, Médio e Grave",
                "divisor_de_frequencia": "01 via",
                "canais_de_entrada": [
                    "(1) LINE (P10)",
                    "(2) Auxiliar (RCA)",
                    "(3) Microfone (P10)"
                ],
                "controle_de_volume": "Geral e Independente (por canal)",
                "canais_de_saida": [
                    "(1) LINEOUT (P10)",
                    "(2) Caixa Passiva 8 Ohms (P10)"
                ],
                "tela_metalica_de_protecao_frontal": True,
                "suporte_para_pedestal": True,
                "dimensoes_aproximadas": {
                    "produto": "46 x 32,5 x 33,5 cm",
                    "embalagem": "49 x 34 x 35 cm"
                },
                "rede": "127 / 220 V (via Chave Seletora de Voltagem)",
                "padrao_de_fabrica": "pré-ajustado em 220V",
                "peso": {
                    "liquido": "10,9 Kg",
                    "bruto": "11,7 Kg"
                }
            }
        }
    ]
}

# Convertendo os dados para JSON
json_dados = json.dumps(dados, indent=4, ensure_ascii=False)

# Salvando em um arquivo JSON
with open("dados_monitores_retornos.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(json_dados)

print("Dados convertidos e salvos em dados_monitores_retornos.json")
