BASE_URL = "https://arquivos.receitafederal.gov.br/dados/cnpj"

INITIAL_DATE = "2023-05"

datasets = {
    "empresas": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Empresas{i}.zip",
        "fn_pattern": r"Empresas(\d)",
    },
    "estabelecimentos": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Estabelecimentos{i}.zip",
        "fn_pattern": r"Estabelecimentos(\d)",
    },
    "socios": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Socios{i}.zip",
        "fn_pattern": r"Socios(\d)",
    },
    "simples": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Simples.zip",
    },
}

auxiliary_tables = {
    "cnaes": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Cnaes.zip",
    },
    "motivos": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Motivos.zip",
    },
    "municipios": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Municipios.zip",
    },
    "naturezas": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Naturezas.zip",
    },
    "paises": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Paises.zip",
    },
    "qualificacoes": {
        "url_format": BASE_URL + "/dados_abertos_cnpj/{date_ref:%Y-%m}/Qualificacoes.zip",
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
