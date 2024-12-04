#Class name :cust.app.workorder.FldGLAccNew
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.util import MXException
from psdi.server import MXServer

try:
    mbo_value = mbo.getMboValue("GLACCOUNT")
    mbo_worktype = mbo.getMboValue("WORKTYPE")
    sys_date = MXServer.getMXServer().getDate()

    if mbo_value and mbo_worktype:
        if mbo_value.getString() and mbo_worktype.getString() == "PM":
            mbo.changeStatus("APPR", sys_date, "Workorder Status moved to APPR")

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))