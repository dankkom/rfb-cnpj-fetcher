import argparse
from pathlib import Path

from rfb_cnpj_fetcher import constants, fetcher


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path)

    args = parser.parse_args()

    return args


def main():
    args = get_args()
    data_dir = args.data_dir

    for dataset in constants.datasets:
        fetcher.fetch_dataset(dataset, data_dir=data_dir)

    for auxiliary_table in constants.auxiliary_tables:
        fetcher.fetch_auxiliary_tables(auxiliary_table, data_dir=data_dir)

    for tax_regime in constants.tax_regimes:
        fetcher.fetch_tax_regime(tax_regime, data_dir=data_dir)

    for doc in constants.docs:
        fetcher.fetch_docs(doc, data_dir=data_dir)


if __name__ == "__main__":
    main()
