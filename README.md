# Suspend or Resume Fabric Capacity

## Usage
### Python
Use the python script via command line like 
```
python3 suspend_or_resume_fabric_capacity.py /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity suspend
```
### Powershell
Use the powershell script via command line like
```
suspend_or_resume_fabric_capacity.ps1 /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity suspend
```

### Parameters
#### Resource ID:
    Resource ID of the Capacity, can be found in the Azure Portal on the resource overview page in the top right when clicking on JSON View.
#### Operations:
    Can be either suspend or resume

## Azure Automation Runbook
To use the script as an Azure Runbook, the authentication will happen via the System Assigned Managed Identity of the Automation Account. That identity will need to have contributor rights on the Fabric Capacity resource.