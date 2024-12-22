import json
with open(r'E:\code\github_clone\Mycode\Electrochemistry\12-22DOL\data.json', 'r') as file:
    data = json.load(file)
newdata = {}
for j in data[0]:
    newdata[j] = []
for i in data:
    for j in newdata:
        newdata[j].append(i[j])
with open(r'E:\code\github_clone\Mycode\Electrochemistry\12-22DOL\changed_data.json', 'w') as file:
    json.dump(newdata, file, indent=4)