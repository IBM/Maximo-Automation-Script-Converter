package cust.app.workorder;

import java.rmi.RemoteException;

import psdi.mbo.MboRemote;
import psdi.mbo.MboSetRemote;
import psdi.mbo.MboValue;
import psdi.mbo.MboValueAdapter;
import psdi.util.MXException;


/*
This custom class is applicable to object name WORKORDER, attribute name STATUS, and launch point type ATTRIBUTE and Eventype RUN ACTION.
*/

public class FldWOStatusNew extends MboValueAdapter {
	
	public FldWOStatusNew (MboValue mbv) {
		super(mbv);
	}
	
	public void action() throws MXException, RemoteException {
		MboRemote woMbo = this.getMboValue().getMbo();
		String woStatus = this.getMboValue().getString();
		
		if (woStatus.equals("COMP")) {
			MboSetRemote childMatUseTransSet = woMbo.getMboSet("SHOWACTUALMATERIAL");
			MboRemote childMatUseTransMbo = childMatUseTransSet.moveFirst();
			double totalCost = 0;
			
			while (childMatUseTransMbo != null) {
				double linecost = childMatUseTransMbo.getDouble("LINECOST");
				totalCost = totalCost + linecost;
				childMatUseTransMbo = childMatUseTransSet.moveNext();
			}
			woMbo.setValue("ACTMATCOST", totalCost, NOVALIDATION_AND_NOACTION);
		}
	}

}
