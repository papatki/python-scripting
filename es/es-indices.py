#!/usr/bin/env python3
import requests
import json

url_blocked = 'http://localhost:9200/_all/_settings'
url_disk = 'http://localhost:9200/_cat/allocation?h=disk.percent'
header = {
    'Content-Type': 'application/json'
}
indices_unblocked = '{"index.blocks.read_only_allow_delete": null}'

disk_usage = int((requests.get(url_disk)).text)
get_blocked = requests.get(url_blocked).json()


# Check if http://localhost:9200/_all/_settings contains "read_only_allow_delete"
def check_json(json_arg):
    data = json.dumps(json_arg)
    if "read_only_allow_delete" in data:
        return "blocked"
    else:
        return "not blocked"


def get_disk_usage(json_arg):
    data = json.dumps(json_arg)
    if data >= '85':
        return "full"
    else:
        return "free"


# print(get_disk_usage(disk_usage))
# print(disk_usage)

# Unlock indices
if check_json(get_blocked) == "blocked":
    requests.put(url_blocked, data=indices_unblocked, headers=header)
    print('Indexes unblocked, put "index.blocks.read_only_allow_delete": "null"')
else:
    print('OK')
    exit(0)

# disk_usage <= 85
