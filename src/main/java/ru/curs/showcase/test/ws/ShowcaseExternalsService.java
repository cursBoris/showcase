
package ru.curs.showcase.test.ws;

import java.net.MalformedURLException;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import javax.xml.ws.WebEndpoint;
import javax.xml.ws.WebServiceClient;
import javax.xml.ws.WebServiceException;
import javax.xml.ws.WebServiceFeature;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.2.4-b01
 * Generated source version: 2.2
 * 
 */
@WebServiceClient(name = "ShowcaseExternalsService", targetNamespace = "http://showcase.curs.ru", wsdlLocation = "http://localhost:7777/Showcase/forall/webservices?wsdl")
public class ShowcaseExternalsService
    extends Service
{

    private final static URL SHOWCASEEXTERNALSSERVICE_WSDL_LOCATION;
    private final static WebServiceException SHOWCASEEXTERNALSSERVICE_EXCEPTION;
    private final static QName SHOWCASEEXTERNALSSERVICE_QNAME = new QName("http://showcase.curs.ru", "ShowcaseExternalsService");

    static {
        URL url = null;
        WebServiceException e = null;
        try {
            url = new URL("http://localhost:7777/Showcase/forall/webservices?wsdl");
        } catch (MalformedURLException ex) {
            e = new WebServiceException(ex);
        }
        SHOWCASEEXTERNALSSERVICE_WSDL_LOCATION = url;
        SHOWCASEEXTERNALSSERVICE_EXCEPTION = e;
    }

    public ShowcaseExternalsService() {
        super(__getWsdlLocation(), SHOWCASEEXTERNALSSERVICE_QNAME);
    }

    public ShowcaseExternalsService(WebServiceFeature... features) {
        super(__getWsdlLocation(), SHOWCASEEXTERNALSSERVICE_QNAME, features);
    }

    public ShowcaseExternalsService(URL wsdlLocation) {
        super(wsdlLocation, SHOWCASEEXTERNALSSERVICE_QNAME);
    }

    public ShowcaseExternalsService(URL wsdlLocation, WebServiceFeature... features) {
        super(wsdlLocation, SHOWCASEEXTERNALSSERVICE_QNAME, features);
    }

    public ShowcaseExternalsService(URL wsdlLocation, QName serviceName) {
        super(wsdlLocation, serviceName);
    }

    public ShowcaseExternalsService(URL wsdlLocation, QName serviceName, WebServiceFeature... features) {
        super(wsdlLocation, serviceName, features);
    }

    /**
     * 
     * @return
     *     returns ShowcaseExternals
     */
    @WebEndpoint(name = "ShowcaseExternalsPort")
    public ShowcaseExternals getShowcaseExternalsPort() {
        return super.getPort(new QName("http://showcase.curs.ru", "ShowcaseExternalsPort"), ShowcaseExternals.class);
    }

    /**
     * 
     * @param features
     *     A list of {@link javax.xml.ws.WebServiceFeature} to configure on the proxy.  Supported features not in the <code>features</code> parameter will have their default values.
     * @return
     *     returns ShowcaseExternals
     */
    @WebEndpoint(name = "ShowcaseExternalsPort")
    public ShowcaseExternals getShowcaseExternalsPort(WebServiceFeature... features) {
        return super.getPort(new QName("http://showcase.curs.ru", "ShowcaseExternalsPort"), ShowcaseExternals.class, features);
    }

    private static URL __getWsdlLocation() {
        if (SHOWCASEEXTERNALSSERVICE_EXCEPTION!= null) {
            throw SHOWCASEEXTERNALSSERVICE_EXCEPTION;
        }
        return SHOWCASEEXTERNALSSERVICE_WSDL_LOCATION;
    }

}
