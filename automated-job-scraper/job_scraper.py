from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INPUT_HTML = ROOT / "job_board_sample.html"
OUTPUT_CSV = ROOT / "sample_job_output.csv"


@dataclass
class Job:
    job_id: str
    title: str
    company: str
    location: str
    pay_usd: int
    tags: list[str]
    url: str


class JobBoardParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.jobs: list[Job] = []
        self._current: dict[str, object] | None = None
        self._field: str | None = None
        self._tag_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        class_name = attrs_dict.get("class", "")

        if tag == "article" and "job-card" in class_name:
            self._current = {
                "job_id": attrs_dict.get("data-id", ""),
                "title": "",
                "company": "",
                "location": "",
                "pay": "",
                "tags": [],
                "url": "",
            }
            return

        if self._current is None:
            return

        if tag == "a" and not self._current["url"]:
            self._field = "title"
            self._current["url"] = attrs_dict.get("href", "")
        elif tag == "p" and "company" in class_name:
            self._field = "company"
        elif tag == "p" and "location" in class_name:
            self._field = "location"
        elif tag == "p" and "pay" in class_name:
            self._field = "pay"
        elif tag == "li":
            self._field = "tag"
            self._tag_buffer = []

    def handle_data(self, data: str) -> None:
        if self._current is None or self._field is None:
            return

        value = " ".join(data.split())
        if not value:
            return

        if self._field == "tag":
            self._tag_buffer.append(value)
        else:
            existing = str(self._current.get(self._field, ""))
            self._current[self._field] = f"{existing} {value}".strip()

    def handle_endtag(self, tag: str) -> None:
        if self._current is None:
            return

        if tag == "li" and self._field == "tag":
            tag_value = " ".join(self._tag_buffer).strip()
            if tag_value:
                self._current["tags"].append(tag_value)
            self._field = None
            self._tag_buffer = []
        elif tag in {"a", "p"}:
            self._field = None
        elif tag == "article":
            self.jobs.append(
                Job(
                    job_id=str(self._current["job_id"]),
                    title=str(self._current["title"]),
                    company=str(self._current["company"]),
                    location=str(self._current["location"]),
                    pay_usd=parse_pay(str(self._current["pay"])),
                    tags=list(self._current["tags"]),
                    url=str(self._current["url"]),
                )
            )
            self._current = None
            self._field = None


def parse_pay(raw_pay: str) -> int:
    match = re.search(r"\$([0-9][0-9,]*)", raw_pay)
    if not match:
        return 0
    return int(match.group(1).replace(",", ""))


def is_good_fit(job: Job) -> bool:
    searchable = " ".join([job.title, job.company, " ".join(job.tags)]).lower()
    keywords = ["python", "csv", "scraping", "automation", "gmail", "excel"]
    return job.pay_usd >= 80 and any(keyword in searchable for keyword in keywords)


def scrape_jobs(html_path: Path) -> list[Job]:
    parser = JobBoardParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    return [job for job in parser.jobs if is_good_fit(job)]


def write_csv(jobs: list[Job], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=[
                "job_id",
                "title",
                "company",
                "location",
                "pay_usd",
                "tags",
                "url",
            ],
        )
        writer.writeheader()
        for job in jobs:
            writer.writerow(
                {
                    "job_id": job.job_id,
                    "title": job.title,
                    "company": job.company,
                    "location": job.location,
                    "pay_usd": job.pay_usd,
                    "tags": "; ".join(job.tags),
                    "url": job.url,
                }
            )


def main() -> None:
    jobs = scrape_jobs(INPUT_HTML)
    write_csv(jobs, OUTPUT_CSV)
    print(f"Wrote {len(jobs)} jobs to {OUTPUT_CSV.name}")


if __name__ == "__main__":
    main()
