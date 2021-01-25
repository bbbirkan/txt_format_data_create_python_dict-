import json
import re

#doesnt work :/
"""
dictionary = {}
with open('/Users/birkankalyon/Desktop/okk.txt', "r") as f:
    for line in f:
        s = (line.replace("\"", "").replace("\n\n", "").replace("\n", "").strip().split(":"))
        xkey = (s[0])
        xvalue = (s[-1])
        zvalue = str(xvalue)
        value = zvalue[:0] + zvalue[0 + 1:]
        key = xkey.replace(' ', '', 1)
        dict = {'key1': 'stackoverflow'}
        dictadd={key:value}
        (dict.update(dictadd))
        # dict1={key:value}
        # dictpop[key] = value
        # dict3={**dict, **dictadd}
        # print(key)
        # print(value)
        dictionary_list = []
        dictionary_list.append(key)
        dictionary_list.append(value)
        #for i in dictadd:
            #dictionary_list.extend([i,dictadd[i]])
            #a=dictionary_list.append(i)
            #b=dictionary_list.append(dictadd[i])
            #print(dictionary_list)
            #print(i, dictadd[i])
"""



f = open("/Users/birkankalyon/PycharmProjects/word_aplication/translate_json/english01.txt", "r")
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
with open("/Users/birkankalyon/PycharmProjects/word_aplication/translate_json/english02.json", 'w', encoding='utf8') as f3:
  json.dump(data, f3, ensure_ascii=False, indent=1)
  my_dict = json.dumps(data, ensure_ascii=False)
#rint(json.dumps(data, sort_keys=True, indent=4))

