#!/usr/bin/env python3
# use this like `python3 suspend_or_resume_fabric_capacity.py /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity suspend`
import logging
import sys
import os

import requests


# resource_id = "/subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity"
resource_id = str(sys.argv[1])

# resume_or_suspend = "suspend"
resume_or_suspend = str(sys.argv[2])
operation = "suspend"
if resume_or_suspend == "resume":
    operation = "resume"

if os.getenv('IDENTITY_ENDPOINT'):
    # using managed identity
    endPoint = os.getenv('IDENTITY_ENDPOINT')+"?resource=https://management.azure.com/" 
    identityHeader = os.getenv('IDENTITY_HEADER') 
    payload={}
    headers = { 
    'X-IDENTITY-HEADER': identityHeader,
    'Metadata': 'True' 
    } 
    response = requests.request("GET", endPoint, headers=headers, data=payload) 
    response.raise_for_status()
    token = response.json()["access_token"]
else:
    from azure.identity import DefaultAzureCredential
    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/").token

url = f"https://management.azure.com{resource_id}/{operation}?api-version=2022-07-01-preview"
logging.info(f"Calling {url}")
response = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": f"Bearer {token}"})
if not response.ok and response.json()["error"]["message"] == 'Service is not ready to be updated':
    logging.warning(f"Service is not ready to be updated, probably it is already in desired state: {resume_or_suspend}")
else:
    response.raise_for_status()