import json,csv,sys,os
d=sys.argv[1]
rows=[]
for c in "us gb jp de fr kr br mx tw hk".split():
  for chart in ["paid","grossing"]:
    j=json.load(open(f"{d}/{chart}_{c}.json"))
    upd=j["feed"]["updated"]["label"]
    for i,e in enumerate(j["feed"].get("entry",[]),1):
      rows.append(dict(country=c,chart=chart,rank=i,id=e["id"]["attributes"]["im:id"],name=e["im:name"]["label"],
        artist=e["im:artist"]["label"],category=e["category"]["attributes"]["label"],genre_id=e["category"]["attributes"]["im:id"],
        price=e["im:price"]["attributes"]["amount"],currency=e["im:price"]["attributes"]["currency"],
        url=e["id"]["label"].split("?")[0],feed_updated=upd))
w=csv.DictWriter(open(f"{d}/all.csv","w"),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print(len(rows))
