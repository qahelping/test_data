import csv

from enums import PageTitle


def filled(value: str) -> bool:
    return bool(value and value.strip())


def match_title(title: str):
    for item in PageTitle:
        if item.name == title:
            return item.value

    return None


def load_csv(csv_path: str):
    with open(csv_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def get_page_info(pages: list[dict], name: str, build=None):
    for row in pages:
        if row.get("name") != name:
            continue

        selector = row.get("selector")
        url = row.get("url")
        title = row.get("title")

        if build:
            if filled(row.get("test_selector")):
                selector = row.get("test_selector")

            if filled(row.get("test_url")):
                url = row.get("test_url")

            if filled(row.get("test_title")):
                title = row.get("test_title")
        return {
            "selector": selector,
            "url": url,
            "title": match_title(title),
        }

    raise ValueError(f"Строка name='{name}' не найдена в списке страниц.")
