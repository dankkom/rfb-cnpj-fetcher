import httpx
from tqdm import tqdm


def get_file(url) -> bytes:
    with httpx.stream("GET", url, verify=False) as r:
        return r.read().content


def download_file(url) -> bytes:
    with httpx.stream("GET", url, verify=False) as r:
        length = int(r.headers.get("Content-Length", "0"))
        with tqdm(total=length, unit_scale=True, unit="B") as pb:
            downloaded = r.num_bytes_downloaded
            for chunk in r.iter_bytes():
                yield chunk
                pb.update(r.num_bytes_downloaded - downloaded)
                downloaded = r.num_bytes_downloaded
