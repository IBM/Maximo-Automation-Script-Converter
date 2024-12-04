package cust.app.workorder;

import java.rmi.RemoteException;

import psdi.app.workorder.FldWOPriority;
import psdi.mbo.MboValue;
import psdi.util.MXApplicationException;
import psdi.util.MXException;

public class FldWOPriorityCust extends FldWOPriority{

	public FldWOPriorityCust(MboValue mbv) {
		super(mbv);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void validate() throws MXException, RemoteException {
		super.validate();
		
		int wopriority = this.getMboValue().getInt();
		if (wopriority > 5) {
			throw new MXApplicationException("custerrgrp", "custerrkey");
		}
	}

}
