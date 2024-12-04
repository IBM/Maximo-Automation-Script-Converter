#Class name :cust.app.FldTicketId
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.util import MXException
from psdi.mbo import MboConstants

try:
    mbo_value = mbo.getMboValue("REPORTEDPRIRITY")
    mbo = mbo_value.getMbo()
    app = mbo.getThisMboSet().getApp()
    if app and app.upper() == "SR":
        mbo.setValue("REPORTEDPRIRITY", 2, MboConstants.NOACCESSCHECK)
except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))