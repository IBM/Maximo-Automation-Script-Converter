package cust.app;

import java.rmi.RemoteException;

import psdi.mbo.Mbo;
import psdi.mbo.MboValue;
import psdi.server.MXServer;
import psdi.util.MXException;
import psdi.app.po.*;

/* This custom class is applicable to object name PO
 * attribute name TOTALCOST, and launch point type ATTRIBUTE
 */
public class FldPOTotalCost extends psdi.app.common.purchasing.FldPurTotalCost {

    public FldPOTotalCost(MboValue mbv) throws MXException,RemoteException
    {
        super(mbv);
    }
    
    public void validate() throws MXException, RemoteException {

        super.validate();
        Mbo po = this.getMboValue().getMbo();
        double approvalThreshold = 5000;

        double poTotalCost = po.getDouble("totalcost");
		String vendor = po.getString("vendor");
        if (vendor != null && poTotalCost <= approvalThreshold) {
			((PORemote) po).changeStatus("APPR", MXServer.getMXServer().getDate(), "Auto-approved by script");
        }
    }
}
