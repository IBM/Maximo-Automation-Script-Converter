#Class name :cust.app.FldInvoiceDate
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.util import MXException, MXApplicationException
from psdi.mbo import MboConstants
from psdi.server import MXServer

try:
    invoice = mbo_value.getMbo()
    cur_date = MXServer.getMXServer().getDate()
    invoice_date = invoice.getDate("INVOICEDATE")

    if invoice_date < cur_date:
        raise MXApplicationException("asset", "AsOfDateNotValid", ["Invoice Date"])

except MXException as e:
    scriptLog.error("Got an MXException: " + str(e))
except Exception as e:
    scriptLog.error("Got an Exception: " + str(e))