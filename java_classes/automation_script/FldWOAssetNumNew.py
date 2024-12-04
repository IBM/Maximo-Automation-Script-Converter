#Class name :cust.app.workorder.FldWOAssetNumNew
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
# OBJECT: WORKORDER	ATTRIBUTE: ASSETNUM

from psdi.util import MXException
from psdi.mbo import MboConstants

try:
    assetnum = mbo_value.getString()

    if assetnum:
        woMbo = mbo_value.getMbo()
        childWOSet = woMbo.getMboSet("CHILDREN")
        childWO = childWOSet.moveFirst()

        while childWO is not None:
            childWO.setValue("ASSETNUM", assetnum, MboConstants.NOVALIDATION_AND_NOACTION)
            childWO = childWOSet.moveNext()

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))