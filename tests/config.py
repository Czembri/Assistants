import json

with open('config.json', 'r') as config:
    json_reader = json.load(config)

    cloud = json_reader['files']
    secret_key = json_reader['sql']['secret_key']
    db_uri = json_reader['sql']['db_uri']

print(cloud)
print(secret_key)
print(db_uri)
