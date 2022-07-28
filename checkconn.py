## Imports section
import requests
import os
import sys
import configparser
import json

# settings
filename="endpoints.curl" # name of the file that contains the endpoints

# File syntax example :
#     [ENDPOINT NAME]
#     url=http://example.org/path
#     method=POST
#     headers={"testheader": "testvalue"}
#     data={"":""}
#     response=500

# Read file:
fileData = configparser.ConfigParser()
curlFile=os.path.join(os.path.dirname(__file__), 'conf', filename) # File is in script root directory under /conf folder
fileData.read(curlFile) 
    

## Functions that are goint to be used in the code:
def create_request(url, method, headers, data, response):
    r=requests.request(method=method,url=url,headers=headers,data=data)
    if r.status_code==int(response):
        return 0
    else:
        return r.status_code

def get_property_value(section, var): # reads property value from file and validates if exists or has value. Crashes if not configured
    if fileData.has_option(section, var ): #validate if option exists
        if fileData[section][var] !='': #validate if option has value
            return(fileData[section][var])
        else:
            sys.exit("Error: Property "+ var +" has no value! Please setup url in "+ curlFile +" config file") #if option does not exists program exits
    else:
        sys.exit("Error: No "+ var +" defined! Please setup "+ var +" in "+ curlFile +" config file") #if option does not have value program exits
    
def get_property_value_json(section, var): # reads json property value from file and validates if exists or has value. Crashes if not configured
    if fileData.has_option(section, var ): #validate if option exists
        if fileData[section][var] !='': #validate if option has value
            return(json.loads(fileData[section][var]))
        else:
            sys.exit("Error: Property "+ var +" has no value! Please setup url in "+ curlFile +" config file") #if option does not exists program exits
    else:
        sys.exit("Error: No "+ var +" defined! Please setup "+ var +" in "+ curlFile +" config file") #if option does not have value program exits

## Read each configuration in config file. 
for section in fileData.sections():
    url=get_property_value(section, "url")
    method=get_property_value(section, "method")
    headers=get_property_value_json(section, "headers")
    data=get_property_value_json(section, "data")
    response=get_property_value(section, "response")
    result=create_request(url, method, headers, data, response)
    print(result)
