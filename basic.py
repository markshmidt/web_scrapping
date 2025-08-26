# file: step1_one_page.py
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/page/1/"

# Downloading html of the page
response = requests.get(url, timeout=15)   # timeout prevents hanging forever
html = response.text # this is the raw HTML (a long string)

# Parsing the HTML so we can search it
soup = BeautifulSoup(html, "html.parser") #writes it like html doc

# 3) Each quote is inside a block with class="quote"
quote_blocks = soup.select(".quote")  # read as: find elements with class 'quote'
print(quote_blocks)

for block in quote_blocks:
    text = block.select_one(".text").get_text(strip=True)      # the quote text
    author = block.select_one(".author").get_text(strip=True)  # the author name
    tags = block.select_one(".tags").get_text(strip=True)
    print(f"— {text}  ({author})")
