import urllib.parse

from bs4 import BeautifulSoup


def scrape_index(html: str) -> dict:
    soup = BeautifulSoup(html, "lxml")

    links = {}

    anchors = soup.select("#content-core a")
    for a in anchors:
        href = a["href"]
        filename = href.rsplit("/", maxsplit=1)[1]
        filename = urllib.parse.unquote(filename)
        text = a.text
        if not text:
            continue
        links[filename] = {"href": href, "text": text}

    return links
