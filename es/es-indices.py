#!/usr/bin/env python3
import requests
import json
from elasticsearch import Elasticsearch

# connect to the es cluster
es = Elasticsearch("localhost:9200")
print(es.cluster.state()['cluster_name'])
# print(es.cluster.state(metric='_all'))
# create an index
# es.indices.create('index-003')

# print(es.cat.indices(h='health,uuid'))
# print(es.cat.allocation(h='disk.percent'))


settings_blocked = es.indices.get_settings(index='_all', name='index.blocks.read_only_allow_delete')

# # Check if http://localhost:9200/_all/_settings contains "read_only_allow_delete"

# es.indices.put_settings(body={"index.blocks.read_only_allow_delete": "true"}, index='_all')
print(es.indices.get_settings(index='_all', name='index.blocks.read_only_allow_delete'))


#  Check if http://localhost:9200/_all/_settings contains "read_only_allow_delete"
def unblock_indexes(arg):
    data = json.dumps(arg)
    if "true" in data:
        es.indices.put_settings(body={"index.blocks.read_only_allow_delete": "false"}, index='_all')
        print('Indexes unblocked, put "index.blocks.read_only_allow_delete": "false"')
    else:
        print('OK.Indexes not blocked')


unblock_indexes(settings_blocked)

