import json
import re
f = open("source code.txt", "r")
data = {}
for line in f:
    try:
        line = (line.replace("\"", "").replace("\n\n", "").replace("\n", "").strip().split(":"))
        line[0] = re.sub("[^\w]+", "", line[0])
        line[1] = re.sub("[^\w]+", " ", line[1])
        data[line[0]] = line[1]
    except:
        pass
data = {x:v[1:-1]for x, v in data.items()}
print(data)
with open("export file.json", 'w', encoding='utf8') as f3:
  json.dump(data, f3, ensure_ascii=False, indent=1)
  my_dict = json.dumps(data, ensure_ascii=False)


