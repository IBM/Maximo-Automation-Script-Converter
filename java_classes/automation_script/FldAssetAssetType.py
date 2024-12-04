#Class name :cust.app.FldAssetAssetType
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.util import MXException
from psdi.mbo import MboConstants

try:
    asset = mbo_value.getMbo()
    value = mbo_value
    internal_asset_type = asset.getTranslator().toInternalString("ASSETTYPE", value.toString())

    if internal_asset_type.upper() == "PRODUCTION":
        asset.setFieldFlag("VENDOR", MboConstants.REQUIRED, True)
    else:
        asset.setFieldFlag("VENDOR", MboConstants.REQUIRED, False)

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))