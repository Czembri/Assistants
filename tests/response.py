import json
import requests


url = 'http://api.dataatwork.org/v1/jobs'
response = requests.get(url).text
parseJson = json.loads(response)

listOfJobs = []
for job in parseJson:
    try:
        print(job['title'])
    except:
        break