# Quote Scraper
import csv
import json
import time
import requests
from bs4 import BeautifulSoup

BASE = "https://quotes.toscrape.com"
START_URL = f"{BASE}/page/1/"

def save_csv(rows, path="quotes.csv"):
    """Save scraped quotes into a CSV file."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "author", "tags"])
        for r in rows:
            writer.writerow([r["text"], r["author"], ";".join(r["tags"])])

def save_json(rows, path="quotes.json"):
    """Save scraped quotes into a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

def main():
    items = []
    url = START_URL

    while url:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        for block in soup.select(".quote"):
            text = block.select_one(".text").get_text(strip=True)
            author = block.select_one(".author").get_text(strip=True)
            tags = [t.get_text(strip=True) for t in block.select(".tags .tag")]
            items.append({"text": text, "author": author, "tags": tags})

        next_link = soup.select_one(".pager .next a")
        url = f"{BASE}{next_link['href']}" if next_link else None
        if url:
            time.sleep(0.5)

    print(f"Collected {len(items)} quotes.")
    save_csv(items)
    save_json(items)
    print("Saved quotes.csv and quotes.json")

if __name__ == "__main__":
    main()
