import datetime
from pathlib import Path
import re
from urllib.parse import unquote

import httpx
from tqdm import tqdm

from . import meta
from .storage import get_filepath


def get_file_metadata(url: str) -> dict:
    filename = unquote(url.rsplit("/", 1)[1])
    name, extension = filename.rsplit(".", 1)
    r = httpx.head(url, verify=False)
    file_size = int(r.headers.get("content-length", 0))
    if last_modified := r.headers.get("last-modified"):
        last_modified = datetime.datetime.strptime(
            r.headers.get("last-modified"),
            "%a, %d %b %Y %H:%M:%S %Z",
        )
    return {
        "name": name,
        "extension": extension,
        "url": url,
        "file_size": file_size,
        "last_modified": last_modified,
    }


def download_file(
    file_meta: dict,
    client: httpx.Client,
) -> bytes:
    headers = {}
    file_size = file_meta["file_size"]
    url = file_meta["url"]

    filepath: Path = file_meta["filepath"]
    if filepath.exists():
        size = filepath.stat().st_size
        if size == file_size:
            return
        headers |= {"Range": f"bytes={size}-"}

    filepath.parent.mkdir(exist_ok=True, parents=True)

    print(f"Downloading file {url} to {filepath}")

    with client.stream("GET", url, headers=headers, timeout=600) as r:
        pb = tqdm(total=file_size, unit_scale=True, unit="B")
        with open(filepath, "wb") as f:
            for chunk in r.iter_bytes():
                f.write(chunk)
                pb.update(len(chunk))
        pb.close()


def robust_download_file(
    file_meta: dict,
    client: httpx.Client,
) -> bytes:
    """Retry download if an error occurs."""
    while True:
        try:
            download_file(file_meta, client)
            break
        except httpx.HTTPError as e:
            print("Status code:", e.response.status_code)
            print(f"Error downloading file {file_meta['name']}. Retrying...")
            continue


def fetch_dataset(dataset: str, data_dir: Path):
    client = httpx.Client()
    fn_pattern = meta.datasets[dataset].get("fn_pattern")
    for url in meta.datasets[dataset]["urls"]:
        file_meta = get_file_metadata(url) | {
            "dataset": dataset,
        }
        if fn_pattern:
            partition, = re.search(fn_pattern, file_meta["name"]).groups()
            file_meta |= {"partition": partition}
        filepath = get_filepath(data_dir=data_dir, **file_meta)
        file_meta |= {"filepath": filepath}
        robust_download_file(file_meta, client)
    client.close()


def fetch_auxiliary_tables(auxiliary_table: str, data_dir: Path):
    client = httpx.Client()
    for url in meta.auxiliary_tables[auxiliary_table]["urls"]:
        file_meta = get_file_metadata(url) | {
            "dataset": auxiliary_table,
            "group": "tabelas-auxiliares",
        }
        filepath = get_filepath(data_dir=data_dir, **file_meta)
        file_meta |= {"filepath": filepath}
        robust_download_file(file_meta, client)
    client.close()


def fetch_tax_regime(tax_regime: str, data_dir: Path):
    client = httpx.Client()
    for url in meta.tax_regimes[tax_regime]["urls"]:
        file_meta = get_file_metadata(url) | {
            "dataset": tax_regime,
            "group": "regimes-tributarios",
        }
        filepath = get_filepath(data_dir=data_dir, **file_meta)
        file_meta |= {"filepath": filepath}
        robust_download_file(file_meta, client)
    client.close()


def fetch_docs(doc: str, data_dir: Path):
    client = httpx.Client()
    for url in meta.docs[doc]["urls"]:
        file_meta = get_file_metadata(url) | {
            "dataset": doc,
            "group": "documentacao",
        }
        filepath = get_filepath(data_dir=data_dir, **file_meta)
        file_meta |= {"filepath": filepath}
        robust_download_file(file_meta, client)
    client.close()
