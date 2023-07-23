BASE_URL = "https://dadosabertos.rfb.gov.br/CNPJ"

datasets = {
    "empresas": {
        "urls": [
            BASE_URL + f"/Empresas{i}.zip" for i in range(10)
        ],
        "fn_pattern": r"Empresas(\d)",
    },
    "estabelecimentos": {
        "urls": [
            BASE_URL + f"/Estabelecimentos{i}.zip" for i in range(10)
        ],
        "fn_pattern": r"Estabelecimentos(\d)",
    },
    "socios": {
        "urls": [
            BASE_URL + f"/Socios{i}.zip" for i in range(10)
        ],
        "fn_pattern": r"Socios(\d)",
    },
    "simples": {
        "urls": [
            BASE_URL + "/Simples.zip",
        ],
    },
}

auxiliary_tables = {
    "cnaes": {
        "urls": [
            BASE_URL + "/Cnaes.zip",
        ],
    },
    "motivos": {
        "urls": [
            BASE_URL + "/Motivos.zip",
        ],
    },
    "municipios": {
        "urls": [
            BASE_URL + "/Municipios.zip",
        ],
    },
    "naturezas": {
        "urls": [
            BASE_URL + "/Naturezas.zip",
        ],
    },
    "paises": {
        "urls": [
            BASE_URL + "/Paises.zip",
        ],
    },
    "qualificacoes": {
        "urls": [
            BASE_URL + "/Qualificacoes.zip",
        ],
    },
}

tax_regimes = {
    "imunes-isentas": {
        "urls": [
            BASE_URL + "/regime_tributario/Imunes%20e%20isentas.zip",
        ],
    },
    "lucro-arbitrado": {
        "urls": [
            BASE_URL + "/regime_tributario/Lucro%20Arbitrado.zip",
        ],
    },
    "lucro-presumido": {
        "urls": [
            BASE_URL + "/regime_tributario/Lucro%20Presumido.zip",
        ],
    },
    "lucro-real": {
        "urls": [
            BASE_URL + "/regime_tributario/Lucro%20Real.zip",
        ],
    },
    "leiaute-dos-arquivos": {
        "urls": {
            BASE_URL + "/regime_tributario/Leiaute%20dos%20Arquivos.odt",
        },
    },
}

docs = {
    "cnpj-metadados": {
        "urls": [
            "https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf",
        ],
    },
    "layout-dados-abertos-cnpj": {
        "urls": [
            BASE_URL + "/LAYOUT_DADOS_ABERTOS_CNPJ.pdf",
        ],
    },
}
