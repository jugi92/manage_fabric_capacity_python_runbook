# Suspend or Resume Fabric Capacity

## Usage
### Python
Use the python script via command line like 
```
python3 manage_fabric_capacity.py.py /subscriptions/12345678-1234-1234-1234-123a12b12d1c/resourceGroups/fabric-rg/providers/Microsoft.Fabric/capacities/myf2capacity suspend
```

### Parameters
#### Resource ID (required):
    Resource ID of the Capacity, can be found in the Azure Portal on the resource overview page in the top right when clicking on JSON View.
#### Operations (required):
    Can be either suspend, resume or scale
#### SKU (optional):
    Required if operation = scale, some SKU between F2 to F2048

## Azure Automation Runbook
To use the script as an Azure Runbook, the authentication will happen via the System Assigned Managed Identity of the Automation Account. That identity will need to have contributor rights on the Fabric Capacity resource.

Create Runbook:
![Create Runbook](media/01_Screenshot_Create_Runbook.png)

Choose from Gallery:
![Choose from Gallery](media/02_Screenshot_Choose_from_Gallery.png)

Search Gallery for "Fabric":
![Search Gallery for "Fabric"](media/03_Screenshot_Search_Gallery_For_Fabric.png)

Name the Runbook and select Python Runtime:
![Name the Runbook and select Python Runtime](media/04_Screenshot_Name_Runbook_and_Select_Runtime_Environment.png)

Publish the runbook:
![Publish the runbook](media/05_Screenshot_Publish_Runbook.png)

Go to schedules:
![Go to schedules](media/06_Screenshot_Go_To_Schedules.png)

Get Ressource ID of your Fabric Capacity
![Get Ressource ID of your Fabric Capacity](media/07_Screenshot_Get_Fabric_Capacity_Ressource_ID.png)

Copy the Ressource ID
![Copy the Ressource ID](media/08_Screenshot_Copy_Fabric_Capacity_Ressource_ID.png)

Put Capacity ID and the Operations (e.g. "suspend") as parameter
![Put Capacity ID and the Operations (e.g. "suspend") as parameter](media/09_Screenshot_Set_Capacity_ID_and_operation_as_parameter.png)

Create Identity for Automation Account and copy the Object ID
![Create Identity for Automation Account and copy the Object ID](media/10_Screenshot_Assign_Identity_And_Copy_Object_ID.png)

On the Fabric Capacity assign the contributor role to the Automation Account Object ID
![On the Fabric Capacity assign the contributor role to the Automation Account Object ID](media/11_Screenshot_Assign_Contributor_Role_To_AutomationAccountIdentity.png)