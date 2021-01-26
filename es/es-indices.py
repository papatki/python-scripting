#!/usr/bin/env python3
import requests
import json

url_blocked = 'http://localhost:9200/_all/_settings'
url_disk = 'http://localhost:9200/_cat/allocation?h=disk.percent'
header = {
    'Content-Type': 'application/json'
}
indices_blocked = {"index.blocks.read_only_allow_delete": "null"}
disk_usage = int((requests.get(url_disk)).text)
# r = int(disk_usage.text)

get_blocked = requests.get(url_blocked).json()


# rb = r_blocs.json()

# Check if http://localhost:9200/_all/_settings contains "read_only_allow_delete"
def check_json(json_arg):
    data = json.loads(json_arg)
    if "read_only_allow_delete" in data:
        return "blocked"
    else:
        return "not blocked"


# Unlock indices
if check_json(get_blocked) == "blocked":
    requests.put(url_blocked, data=indices_blocked, headers=header)
    print('Indexes unblocked, put "index.blocks.read_only_allow_delete": "null"')
else:
    print('OK')
    exit(0)

# disk_usage <= 85
