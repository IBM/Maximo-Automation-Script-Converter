package cust.app;

import java.rmi.RemoteException;

import psdi.mbo.Mbo;
import psdi.mbo.MboValue;
import psdi.util.MXException;

/* This custom class is applicable to object name ASSET
 * attribute name VENDOR, and launch point type ATTRIBUTE
 */

public class FldAssetAssetType extends psdi.app.asset.FldAssetAssetType {

    public FldAssetAssetType(MboValue mbv) throws MXException,RemoteException
    {
        super(mbv);
    }
    
    public void action() throws MXException, RemoteException {
        super.action();
        Mbo asset = this.getMboValue().getMbo();
        MboValue value = this.getMboValue();
        String internalAssetType = asset.getTranslator().toInternalString("ASSETTYPE", value.toString());
        if ( internalAssetType.equalsIgnoreCase("PRODUCTION")) {        
            asset.setFieldFlag("VENDOR", REQUIRED, true);
        }
        else
            asset.setFieldFlag("VENDOR", REQUIRED, false);
    }
}
