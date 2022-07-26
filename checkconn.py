import requests
import os
import sys

## test using jproperties lib

#import jproperties
#from jproperties import Properties
#
#for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'conf')):
#    print (filename)
#    if filename.endswith(".curl"):
#        configs=Properties()
#        with open(os.path.join(os.path.dirname(__file__), 'conf', filename), 'rb') as config_file:
#            configs.load(config_file)
#            print(configs.get("url"))


## test using configparser ilb
import configparser

for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'conf')):
    configParser = configparser.RawConfigParser()
    curlFile=os.path.join(os.path.dirname(__file__), 'conf', filename)
    #configFilePath = r'curlfile'
    configParser.read(curlFile)
    print(url)


#url = "https://www.example.com"
#
#request_response = requests.head(url)
#status_code = request_response.status_code
#website_is_up = status_code == 200
#
#requests.request(method=)
#
#print(website_is_up)
## OUTPUT
#True
