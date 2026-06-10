"""
Portfolio sample: scrape a public demo website into CSV.

Target site: https://quotes.toscrape.com/
This sample intentionally uses only Python's standard library.
"""

from html.parser import HTMLParser
from urllib.request import urlopen
import csv


class QuoteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.quotes = []
        self._in_quote = False
        self._in_author = False
        self._current = {"quote": "", "author": ""}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        class_name = attrs.get("class", "")
        if tag == "span" and "text" in class_name:
            self._in_quote = True
        if tag == "small" and "author" in class_name:
            self._in_author = True

    def handle_endtag(self, tag):
        if tag == "span" and self._in_quote:
            self._in_quote = False
        if tag == "small" and self._in_author:
            self._in_author = False
            if self._current["quote"] and self._current["author"]:
                self.quotes.append(self._current)
                self._current = {"quote": "", "author": ""}

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return
        if self._in_quote:
            self._current["quote"] = text
        if self._in_author:
            self._current["author"] = text


def fetch_quotes(page=1):
    url = f"https://quotes.toscrape.com/page/{page}/"
    with urlopen(url, timeout=20) as response:
        html = response.read().decode("utf-8")
    parser = QuoteParser()
    parser.feed(html)
    return parser.quotes


def main():
    all_quotes = []
    for page in range(1, 4):
        all_quotes.extend(fetch_quotes(page))

    with open("quotes_sample.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author"])
        writer.writeheader()
        writer.writerows(all_quotes)

    print(f"Wrote {len(all_quotes)} rows to quotes_sample.csv")


if __name__ == "__main__":
    main()

