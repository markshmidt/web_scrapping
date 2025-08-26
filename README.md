## Quotes Scraper (Python)

A tiny Python scraper for quotes.toscrape.com.
It collects quote text, author, and tags across all pages and saves them to CSV and JSON.

## Features

- Follows pagination (clicks “Next” automatically)
- Extracts: text, author, tags
- Outputs:
quotes.csv (tags joined by ;)
quotes.json (tags preserved as a list)
- Uses a short delay between requests to be polite
- Uses Pylint to make the code clearer and readable
