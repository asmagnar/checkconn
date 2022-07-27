## Imports section
import requests
import os
import sys
import configparser
import json

## Functions that are goint to be used in the code:
def create_request(url, method, headers, data, response):
    r=requests.request(method=method,url=url,headers=headers,data=data)
    if r.status_code==int(response):
        return 0
    else:
        return r.status_code

def validate_property():
    #some code
    print("stuff")

filename="endpoints.curl"
fileData = configparser.ConfigParser()
curlFile=os.path.join(os.path.dirname(__file__), 'conf', filename) # File is in script root directory under /conf folder
fileData.read(curlFile)



## Read each configuration in config file. 
for section in fileData.sections():
    if fileData.has_option(section,'url'): #validate if option exists
        if fileData[section]['url'] =='': #validate if option has value
            sys.exit("Error: Property url has no value! Please setup url in "+ curlFile +" config file") 
        else:
            url=fileData[section]['url']
    else:
        sys.exit("Error: No url defined! Please setup url in "+ curlFile +" config file") #if option does not have value program exits

    method=fileData[section]['method']
    headers=json.loads(fileData[section]['headers'])
    data=fileData[section]['data']
    response=fileData[section]['response']
    result=create_request(url, method, headers, data, response)
    print(result)

#endpoints.curl file:
#[IPG TEST EXAMPLE]
#url=
#method=
#headers={"x-api-key": "PMAK-62e14ee9ce05de328ea1af2a-adba641dba080a40730c6e12e24f3ef0aa", "testheader": "testvalue"}
#data=
#response=500
