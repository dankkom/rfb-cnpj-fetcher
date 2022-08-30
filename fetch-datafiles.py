import datetime
import argparse
import json
from pathlib import Path

import httpx

from rfb_cnpj.collect import download_file
from rfb_cnpj.storage import get_filename


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datadir", type=Path)

    args = parser.parse_args()

    return args


def main():
    args = get_args()
    datadir = args.datadir

    with open(datadir / "index.json", "r", encoding="utf-8") as f:
        index = json.load(f)

    client = httpx.Client(verify=False, timeout=60)

    for file in index:
        while True:
            try:
                download_file(file, datadir, client)
                break
            except (httpx.NetworkError, httpx.ReadTimeout) as e:
                print(f"Error {e}")

    client.close()


if __name__ == "__main__":
    main()
