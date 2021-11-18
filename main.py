import json

f = open('steam.json')

data = json.load(f)

print(data[0])

print(f"er zitten {len(data)} items in.")

f.close()