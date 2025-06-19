import requests
import sys
import json

if len(sys.argv)!=2:
    sys.exit()
    
#Making a HTTP request to itunes using python
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

#Grabs the json object I care about 
o=response.json()

#Prints the results and the key:value in trackName
for result in o["results"]:
    print(result["trackName"])