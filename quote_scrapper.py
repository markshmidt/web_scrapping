# Quote Scrapper
import csv
import json
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/page/1/"

def save_csv(rows, path="quotes.csv"):
    '''
    Saving scrapped quotes into a csv file.
    '''
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "author", "tags"])
        for r in rows:
            writer.writerow([r["text"], r["author"], ";".join(r["tags"])])

def save_json(rows, path="quotes.json"):
    '''
    Saving scrapped quotes into a json file.
    '''
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

def main():
    # 1) download html
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    html = resp.text

    # 2) parse
    soup = BeautifulSoup(html, "html.parser")

    # 3) extract blocks and fields
    items = []
    for block in soup.select(".quote"):  # or: soup.find_all("div", class_="quote")
        text = block.select_one(".text").get_text(strip=True)
        author = block.select_one(".author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in block.select(".tags .tag")]
        items.append({"text": text, "author": author, "tags": tags})

    print(f"Collected {len(items)} quotes from page 1.")

    # 4) save
    save_csv(items)
    save_json(items)
    print("Saved quotes.csv and quotes.json")

if __name__ == "__main__":
    main()
