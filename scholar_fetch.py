import requests
import json

ORCID_ID = "0000-0002-2628-326X"

url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"

headers = {
    "Accept": "application/json"
}

r = requests.get(url, headers=headers)
data = r.json()

pubs = []

for group in data["group"]:
    work = group["work-summary"][0]

    title = work["title"]["title"]["value"]

    year = None
    if work["publication-date"] and work["publication-date"]["year"]:
        year = work["publication-date"]["year"]["value"]

    doi = None
    for ext in work.get("external-ids", {}).get("external-id", []):
        if ext["external-id-type"] == "doi":
            doi = ext["external-id-value"]

    pubs.append({
        "title": title,
        "year": year,
        "journal": "",
        "url": f"https://doi.org/{doi}" if doi else "#"
    })

with open("publications.json", "w") as f:
    json.dump(pubs, f, indent=2)
