import datetime
import urllib.parse

import httpx
from bs4 import BeautifulSoup


def scrape_index(html: str) -> dict:
    soup = BeautifulSoup(html, "lxml")

    links = []

    anchors = soup.select("#content-core a")
    for a in anchors:
        href = a["href"]
        filename = href.rsplit("/", maxsplit=1)[1]
        filename = urllib.parse.unquote(filename)
        text = a.text
        if not text:
            continue
        links.append({"href": href, "text": text, "filename": filename})

    return links


def get_links_metadata(links: list[dict]) -> list[dict]:

    def parse(headers):
        if last_modified := headers.get("last-modified"):
            last_modified = datetime.datetime.strptime(
                last_modified,
                r"%a, %d %b %Y %H:%M:%S %Z",
            )
        if content_length := headers.get("content-length"):
            content_length = int(headers["content-length"])
        return {
            "last-modified": last_modified,
            "content-length": content_length,
        }

    with httpx.Client(verify=False, timeout=300) as client:
        for link in links:
            headers = {}
            if "headers" not in link:
                r = client.head(link["href"])
                headers = parse(r.headers)
            yield {
                **headers,
                **link,
            }
