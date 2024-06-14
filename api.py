import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())



#make a proper format for the api data we received
import sys
import requests
import json

if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])
print(response.json())
#just printing as we have them in the API key and understand it is difficult to understand the data 
print("-----------------------------------------------------------------------------------------------")
print(json.dumps(response.json(), indent=2))
#using dumps creating a 2 spaces in the file representing 
print("----------------------------------------------------------------------------------------------------")
#if we need any specific things from the API like songs or something use below for loop and proper allignment in the file
o = response.json()
for result in o["results"]:
    print(result["trackName"], result["trackPrice"])


