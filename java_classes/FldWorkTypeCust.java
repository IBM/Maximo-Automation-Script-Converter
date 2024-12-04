package cust.app.workorder;

import java.rmi.RemoteException;

import psdi.app.workorder.FldWorkType;
import psdi.mbo.Mbo;
import psdi.mbo.MboValue;
import psdi.util.MXException;

/*
This custom class is applicable to object name WORKORDER, attribute name WORKTYPE, and launch point type ATTRIBUTE and Eventype RUN ACTION.
*/

public class FldWorkTypeCust extends FldWorkType {

	public FldWorkTypeCust(MboValue mbv) throws MXException {
		super(mbv);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void action() throws MXException, RemoteException {
		super.action();
		
		Mbo woRemote = this.getMboValue().getMbo();
		String worktype = this.getMboValue().getString();
		if (worktype == "EM") {
			woRemote.setValue("WOPRIORITY", "1", NOVALIDATION_AND_NOACTION);
			woRemote.setFieldFlag(worktype, READONLY, true);
		}
		
	}

}
