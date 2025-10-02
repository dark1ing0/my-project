import requests
from bs4 import BeautifulSoup
import json

URL = "https://ru.citaty.net/"  # URL

response = requests.get(
    URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10, allow_redirects=True
)

soup = BeautifulSoup(response.text, "html.parser")

products = []
for item in soup.find_all("div", class_="blockquote"):
    quote_elem = item.find("p", class_="blockquote-text")
    quote = (
        quote_elem.get_text(strip=True).replace("\xa0", " ") if quote_elem else "N/A"
    )
    author_elem = item.find("a", class_="link")
    author = author_elem.get_text(strip=True) if author_elem else "N/A"
    if quote != "N/A" and len(quote) > 10:
        products.append({"quote": quote, "author": author})

print("Первые 10 цитат:")
for p in products[:10]:
    print(p)
print(f"Всего: {len(products)} цитат")
