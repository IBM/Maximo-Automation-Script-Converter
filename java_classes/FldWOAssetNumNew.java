// OBJECT: WORKORDER	ATTRIBUTE: ASSETNUM

package cust.app.workorder;

import java.rmi.RemoteException;

import psdi.mbo.MboRemote;
import psdi.mbo.MboSetRemote;
import psdi.mbo.MboValue;
import psdi.pluss.app.workorder.PlusSFldWOAssetNum;
import psdi.util.MXException;

public class FldWOAssetNumNew extends PlusSFldWOAssetNum {

	public FldWOAssetNumNew(MboValue arg0) throws MXException {
		super(arg0);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void action() throws RemoteException, MXException {
		super.action();
		
		String assetnum = this.getMboValue().getString();
		
		if (assetnum != "") {
			MboRemote woMbo = this.getMboValue().getMbo();
			MboSetRemote childWOSet = woMbo.getMboSet("CHILDREN");
			MboRemote childWO = childWOSet.moveFirst();
			
			while (childWO != null) {
				childWO.setValue("ASSETNUM", assetnum, NOVALIDATION_AND_NOACTION);
				childWO = childWOSet.moveNext();
			}
			
		}
		
	}
}
