#Class name :cust.app.FldPOTotalCost
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.util import MXException
from psdi.server import MXServer

try:
    mbo = mbo_value.getMbo()
    poTotalCost = mbo.getDouble("TOTALCOST")
    vendor = mbo.getString("VENDOR")
    approvalThreshold = 5000

    if vendor and poTotalCost <= approvalThreshold:
        mbo.changeStatus("APPR", MXServer.getMXServer().getDate(), "Auto-approved by script")

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))