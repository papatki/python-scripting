#!/usr/bin/env python3
import requests
import json
from elasticsearch import Elasticsearch
# connect to the es cluster
es = Elasticsearch("localhost:9200")
print(es.cluster.state()['cluster_name'])
# print(es.cluster.state(metric='_all'))
# create an index
# es.indices.create('index-001')

print(es.cat.indices(h='health,uuid'))
print(es.cat.allocation(h='disk.percent'))