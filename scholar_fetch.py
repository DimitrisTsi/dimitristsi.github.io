from scholarly import scholarly
import json

AUTHOR_ID = "RgjimzYAAAAJ"

author = scholarly.search_author_id(AUTHOR_ID)
author = scholarly.fill(author)

pubs = []

for p in author["publications"]:
    p = scholarly.fill(p)
    pubs.append({
        "title": p["bib"]["title"],
        "year": p["bib"].get("pub_year"),
        "journal": p["bib"].get("venue"),
        "url": p.get("pub_url")
    })

with open("publications.json", "w") as f:
    json.dump(pubs, f, indent=2)
