package cust.app;


import java.rmi.RemoteException;

import psdi.mbo.Mbo;
import psdi.mbo.MboValue;
import psdi.util.MXException;

/* This custom class is applicable to object name SR
 * attribute name REPORTEDPRIRITY, and launch point type ATTRIBUTE
 */

public class FldTicketId extends psdi.app.ticket.FldTkTicketId {

    public FldTicketId(MboValue mbv) throws MXException,RemoteException
    {
        super(mbv);
    }
    
    public void action() throws MXException, RemoteException {
        super.action();
        Mbo ticket = this.getMboValue().getMbo();      
        String app = ticket.getThisMboSet().getApp();
        if (app!=null && app.equalsIgnoreCase("SR") ) {
            ticket.setValue("reportedprioty",2,NOACCESSCHECK);
        }
    }
}
