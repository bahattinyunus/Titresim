# -*- coding: utf-8 -*-
"""
Sync quotes.json to web/app.js QUOTES_DATA array.
"""
import json
import re
from pathlib import Path

quotes_file = Path("data/quotes.json")
app_js_file = Path("web/app.js")

with open(quotes_file, "r", encoding="utf-8") as f:
    quotes_data = json.load(f)

# JavaScript formatına dönüştür
js_quotes = []
for q in quotes_data:
    js_quotes.append({
        "id": q["id"],
        "author": q["author"],
        "era": q["era"],
        "work": q["work"],
        "quote": q["quote_tr"],
        "category": q["category"],
        "freq": q["recommended_freq"],
        "reflection": q["reflection"]
    })

js_array_str = "const QUOTES_DATA = " + json.dumps(js_quotes, ensure_ascii=False, indent=2) + ";\n"

with open(app_js_file, "r", encoding="utf-8") as f:
    content = f.read()

# const QUOTES_DATA = [ ... ]; regex ile bul ve değiştir
pattern = r"const QUOTES_DATA = \[[\s\S]*?\];\n"
if re.search(pattern, content):
    new_content = re.sub(pattern, js_array_str, content, count=1)
    with open(app_js_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"app.js başarıyla güncellendi: {len(js_quotes)} alıntı yazıldı.")
else:
    print("QUOTES_DATA deseni app.js içinde bulunamadı.")
