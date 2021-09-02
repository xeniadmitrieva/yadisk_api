import requests
import sys

def SendRequest (method, url,head, testName, statusCode=200):
        response = requests.request(method, url, headers=head)
        if not response.status_code == statusCode :
             raise AssertionError(testName +' -> FAIL\n Not passed test server return ' + str(response.status_code))
        if not method=='DELETE':
            result = response.json()
            return result

def ExistingFileName (jsonstr,fileName,testName):
    exist = 1
    i = 0
    while i < int(len(jsonstr['_embedded']['items'])):
        if jsonstr['_embedded']['items'][i]['name'] == fileName:
            exist = 0
            break
        i = i + 1
    if not exist == 0:
        raise AssertionError(testName +' -> FAIL\n File '+fileName+' does not exist\n '+str(jsonstr))

import random
import string
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))