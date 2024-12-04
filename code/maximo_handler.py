import requests
import json
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core import IAMTokenManager
import time
import logging

load_dotenv()

class MaximoHandler:
    
    def __init__(self):
        self.MAS_URL = os.getenv("MAS_URL", None)
        self.MAS_APIKEY = os.getenv("MAS_APIKEY", None)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(os.environ.get('LOGLEVEL', 'INFO').upper())


    def getvalues(self, classname):
        self.logger.info("------------------------------------------------ getColumns Started ------------------------------------------------")
        start_time = time.time()
        self.logger.debug(f"TableName  : {classname}")
        
        url = self.MAS_URL + "/api/os/MXAPIMAXATTRIBUTE?lean=1&ignorecollectionref=1&oslc.select=objectname,attributename,classname&oslc.where=classname=%22" + classname+ "%22"

        headers = {
            "Content-Type": "application/json",
            "apikey": self.MAS_APIKEY
            }
           
        response = requests.request("GET", url, headers=headers, verify=False)

        print(response.text)

        return response.text
    