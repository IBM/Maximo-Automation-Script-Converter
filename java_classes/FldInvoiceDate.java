package cust.app;

import java.rmi.RemoteException;
import java.util.Date;

import psdi.mbo.Mbo;
import psdi.mbo.MboValue;
import psdi.server.MXServer;
import psdi.util.MXApplicationException;
import psdi.util.MXException;

/* This custom class is applicable to object name INVOICE
 * attribute name INVOICEDATE, and launch point type ATTRIBUTE
 */

public class FldInvoiceDate extends psdi.app.invoice.FldInvoiceInvoiceDate {

    public FldInvoiceDate(MboValue mbv) throws MXException,RemoteException
    {
        super(mbv);
    }
    
    public void action() throws MXException, RemoteException {
        super.action();
        Mbo invoice = this.getMboValue().getMbo();
        Date curDate = MXServer.getMXServer().getDate();

        Date invoiceDate = invoice.getDate("invoicedate");
         
        if ( invoiceDate.before(curDate)) {
            Object[] params = {"Invoice Date"};
            throw new MXApplicationException("asset", "AsOfDateNotValid", params);
        }
    }
}
