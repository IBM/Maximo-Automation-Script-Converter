#Class name :cust.app.workorder.FldWorkTypeCust
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.mbo import MboConstants

try:
    worktype = mbo_value.getString("WORKTYPE")
    if worktype == "EM":
        mbo.setValue("WOPRIORITY", "1", MboConstants.NOVALIDATION_AND_NOACTION)
        mbo.setFieldFlag(worktype, MboConstants.READONLY, True)

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))