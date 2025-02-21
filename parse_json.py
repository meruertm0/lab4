import json
from tabulate import tabulate

with open('sample-data.json', 'r') as f:
    data = json.load(f)


keys = ["dn", "descr", "speed", "mtu"]

arr = []

for obj in data["imdata"]:
    attr = obj["l1PhysIf"]["attributes"]
    tmp = []
    for i in keys:
        tmp.append(attr.get(i))
    arr.append(tmp)

header_keys = ["DN", "Description", "Speed", "MTU"]


print("Interface Status")
width = 67
print("=" * width)
print(tabulate(arr, headers=header_keys))
