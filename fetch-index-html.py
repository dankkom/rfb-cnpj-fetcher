import argparse
import json
from pathlib import Path

from rfb_cnpj import collect, scraper

URL = (
    "https://www.gov.br"
    "/receitafederal"
    "/pt-br"
    "/assuntos"
    "/orientacao-tributaria"
    "/cadastros"
    "/consultas"
    "/dados-publicos-cnpj"
)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datadir", type=Path)

    args = parser.parse_args()

    return args


def main():
    args = get_args()
    datadir = args.datadir

    datadir.mkdir(parents=True, exist_ok=True)

    html = collect.get_file(URL)
    links = scraper.scrape_index(html.decode("utf-8"))

    with open(datadir / "index.html", "wb") as f:
        f.write(html)
    with open(datadir / "index.json", "w", encoding="utf-8") as f:
        json.dump(links, f)


if __name__ == "__main__":
    main()
