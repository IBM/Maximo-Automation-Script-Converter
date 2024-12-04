#Class name :cust.app.workorder.FldWOPriorityCust
#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
#OBJECTNAME:
#ATTRIBUTENAME: 
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION 
from psdi.util import MXException, MXApplicationException

class FldWOPriorityCust(FldWOPriority):

    def __init__(self, mbv):
        super(FldWOPriorityCust, self).__init__(mbv)

    def validate(self):
        super().validate()
        wopriority = self.getMboValue().getInt()
        if wopriority > 5:
            raise MXApplicationException("custerrgrp", "custerrkey")


Input: