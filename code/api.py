import requests
import json

class_name = "psdi.app.financial.FldPartialGLAccount"
url = "https://xxxxxxxxxxxxxx.us-south.containers.appdomain.cloud/maximo/api/os/MXAPIMAXATTRIBUTE?lean=1&ignorecollectionref=1&oslc.select=objectname,attributename,classname&oslc.where=classname=%22" + class_name+ "%22"

headers = {
  'Content-Type': 'application/json',
  'apikey': 'xxxxxxxxxxxx'
}

payload = {}

response = requests.request("GET", url, headers=headers, verify=False)

print(response.text)