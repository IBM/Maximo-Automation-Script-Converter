package cust.app.workorder;

import java.rmi.RemoteException;
import java.util.Date;

import psdi.app.financial.FldPartialGLAccount;
import psdi.plusd.app.workorder.PlusDWORemote;
import psdi.mbo.MboValue;
import psdi.server.MXServer;
import psdi.util.MXException;


/*
This custom class is applicable to object name WORKORDER, attribute name GLACCOUNT, and launch point type ATTRIBUTE and Eventype RUN ACTION.
*/

public class FldGLAccNew extends FldPartialGLAccount {

	public FldGLAccNew(MboValue mbv) {
		super(mbv);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void action() throws RemoteException, MXException {
		super.action();
		
		PlusDWORemote woMbo = (PlusDWORemote) this.getMboValue().getMbo();
		
		String woGlAccount = this.getMboValue().getString();
		String woWorkType = this.getMboValue("WORKTYPE").getString();
		Date sysdate = MXServer.getMXServer().getDate();
		
		if (woGlAccount != null && woWorkType == "PM") {
			woMbo.changeStatus("APPR", sysdate, "Workorder Status moved to APPR");
		}

	}

}
