#Class name :cust.app.workorder.FldWOStatusNew
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.mbo import MboConstants

try:
    mbo_value = mbo.getMboValue("STATUS")
    mbo = mbo_value.getMbo()
    worktype = mbo_value.getString("STATUS")

    if worktype == "COMP":
        childMatUseTransSet = mbo.getMboSet("SHOWACTUALMATERIAL")
        childMatUseTransMbo = childMatUseTransSet.moveFirst()
        totalCost = 0

        while childMatUseTransMbo is not None:
            linecost = childMatUseTransMbo.getDouble("LINECOST")
            totalCost += linecost
            childMatUseTransMbo = childMatUseTransSet.moveNext()

        mbo.setValue("ACTMATCOST", totalCost, MboConstants.NOVALIDATION_AND_NOACTION)

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))