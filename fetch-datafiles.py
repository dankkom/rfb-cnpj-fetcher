import argparse
import json
from pathlib import Path

from rfb_cnpj.collect import download_file


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

    for filename in index:
        destfilepath = datadir / filename
        if destfilepath.exists():
            continue
        print(filename)
        with open(datadir / filename, "wb") as f:
            for chunk in download_file(index[filename]["href"]):
                f.write(chunk)


if __name__ == "__main__":
    main()
