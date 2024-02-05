#!/usr/bin/env python3
# use this to suspend like `python3 suspend_or_resume_fabric_capacity.py /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity suspend`
# use this to resume like `python3 suspend_or_resume_fabric_capacity.py /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity resume`
# use this to scale like `python3 suspend_or_resume_fabric_capacity.py /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity scale F4`
import argparse
import os

import requests

parser = argparse.ArgumentParser()
parser.add_argument("resource_id", help="The resource id of the capacity to change, e.g. /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity")
parser.add_argument("operation", help="The operation to perform, either suspend, resume or scale")
parser.add_argument("sku", nargs="?", help="The sku to scale to, e.g. F4")
args = parser.parse_args()

resource_id = args.resource_id

operation = "suspend"
if args.operation == "resume":
    operation = "resume"
if args.operation == "scale":
    operation = "scale"
    

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

baseurl = f"https://management.azure.com{resource_id}/"

if operation == "scale":
    sku = args.sku
    url = f"https://management.azure.com{resource_id}?api-version=2022-07-01-preview"
    print(f"INFO: Scaling {url} to {sku}")
    payload = {"sku":{"name": sku,"tier":"Fabric"}}
    response = requests.patch(url, headers={'Content-Type': 'application/json', "Authorization": f"Bearer {token}"}, json=payload)
    response.raise_for_status()

else:
    url = f"https://management.azure.com{resource_id}/{operation}?api-version=2022-07-01-preview"
    print(f"INFO: Calling {url}")
    response = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": f"Bearer {token}"})
    if not response.ok and response.json()["error"]["message"] == 'Service is not ready to be updated':
        print(f"WARN: Service is not ready to be updated, probably it is already in desired state: {operation}")
    else:
        response.raise_for_status()