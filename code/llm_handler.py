import requests
import json
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core import IAMTokenManager
import time
load_dotenv()

import logging

class LlmHandler:
    
    def __init__(self):
        self.IBMC_AUTH_URL = os.getenv("IBMC_AUTH_URL", None)
        self.WX_APIKEY = os.getenv("WX_APIKEY", None)
        self.WX_ENDPOINT_URL = os.getenv("WX_ENDPOINT_URL", None)
        self.WX_PROJECT_ID = os.getenv("WX_PROJECT_ID", None)
        self.WX_MODEL_ID = os.getenv("WX_MODEL_ID", None)
        self.WX_PROMPT_FILE_NAME = os.getenv("WX_PROMPT_FILE_NAME", "")

        if self.WX_PROMPT_FILE_NAME:
            # Combine the current directory with the file name to create the full path
            current_dir = os.getcwd()
            prompt_file_path = os.path.join(current_dir, self.WX_PROMPT_FILE_NAME)
            
            # Check if the file exists and read its content
            if os.path.exists(prompt_file_path):
                with open(prompt_file_path, 'r', encoding='utf-8') as file:
                    self.WX_INSTRUCTION = file.read().strip()
            else:
                raise FileNotFoundError(f"The file '{self.WX_PROMPT_FILE_NAME}' does not exist in the current directory: {current_dir}")
        else:
            raise ValueError("Environment variable WX_PROMPT_FILE_NAME is not set or empty.")

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(os.environ.get('LOGLEVEL', 'INFO').upper())
        
    def callWatsonx(self, project_id, model_id, prompt_input, max_new_tokens):
        self.logger.info("------------------------------------------------ callWatsonx Started ------------------------------------------------")
        start_time = time.time()
        self.logger.info(f"Prompt : {prompt_input} ")
        print("------------------------------------------------ callWatsonx Started ------------------------------------------------")
        start_time = time.time()
        print(f"Prompt : {prompt_input} ")

        self.WX_ACCESS_TOKEN = IAMTokenManager(apikey = self.WX_APIKEY, url = self.IBMC_AUTH_URL).get_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.WX_ACCESS_TOKEN
            }
        
        parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": max_new_tokens,
            "min_new_tokens": 1,
            "repetition_penalty": 1,
            "stop_sequences": [
			"Input:"
		]
            }
        
        llmPayload = {
            "project_id": project_id,
            "model_id": model_id, 
            "parameters": parameters,
            "input": prompt_input
            }
        
        llmResponse = requests.post(self.WX_ENDPOINT_URL, json=llmPayload, headers=headers)
        if llmResponse.status_code == 200:
            output = llmResponse.json()["results"][0]["generated_text"]
        else:
            output = llmResponse.text

        result = {}
        result["status_code"] = llmResponse.status_code
        result["output"] = output
        
        end_time = time.time()
        execution_time = end_time - start_time
        self.logger.info(f"\n\n\nresult : {result} ")
        self.logger.info(f"\nExecution time: callWatsonx : {execution_time} seconds")
        self.logger.debug("----------------------------------- callWatsonx Completed------------------------------------------------\n\n\n")
        print(f"\n\n\nresult : {result} ")
        print(f"\nExecution time: callWatsonx : {execution_time} seconds")
        print("------------------------------------------------ callWatsonx Completed ------------------------------------------------\n\n\n")

        return result
    
    def code_generator(self,input_class):
        prompt_input = self.WX_INSTRUCTION + "\n" + "\n" + input_class + "\n\n"
        print("prompt = ",prompt_input)

        llmResponse = self.callWatsonx(self.WX_PROJECT_ID, self.WX_MODEL_ID, prompt_input, 2000)

        self.logger.debug(f"class name from llm : {llmResponse}")  
        self.logger.debug("------------------------------------------------ generate code Completed ------------------------------------------------")
        return llmResponse 
