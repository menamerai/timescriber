import json

f = open("./output/data.json")

data = json.load(f)

for segment in data["segments"]:
    print(f"{segment['start']}: {segment['text']}")

f.close()