from pathlib import Path

import httpx
from tqdm import tqdm

from .storage import get_filename


def get_file(url: str) -> bytes:
    with httpx.stream("GET", url, verify=False) as r:
        return r.read()


def download_file(
    file: dict,
    datadir: Path,
    client: httpx.Client,
) -> bytes:
    headers = {}
    filename = get_filename(file)
    content_length = file["content-length"]
    url = file["href"]

    destfilepath: Path = datadir / filename
    if destfilepath.exists():
        size = destfilepath.stat().st_size
        if size == content_length:
            return
        headers |= {"Range": f"bytes={size}-"}

    print(f"Downloading file {url}")

    with client.stream("GET", url, headers=headers) as r:
        pb = tqdm(total=content_length, unit_scale=True, unit="B")
        with open(destfilepath, "wb") as f:
            downloaded = r.num_bytes_downloaded
            for chunk in r.iter_bytes():
                f.write(chunk)
                pb.update(r.num_bytes_downloaded - downloaded)
                downloaded = r.num_bytes_downloaded
        pb.close()


def empresas():
    ...


def estabelecimentos():
    ...


def socios():
    ...


def simples():
    ...


def cnae():
    ...


def motivos():
    ...


def municipios():
    ...


def naturezas():
    ...


def paises():
    ...


def qualificacoes():
    ...


def regime_tributario():
    ...


def docs():
    ...
